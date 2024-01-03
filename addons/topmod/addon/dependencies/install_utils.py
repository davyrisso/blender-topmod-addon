PYTOPMOD_GIT_URL = "https://github.com/topmod-org/pytopmod-core.git"


def is_pytopmod_installed() -> bool:
    import importlib
    import sys

    if "pytopmod" in sys.modules:
        return True
    else:
        try:
            importlib.import_module("pytopmod")
            return True
        except ModuleNotFoundError:
            return False


def install_pytopmod() -> None:
    import ensurepip
    import subprocess
    import sys

    ensurepip.bootstrap()
    subprocess.run(
        [
            sys.executable,
            "-m",
            "pip",
            "install",
            f"git+{PYTOPMOD_GIT_URL}",
        ]
    )


def uninstall_pytopmod():
    import subprocess
    import sys

    subprocess.run(
        [
            sys.executable,
            "-m",
            "pip",
            "uninstall",
            "-y",
            "pytopmod",
        ]
    )
