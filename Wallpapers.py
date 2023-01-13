import os
import argparse
from time import sleep
from random import randint


def main():
    parser = argparse.ArgumentParser(description="Wallpapers")
    parser.add_argument("--set", help="Set the default values", action="store_true")
    parser.add_argument("-time", help="Define time in minutes", type=int)
    parser.add_argument("-path", help="Define path")
    args = parser.parse_args()
    
    ## Create the config file
    if not os.path.isfile("wallpapers.conf"):
        with open("wallpapers.conf", "w") as file:
            time = "3600"
            path = "~/Wallpapers/"
            file.write(f"Time= {time}\n")
            file.write(f"PATH= {path}")
            
    if args.set:
        ## Define a new time
        if args.time:
            new_time = args.time
            with open("wallpapers.conf", "r") as file:
                lines = file.readlines()
            for l in range(len(lines)):
                if lines[l].startswith("Time="):
                    lines[l] = f"Time= {new_time}"
            
            with open("wallpapers.conf", "w") as file:
                for l in range(len(lines)):
                    file.write(f"{lines[l].strip()}\n")
        
        ## Define a new path
        if args.path:
            with open("wallpapers.conf", "r") as file:
                lines = file.readlines()
            for l in range(len(lines)):
                if lines[l].startswith("PATH="):
                    lines[l] = f"PATH= {args.path}"
            
            with open("wallpapers.conf", "w") as file:
                for l in range(len(lines)):
                    file.write(f"{lines[l].strip()}\n")
    
    else:    
        with open("wallpapers.conf", "r") as file:
            new_lines = file.readlines()         

        ## Get time and path to wallpapers directory
        pth = new_lines[1].lstrip("PATH= ").strip()
        time = int(new_lines[0].strip("Time= "))*60
     
        while True:
            ## Get the pictures names
            pics = os.listdir(pth)
            
            ## Set the wallpaper
            i = randint(0, (len(pics) - 1))
            picture = f"{pth}/{pics[i]}"
            os.system(f"feh --bg-fill {picture}")
            
            ## Time until the new wallpaper
            sleep(time)            
    
    

if __name__=="__main__":
    main()