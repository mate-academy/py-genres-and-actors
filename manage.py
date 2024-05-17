import os
import sys


def main() -> None:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                          "py-genres-and-actors.settings")

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
