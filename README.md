# Wallpapers
## Description
A script to change the wallpaper automatically after a sleep time.  

### CLI Arguments
**--set** set the config

**-time** set the sleep time until change the wallpaper

**-path** set the path to the wallpapers directory

### Usage
* In the first run the script create a wallpapers.config with the default *time=60*  or 1 hour and *path=~/wallpapers*, since this path probably doesn't exist   in your device, is necesary set the path before the firs run
* You can set the time and path manually in the wallpapers.conf, remember the time is set in minutes

#### To set the config you can use the commands as follows
#### Set the path
     --set -time *time in minutes*
#### Set the sleep time
    --set -path *path to wallpapers directory*
