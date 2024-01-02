import importlib
import sys

bl_info = {
    "name": "Topmod",
    "author": "Topmod Team",
    "location": "View3D > Sidebar > Topmod",
    "version": (0, 1, 0),
    "blender": (3, 0, 0),
    "description": "Topmod",
    "category": "3D View",
}


def reload():
    print("RELOADING TOPMOD")
    sys.modules[__name__] = importlib.reload(sys.modules[__name__])
    for name, module in list(sys.modules.items()):
        if (
            hasattr(module, "__package__")
            and module.__package__ is not None
            and module.__package__.startswith(__name__)
        ):
            sys.modules[name] = importlib.reload(module)


reload()


def register():
    from topmod import addon

    addon.register()


def unregister():
    from topmod import addon

    addon.unregister()
