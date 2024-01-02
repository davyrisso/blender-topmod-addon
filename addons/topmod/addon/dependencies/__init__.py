from bpy import utils as bpy_utils
from topmod.addon.dependencies import operators, preferences, ui

CLASSES = (
    operators.TOPMOD_OT_install_dependencies,
    preferences.TOPMOD_dependencies_preferences,
    ui.TOPMOD_PT_dependencies_panel,
)


def register():
    for cls in CLASSES:
        bpy_utils.register_class(cls)


def unregister():
    for cls in CLASSES:
        bpy_utils.unregister_class(cls)  # pyright: ignore[reportUnknownMemberType]
