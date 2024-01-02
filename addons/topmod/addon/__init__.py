from topmod.addon import creation, dependencies

MODULES = (dependencies, creation)


def register():
    for module in MODULES:
        module.register()


def unregister():
    for module in MODULES:
        module.unregister()
