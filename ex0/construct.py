import site
import os
import sys


def main():

    # sys.prefix = current python path
    # sys.base_prefix = global env python path

    current_python = sys.executable
    in_virtual_env = True
    if sys.prefix == sys.base_prefix:
        in_virtual_env = False

    venv_name = current_python.split('/')[-3]
    if in_virtual_env is False:

        print("\nMATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {current_python}")
        print(f"Virtual Environment: {os.getenv(venv_name)} detected\n")

        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")

        print("\nTo enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\nScripts\nactivate    #On Windows\n")

        print("Then run this program again.")

    elif in_virtual_env is True:

        try:
            package_path = site.getsitepackages()
            print("\nMATRIX STATUS: Welcome to the construct\n")
            print(f"Current Python: {current_python}")
            print(f"Virtual environment: {venv_name}")
            print(f"Environment Path: {sys.prefix}\n")

            print("SUCCESS: You're in an isolated environment!")
            print("Safe to install packages without affecting"
                  " the global system.\n")
            print(f"Package installation path:\n{package_path[0]}")

        except Exception as e:
            print(f"Error: {e}")


if __name__ == '__main__':
    main()
