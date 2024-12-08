import os
import subprocess
import platform
import curses

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

def tui_setup(stdscr):
    """TUI for selecting and setting up development environment."""
    curses.curs_set(0)
    stdscr.clear()

    options = [
        "Install Python",
        "Install Visual Studio Code",
        "Install PostgreSQL",
        "Install Docker",
        "Create Folder Structure",
        "Exit"
    ]
    selected_index = 0

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "Dev Machine Setup", curses.A_BOLD | curses.A_UNDERLINE)

        for idx, option in enumerate(options):
            if idx == selected_index:
                stdscr.addstr(idx + 2, 2, f"> {option}", curses.A_REVERSE)
            else:
                stdscr.addstr(idx + 2, 2, f"  {option}")

        stdscr.refresh()

        key = stdscr.getch()
        if key == curses.KEY_UP and selected_index > 0:
            selected_index -= 1
        elif key == curses.KEY_DOWN and selected_index < len(options) - 1:
            selected_index += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            stdscr.clear()
            stdscr.addstr(0, 0, f"Selected: {options[selected_index]}")
            stdscr.refresh()

            if options[selected_index] == "Install Python":
                stdscr.addstr(1, 0, "Installing Python...")
                stdscr.refresh()
                success = install_package("python3", "sudo apt install -y python3")
                stdscr.addstr(2, 0, "Success" if success else "Failed")
            elif options[selected_index] == "Install Visual Studio Code":
                stdscr.addstr(1, 0, "Installing Visual Studio Code...")
                stdscr.refresh()
                success = install_package("code", "sudo apt install -y code")
                stdscr.addstr(2, 0, "Success" if success else "Failed")
            elif options[selected_index] == "Install PostgreSQL":
                stdscr.addstr(1, 0, "Installing PostgreSQL...")
                stdscr.refresh()
                success = install_package("postgresql", "sudo apt install -y postgresql")
                stdscr.addstr(2, 0, "Success" if success else "Failed")
            elif options[selected_index] == "Install Docker":
                stdscr.addstr(1, 0, "Installing Docker...")
                stdscr.refresh()
                success = install_package("docker", "sudo apt install -y docker.io")
                stdscr.addstr(2, 0, "Success" if success else "Failed")
            elif options[selected_index] == "Create Folder Structure":
                stdscr.addstr(1, 0, "Creating folder structure in ~/projects...")
                stdscr.refresh()
                create_folder_structure(os.path.expanduser("~/projects"))
                stdscr.addstr(2, 0, "Folder structure created!")
            elif options[selected_index] == "Exit":
                break

            stdscr.addstr(4, 0, "Press any key to continue...")
            stdscr.refresh()
            stdscr.getch()

if __name__ == "__main__":
    if platform.system() not in ["Linux", "Darwin"]:
        print("This script currently supports only Linux and macOS.")
    else:
        curses.wrapper(tui_setup)
