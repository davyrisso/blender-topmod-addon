from bpy.types import Context, Panel
from topmod.addon.dependencies import operators, utils


class TOPMOD_PT_dependencies_panel(Panel):
    bl_label = "Dependencies"
    bl_category = "Topmod"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    @classmethod
    def poll(cls, context: Context):
        return not utils.is_pytopmod_installed()

    def draw(self, context: Context):
        self.layout.label(text="Dependencies not installed", icon="ERROR")
        self.layout.operator(
            operators.TOPMOD_OT_install_dependencies.bl_idname,
            icon="CONSOLE",
        )
