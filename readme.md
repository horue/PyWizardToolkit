# PyInstallerToolKit

**PyInstallerToolKit** is a tool designed to automate the creation of Python project installers, including virtual environment setup, dependency installation, and shortcut creation. It serves as an alternative to PyInstaller, especially when you face difficulties in bundling all the necessary libraries in the package.

## Features

- **Shortcut Creation**: Generates desktop shortcuts for the user.
- **Full Installation Setup**: Generates `.bat`, `.vbs` scripts, and `requirements.txt` for the virtual environment.
- **Automatic Installer**: Creates an installer that sets up the virtual environment, installs dependencies, and configures the app.
- **Venv Support**: The tool uses a virtual environment to isolate the dependencies of your project.

## How It Works

### 1. **Project Setup**
`installer-gen.py` helps generate an installer for your Python project. It performs the following steps:
   - Creates a virtual environment.
   - Generates the `requirements.txt` based on the current Python project dependencies.
   - Creates `.bat` and `.vbs` files to automate the launching process of your Python script.
   - Allows you to choose the directory where the project will be installed.

### 2. **Creating the Installer**
After the project setup, the tool creates an installer that will do the following when run:
   - Create a virtual environment (`.venv`).
   - Install all dependencies listed in the `requirements.txt`.
   - Create a shortcut on the desktop for easy access.

### 3. **Scripts Generated**
The following files are generated:
   - `installer.bat`: Used to activate the virtual environment and run the script.
   - `app.vbs`: A Visual Basic script to run the `.bat` file without opening a command prompt.
   - `requirements.txt`: Contains a list of dependencies to install into the virtual environment.
   - `create_shortcut.vbs`: A Visual Basic script that creates a shortcut on the desktop to launch the application.

## How to Use

### Step 1: Generate `.bat` and `.vbs` Files
Run the `bat-vbs-gen.py` script. This will prompt you to select a Python script and the directory where the files will be saved. It will generate the `.bat` and `.vbs` files needed to launch the application.

### Step 2: Generate the Installer
Run the `installer-gen.py` script. This will:
   - Set up a virtual environment.
   - Create the `requirements.txt` from the active virtual environment.
   - Set up the installer that installs the dependencies and sets up the environment.

### Step 3: Create Desktop Shortcut
The `shortcup.py` script creates a shortcut on the desktop that points to the generated `.vbs` script.

### Step 4: Run the Installer
Once everything is set up, you can share the installer package with the user. When they run the installer, it will automatically:
   - Install the necessary dependencies.
   - Create a shortcut to easily launch the application.

## Requirements

- Python 3.x
- `subprocess` module (included in Python standard library)
- Windows OS (for `.vbs` and `.bat` compatibility)

## License

