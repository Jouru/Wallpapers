import os
import sys
import argparse
from time import sleep
from random import randint


def main():
    parser = argparse.ArgumentParser(description="Wallpapers")
    parser.add_argument("--set", help="Set default values", action="store_true")
    parser.add_argument("-time", help="Define time in minutes", type=int)
    parser.add_argument("-path", help="Define path")
    parser.add_argument(
        "--theme", help="Define Wallpapers theme, case sensitive", action="store_true"
    )
    args = parser.parse_args()

    # Create the config file
    config_file = "wallpapers.conf"
    if not os.path.isfile(config_file):
        with open(config_file, "w") as file:
            time = "60"
            path = "/home/abner/Wallpapers"
            theme = "pictures"
            file.write(f"Time= {time}\n")
            file.write(f"PATH= {path}\n")
            file.write(f"THEME= {theme}")

    if args.set:
        # Define a new time
        if args.time:
            new_time = args.time
            with open(config_file, "r") as file:
                lines = file.readlines()
            for line in range(len(lines)):
                if lines[line].startswith("Time="):
                    lines[line] = f"Time= {new_time}"

            with open(config_file, "w") as file:
                for line in range(len(lines)):
                    file.write(f"{lines[line].strip()}\n")

        # Define a new path
        if args.path:
            with open(config_file, "r") as file:
                lines = file.readlines()
            for line in range(len(lines)):
                if lines[line].startswith("PATH="):
                    lines[line] = f"PATH= {args.path}"

            with open(config_file, "w") as file:
                for line in range(len(lines)):
                    file.write(f"{lines[line].strip()}\n")

    # Define the wallpapers theme
    elif args.theme:
        with open(config_file, "r") as file:
            lines = file.readlines()
        themes = os.listdir(lines[1].lstrip("PATH= ").strip())
        for theme in themes:
            print(theme, end=" ")
        theme = input("\nWhich theme do you want apply ")

        if theme not in themes:
            sys.exit(f"{theme} doesn't exist in your themes")

        for line in range(len(lines)):
            if lines[line].startswith("THEME="):
                lines[line] = f"THEME= {theme}"

        with open(config_file, "w") as file:
            for line in lines:
                file.write(f"{line.strip()}\n")

    else:
        with open(config_file, "r") as file:
            new_lines = file.readlines()

        # Get time and path to wallpapers directory
        _, sub_pth = new_lines[2].split(" ")
        pth = f"{new_lines[1].lstrip('PATH= ').strip()}/{sub_pth.strip()}"
        time = int(new_lines[0].strip("Time= ")) * 60

        while True:
            # Get the pictures names
            pics = os.listdir(pth)

            # Set the wallpaper
            i = randint(0, (len(pics) - 1))
            picture = f"{pth}/{pics[i]}"
            os.system(f"feh --bg-fill {picture}")

            # Time until the new wallpaper
            sleep(time)


if __name__ == "__main__":
    main()
