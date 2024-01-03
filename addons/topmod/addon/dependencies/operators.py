import subprocess

from bpy import utils
from bpy.types import Context, Operator
from topmod.addon import module_utils
from topmod.addon.dependencies import install_utils


class InstallDependenciesOperator(Operator):
    bl_idname = "topmod.install_dependencies"
    bl_label = "Install Dependencies"
    bl_description = (
        "Downloads and installs the required python packages for topmod add-on. "
        "An internet connection is required."
    )
    bl_options = {"REGISTER", "INTERNAL"}

    @classmethod
    def poll(cls, context: Context) -> bool:
        return not install_utils.is_pytopmod_installed()

    def execute(self, context: Context) -> set[str]:
        try:
            install_utils.install_pytopmod()
            module_utils.reload_addon()
        except (subprocess.CalledProcessError, ImportError) as err:
            self.report({"ERROR"}, str(err))
            return {"CANCELLED"}

        return {"FINISHED"}


CLASSES = (InstallDependenciesOperator,)


def register():
    for cls in CLASSES:
        utils.register_class(cls)


def unregister():
    for cls in CLASSES:
        utils.unregister_class(cls)
