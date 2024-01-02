from bpy import utils
from bpy.types import Context, Panel
from topmod.addon.dependencies import install_utils, operators


class DependenciesPanel(Panel):
    bl_idname = "TOPMOD_PT_dependencies_panel"
    bl_label = "Dependencies"
    bl_category = "Topmod"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    @classmethod
    def poll(cls, context: Context) -> bool:
        return not install_utils.is_pytopmod_installed()

    def draw(self, context: Context):
        self.layout.label(text="Dependencies not installed", icon="ERROR")
        self.layout.operator(
            operators.InstallDependenciesOperator.bl_idname,
            icon="CONSOLE",
        )


classes = (DependenciesPanel,)


def register():
    for cls in classes:
        utils.register_class(cls)


def unregister():
    for cls in classes:
        utils.unregister_class(cls)
