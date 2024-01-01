import subprocess

from bpy.types import Context, Operator
from topmod.addon.dependencies import utils


class TOPMOD_OT_install_dependencies(Operator):
    bl_idname = "topmod.install_dependencies"
    bl_label = "Install Dependencies"
    bl_description = (
        "Downloads and installs the required python packages for topmod add-on. "
        "An internet connection is required."
    )
    bl_options = {"REGISTER", "INTERNAL"}

    @classmethod
    def poll(cls, context: Context):
        return not utils.is_pytopmod_installed()

    def execute(self, context: Context):
        try:
            utils.install_pytopmod()
        except (subprocess.CalledProcessError, ImportError) as err:
            self.report({"ERROR"}, str(err))
            return {"CANCELLED"}

        return {"FINISHED"}
