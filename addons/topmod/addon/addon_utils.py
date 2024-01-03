def reload_addon():
    import importlib
    import sys

    from topmod.addon import dependencies

    importlib.reload(dependencies)

    sys.modules[__name__] = importlib.reload(sys.modules[__name__])
    for name, module in list(sys.modules.items()):
        if (
            hasattr(module, "__package__")
            and module.__package__ is not None
            and module.__package__.startswith(__name__)
        ):
            sys.modules[name] = importlib.reload(module)


def register_addon():
    from topmod import addon

    addon.register()


def unregister_addon():
    from topmod import addon

    addon.unregister()
