bl_info = {
    "name": "Topmod",
    "author": "Topmod Team",
    "location": "View3D > Sidebar > Topmod",
    "version": (0, 1, 0),
    "blender": (3, 0, 0),
    "description": "Topmod",
    "category": "3D View",
}

if "topmod" in locals():
    from topmod.addon import addon_utils
    from topmod.addon.dependencies import install_utils

    if install_utils.is_pytopmod_installed():
        addon_utils.reload_addon()


def register():
    from topmod.addon import addon_utils

    addon_utils.register_addon()


def unregister():
    from topmod.addon import addon_utils

    addon_utils.unregister_addon()
