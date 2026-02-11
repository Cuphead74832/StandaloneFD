# StandaloneBlox
Allows you to pack a copy of RFD and placefile into an entire executable.

# NOTICE
This project DOES NOT contain roblox binaries of any kind on its repository!

# Requirements
- Python3 (latest is preferred)
- [A copy of RFD](https://github.com/Windows81/Roblox-Freedom-Distribution/releases) (THANKS VISUALPLUGIN FOR THIS AWESOME PROJECT!)
- Pyinstaller (pip install pyinstaller)
- Pillow (pip install pillow)

# Setting up
1. Download this repository and extract it into an empty folder
2. Copy RFD-windows-latest.exe and place.rbxl into the same directory (additionally, if you want a game thumbnail add a place.png)
3. Edit GameConfig.toml and main.py to your liking. (ensure theres a reference to StandaloneBlox and add me in credits if you distribute thanks)
4. Download the assets of your game. [Follow RFD README on Loading Assets](https://github.com/Windows81/Roblox-Freedom-Distribution?tab=readme-ov-file#loading-assets-from-r%C5%8Dblox) and play the game for a while, anything that the game loads (like Animations, Labels, etc...) will be saved, once done close RFD and continue this guide.
5. Test main.py: Just open it, input an username and Start Server+Client if your game opens its ready for packing.
6. Close everything including the script and open the **cmd** on the directory where your RFD and other files are! For a more clean executable, make sure theres only one version of the game present inside the Roblox Folder.
7. Type "pyinstaller build.spec" and wait. 
8. **ENJOY!** Go to the newly generated dist folder and theres your standalone executable! Just open it (it takes a while to open) and enjoy!

# Usage
Once you pack up your project you can execute and put any username and then use the self explanatory buttons to start playing!
Please ensure you credit this project if you distribute your exe!

# Thanks to all my friends for this idea.


