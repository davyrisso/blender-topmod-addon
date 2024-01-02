# Topmod Blender Addon

## Install

1. Download a [release](https://github.com/davyrisso/blender-topmod-addon/tags) `.zip` file ([`topmod.zip`](https://github.com/davyrisso/blender-topmod-addon/releases/download/v0.1.0-alpha/topmod.zip))
2. In Blender: `Edit` > `Preferences` > `Add-ons` > `Install` > Select the `topmod.zip` file downloaded in step 1.

## Developer Workflow

### Blender Setup

1. Download and Install Blender

   [Daily Builds](https://builder.blender.org/download/daily/)

2. Clone this repository:

   `git clone https://github.com/davyrisso/blender-topmod-addon.git`

3. Add the root of the repository to Blender's script directories

   `Edit` > `Preferences` > `File Paths` > `Script Directories` > `Add (+)`

   **Note**: Make sure to use the root of the directory (`blender-topmod-addon`) in which there is an `addons` directory.

4. Reload scripts in Blender

   `Blender Menu` > `System` > `Reload Scripts`

5. Enable the addon

   - The addon should now be visible in the installed addons: `Edit` > `Preferences` > `Add-ons` under `3DView - Topmod`
   - Check the checkbox to enable the addon

6. Install dependencies

   - Click the `Install Dependencies` button in the Addon preferences.

**Note**: Removing the addon at this point from the `Add-ons` preferences in Blender will _**delete the addon source files**_, when working on the addon make sure you do not remove the addon, and make sure to commit often!

### Dev Environment Setup

1. Create a virtual environment

   ```
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Install `requirements` and `requirements_dev`

   ```
   pip install -r requirements.txt
   pip install -r requirements_dev.txt
   ```

3. Optional: IDE Setup (VSCode)

   VSCode should pick up automatically the virtual environment setup in step 1., if it is not the case, select the interpreter:

   - `Cmd+P` > `Python: Select Interpreter`
   - Select `./.venv/bin.python`

   Recommended extensions: Flake8, MyPy, Isort, Black.

   **Note**: You may need to reload the VSCode window for the interpreter to pick up the dev dependencies (in particular bpy-fake-module), in which case do: `Cmd+P` > `Developer: Reload Window`.

### Development workflow

- Run Blender **from the command line** to see all print statements
- Use `Reload Scripts` when making changes: `Blender Menu` > `System` > `Reload Scripts`.

  **Note**: For some changes, you might need to disable/re-enable the addon. Rarely, you will need to restart Blender.
