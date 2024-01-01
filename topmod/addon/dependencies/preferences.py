from bpy.types import AddonPreferences, Context

from topmod.addon.dependencies import operators, utils


class TOPMOD_dependencies_preferences(AddonPreferences):
    bl_idname = "topmod"

    def draw(self, context: Context):
        if utils.is_pytopmod_installed():
            self.layout.label(text="Dependencies installed", icon="CHECKMARK")
        else:
            self.layout.label(text="Dependencies not installed", icon="ERROR")
            self.layout.operator(
                operators.TOPMOD_OT_install_dependencies.bl_idname,
                icon="CONSOLE",
            )
