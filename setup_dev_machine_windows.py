import os
import subprocess
import platform
from prompt_toolkit import prompt
from prompt_toolkit.validation import Validator, ValidationError

def install_package(package_name, install_command):
    """Installs a package using the system's package manager."""
    try:
        subprocess.run(install_command, shell=True, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

def create_folder_structure(base_dir):
    """Creates folder structure for projects."""
    folders = ['personal', 'work']
    for folder in folders:
        path = os.path.join(base_dir, folder)
        os.makedirs(path, exist_ok=True)

def get_user_selection():
    """Prompts user to choose an option."""
    options = [
        "1. Install Python",
        "2. Install Visual Studio Code",
        "3. Install PostgreSQL",
        "4. Install Docker",
        "5. Create Folder Structure",
        "6. Exit"
    ]

    # Show options to the user
    print("\n".join(options))

    # Get input and validate
    while True:
        selection = prompt("Please select an option by number (1-6): ")

        if selection in ['1', '2', '3', '4', '5', '6']:
            return int(selection)
        else:
            print("Invalid selection, please enter a number between 1 and 6.")

def setup_dev_environment():
    """Interactive menu for setting up the development environment."""
    while True:
        user_choice = get_user_selection()

        if user_choice == 1:
            print("Installing Python...")
            success = install_package("Python", "winget install -e --id Python.Python.3")
            print("Python installation", "successful!" if success else "failed.")
        elif user_choice == 2:
            print("Installing Visual Studio Code...")
            success = install_package("VS Code", "winget install -e --id Microsoft.VisualStudioCode")
            print("VS Code installation", "successful!" if success else "failed.")
        elif user_choice == 3:
            print("Installing PostgreSQL...")
            success = install_package("PostgreSQL", "winget install -e --id PostgreSQL.PostgreSQL")
            print("PostgreSQL installation", "successful!" if success else "failed.")
        elif user_choice == 4:
            print("Installing Docker...")
            success = install_package("Docker", "winget install -e --id Docker.DockerDesktop")
            print("Docker installation", "successful!" if success else "failed.")
        elif user_choice == 5:
            print("Creating folder structure in C:\\projects...")
            create_folder_structure("C:\\projects")
            print("Folder structure created!")
        elif user_choice == 6:
            print("Exiting the setup.")
            break

if __name__ == "__main__":
    if platform.system() != "Windows":
        print("This script is designed to run on Windows only.")
    else:
        setup_dev_environment()
