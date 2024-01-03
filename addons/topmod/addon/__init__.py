from topmod.addon import creation, dependencies
from topmod.addon.dependencies import install_utils

MODULES = (creation,)


def register():
    dependencies.register()

    if install_utils.is_pytopmod_installed():
        for module in MODULES:
            module.register()


def unregister():
    for module in MODULES:
        module.unregister()
