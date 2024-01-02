from topmod.addon.creation import operators, ui

MODULES = (operators, ui)


def register():
    for module in MODULES:
        module.register()


def unregister():
    for module in MODULES:
        module.unregister()
