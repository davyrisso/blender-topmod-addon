from typing import cast

from bpy import utils
from bpy.props import EnumProperty
from bpy.types import Context, Event, Mesh, Operator
from topmod.core import converters

import bmesh  # isort: skip


class TOPMOD_OT_create_manifold_from_mesh(Operator):
    bl_idname = "topmod.create_manifold_from_mesh"
    bl_label = "Create from Mesh"
    bl_description = "Creates a Topmod manifold from an existing Blender mesh"
    bl_options = {"REGISTER", "INTERNAL"}

    structure: EnumProperty(  # type: ignore
        items=(("DLFL", "DLFL", ""), ("DCEL", "DCEL", ""))
    )

    @classmethod
    def poll(cls, context: Context) -> bool:
        return context.object.type == "MESH" and not context.object.get("is_manifold")

    def invoke(self, context: Context, event: Event) -> set[str] | set[int]:
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context: Context) -> set[str]:
        mesh = bmesh.new()
        mesh.from_mesh(cast(Mesh, context.object.data))
        dlfl_mesh = converters.bmesh_to_dlfl(mesh)
        context.object["is_manifold"] = True
        context.object["dlfl_mesh"] = converters.dlfl_to_dict(dlfl_mesh)
        return {"FINISHED"}


class TOPMOD_OT_create_manifold_primitive(Operator):
    bl_idname = "topmod.create_manifold_primitive"
    bl_label = "Create Manifold Primitive"
    bl_description = "Creates a Topmod manifold primitive"
    bl_options = {"REGISTER", "INTERNAL"}

    structure: EnumProperty(  # type: ignore
        name="Structure",
        items=(("DLFL", "DLFL", ""), ("DCEL", "DCEL", "")),
    )
    primitive_kind: EnumProperty(  # type: ignore
        name="Kind",
        items=(
            ("POINT_SPHERE", "Point-Sphere", "", "SPHERE", 0),
            ("NGON", "N-Gon", "", "MESH_PLANE", 1),
            ("PLATONIC_SOLID", "Platonic Solid", "", "CUBE", 2),
        ),
    )

    @classmethod
    def poll(cls, context: Context) -> bool:
        return True

    def invoke(self, context: Context, event: Event) -> set[str] | set[int]:
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context: Context) -> set[str]:
        return {"FINISHED"}


CLASSES = (
    TOPMOD_OT_create_manifold_from_mesh,
    TOPMOD_OT_create_manifold_primitive,
)


def register():
    for cls in CLASSES:
        utils.register_class(cls)


def unregister():
    for cls in CLASSES:
        utils.unregister_class(cls)
