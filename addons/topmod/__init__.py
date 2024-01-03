from topmod.addon import module_utils

bl_info = {
    "name": "Topmod",
    "author": "Topmod Team",
    "location": "View3D > Sidebar > Topmod",
    "version": (0, 1, 0),
    "blender": (3, 0, 0),
    "description": "Topmod",
    "category": "3D View",
}

module_utils.reload_addon()


def register():
    from topmod import addon

    addon.register()


def unregister():
    from topmod import addon

    addon.unregister()
