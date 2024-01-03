import bpy  # noqa: F401.
from pytopmod.core.dlfl import mesh as dlfl_mesh

import bmesh  # isort: skip


def bmesh_to_dlfl(input_mesh: bmesh.types.BMesh) -> dlfl_mesh.DLFLMesh:
    output_mesh = dlfl_mesh.DLFLMesh()

    input_mesh.verts.ensure_lookup_table()

    vertices = {
        vertex.index: output_mesh.create_vertex(vertex.co)
        for vertex in input_mesh.verts
    }
    faces = {face.index: output_mesh.create_face() for face in input_mesh.faces}

    for face in input_mesh.faces:
        for loop in face.loops:
            output_mesh.face_vertices[faces[face.index]].append(
                vertices[loop.vert.index]
            )

            start_loop = loop
            if (
                faces[face.index]
                not in output_mesh.vertex_faces[vertices[loop.vert.index]]
            ):
                output_mesh.vertex_faces[vertices[loop.vert.index]].add(
                    faces[face.index]
                )

            loop = loop.link_loop_radial_next
            while loop != start_loop:
                if (
                    faces[face.index]
                    not in output_mesh.vertex_faces[vertices[loop.vert.index]]
                ):
                    output_mesh.vertex_faces[vertices[loop.vert.index]].add(
                        faces[face.index]
                    )
                loop = loop.link_loop_radial_next

    return output_mesh


def dlfl_to_bmesh(input_mesh: dlfl_mesh.DLFLMesh) -> bmesh.types.BMesh:
    output_mesh = bmesh.new()

    vertex_index_map = {}
    for index, vertex_key in enumerate(input_mesh.vertex_keys):
        vertex_index_map[vertex_key] = output_mesh.verts.new(
            input_mesh.vertex_coordinates[vertex_key]
        )

    for face_key in input_mesh.face_keys:
        output_mesh.faces.new(
            [
                vertex_index_map[vertex_key]
                for vertex_key in input_mesh.face_vertices[face_key]
            ]
        )

    return output_mesh


def dlfl_to_dict(mesh: dlfl_mesh.DLFLMesh) -> dict[str, list | dict[str, list]]:
    return {
        "vertices": [vertex_key for vertex_key in mesh.vertex_keys],
        "faces": [face_key for face_key in mesh.face_keys],
        "face_vertices": {
            face_key: vertices for face_key, vertices in mesh.face_vertices.items()
        },
    }
