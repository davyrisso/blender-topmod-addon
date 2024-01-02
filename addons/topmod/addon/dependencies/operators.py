import subprocess

from bpy.types import Context, Operator

from addons.topmod.addon.dependencies import install_utils


class InstallDependenciesOperator(Operator):
    bl_idname = "TOPMOD_OT_install_dependencies"
    bl_label = "Install Dependencies"
    bl_description = (
        "Downloads and installs the required python packages for topmod add-on. "
        "An internet connection is required."
    )
    bl_options = {"REGISTER", "INTERNAL"}

    @classmethod
    def poll(cls, context: Context):
        return not install_utils.is_pytopmod_installed()

    def execute(self, context: Context):
        try:
            install_utils.install_pytopmod()
        except (subprocess.CalledProcessError, ImportError) as err:
            self.report({"ERROR"}, str(err))
            return {"CANCELLED"}

        return {"FINISHED"}


CLASSES = (InstallDependenciesOperator,)


def register():
    for cls in CLASSES:
        install_utils.register_class(cls)


def unregister():
    for cls in CLASSES:
        install_utils.unregister_class(cls)
