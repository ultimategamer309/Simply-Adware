# Simply-Adware
Simply Adware is a simple Python Adware with cross platform persistence
# What is it
Simply Adware runs in the background on a target machine and every 5 mins will open the next link in a array then loop back through the loop. Those links are usually to ad websites in order to generate ad revenue. Simply Adware also installs itself to autorun on login on any windows, osx, or some linux machines. persistence is untested on osx and linux platforms.
# Variables to set
- ```pyCall```: The name used to call python. Generally "python", "python3", or "py" depending
- ```links```: Links is an array of strings that are links to ads. The links will be rotated through opening until the computer is turned off
- ```time```: How often the next ad will be opened (Measured in seconds)
# Persistence
### Windows
Simply Adware will create a file named startup.bat in the startup folder found at ```%AppData%/Roaming/Microsoft/Windows/Start Menu/Programs/Startup```. That batch file simply runs Simply Adware at its current location. If you move the Simply Adware file it will auto-update the batch file on the next run.
### Linux
Simply Adware will create a file named startup.sh in the startup folder found at ```/etc/profile.d```. That sh file simply runs Simply Adware at its current location. If you move the Simply Adware file it will auto-update the sh file on the next run.
### OSX
Simply Adware will create a file named startup.plist in the startup folder found at ```/Library/LaunchAgents```. That plist file simply runs Simply Adware at its current location. If you move the Simply Adware file it will auto-update the sh file on the next run.
# Dependencies
- Python3
Installation scripts for python can be found in the ```Python Installation``` folder. Those scripts will let you install python on any os by running a file named ```install.xx``` where xx changes bassed on the os.
