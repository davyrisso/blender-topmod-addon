from topmod.addon import dependencies
from topmod.addon.dependencies import install_utils


def register():
    dependencies.register()

    if install_utils.is_pytopmod_installed():
        from topmod.addon import creation

        creation.register()


def unregister():
    from topmod.addon import creation

    creation.unregister()
