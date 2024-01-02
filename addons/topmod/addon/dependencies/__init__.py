from topmod.addon.dependencies import operators, preferences, ui

MODULES = (
    operators,
    preferences,
    ui,
)


def register():
    for module in MODULES:
        module.register()


def unregister():
    for module in MODULES:
        module.unregister()
