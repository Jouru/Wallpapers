# Wallpapers
## Description
A script to change the wallpaper automatically after a sleep time.

### Wallpapers themes
This script read the path folder to search all sub folders inside it, this subfolders are interpreted as themes.
To add wallpapers themes just create the folder with the name of the theme and add the images that you want to see in that them, for example if you have anime wallpapers, you can create a subfolder called Anime, then set the theme as Anime, whit this configuration the script will show only the images inaside the Anime subfolder

### Dependency
This script use feh to set the wallpaper, in order to run the script you have to install feh

### CLI Arguments
**--set** set the config

**-time** set the sleep time until change the wallpaper

**-path** set the path to the wallpapers directory

**--theme** set the wallpapers theme

### Usage
* In the first run the script create a wallpapers.config with the default *time=60*  or 1 hour and *path=~/wallpapers*, since this path probably doesn't exist   in your device, is necesary set the path before the firs run
* You can set the time and path manually in the wallpapers.conf, remember the time is set in minutes

#### To set the config you can use the commands as follows
#### Set the path
     --set -time *time in minutes*
#### Set the sleep time
    --set -path *path to wallpapers directory*
#### Set the wallpapers theme
  note: theme selection is case sensitive
  
    --theme
