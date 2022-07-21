import os
import time
from random import randint

def main():
    pth = "~/Wallpapers" ## Change for the path of your wallpapers directory
    pics = os.listdir(path)

    while True:
        i = randint(0,len(pics))
        picture = f"{pth}/{pics[i]}"
        os.system(f"feh --bg-fill {picture}")
        time.sleep(900) ## Time is given in seconds

if __name__=="__main__":
    main()
