from types import ModuleType
from typing import Tuple

from topmod.addon import dependencies
from topmod.addon.dependencies import install_utils


def get_modules() -> Tuple[ModuleType, ...]:
    from topmod.addon import creation

    return (creation,)


def register():
    dependencies.register()

    if install_utils.is_pytopmod_installed():
        for module in get_modules():
            module.register()


def unregister():
    dependencies.unregister()

    if install_utils.is_pytopmod_installed():
        for module in get_modules():
            try:
                module.unregister()
            except RuntimeError as e:
                print(e)
