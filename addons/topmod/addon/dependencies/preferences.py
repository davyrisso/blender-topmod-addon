from bpy import utils
from bpy.types import AddonPreferences, Context
from topmod.addon.dependencies import install_utils, operators


class TOPMOD_dependencies_preferences(AddonPreferences):
    bl_idname = __package__.split(".")[0]

    def draw(self, context: Context):
        if install_utils.is_pytopmod_installed():
            self.layout.label(text="Dependencies installed", icon="CHECKMARK")
        else:
            self.layout.label(text="Dependencies not installed", icon="ERROR")
            self.layout.operator(
                operators.InstallDependenciesOperator.bl_idname,
                icon="CONSOLE",
            )


CLASSES = (TOPMOD_dependencies_preferences,)


def register():
    for cls in CLASSES:
        utils.register_class(cls)


def unregister():
    for cls in CLASSES:
        utils.unregister_class(cls)
