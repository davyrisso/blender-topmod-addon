from bpy import utils
from bpy.props import EnumProperty
from bpy.types import Context, Event, Operator


class CreateManifoldFromMeshOperator(Operator):
    bl_idname = "TOPMOD_OT_creation_manifold_from_mesh"
    bl_label = "Create from Mesh"
    bl_description = "Creates a Topmod manifold from an existing Blender mesh"
    bl_options = {"REGISTER", "INTERNAL"}

    structure: EnumProperty(  # type: ignore
        items=(("DLFL", "DLFL", ""), ("DCEL", "DCEL", ""))
    )

    @classmethod
    def poll(cls, context: Context) -> bool:
        return context.object.type == "MESH"

    def invoke(self, context: Context, event: Event):
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context: Context):
        return {"FINISHED"}


class CreateManifoldPrimitiveOperator(Operator):
    bl_idname = "TOPMOD_OT_creation_manifold_primitive"
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
    def poll(cls, context: Context):
        return True

    def draw(self, context: Context):
        self.layout.prop(self, "structure")
        self.layout.prop(self, "primitive_kind")

    def invoke(self, context: Context, event: Event):
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context: Context):
        return {"FINISHED"}


CLASSES = (
    CreateManifoldFromMeshOperator,
    CreateManifoldPrimitiveOperator,
)


def register():
    for cls in CLASSES:
        utils.register_class(cls)


def unregister():
    for cls in CLASSES:
        utils.unregister_class(cls)
