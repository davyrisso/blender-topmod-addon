from topmod.addon import dependencies

MODULES = (dependencies,)


def register():
    for module in MODULES:
        print("REGISTERING", module)
        module.register()


def unregister():
    for module in MODULES:
        module.unregister()
