# Simply-Adware
Simply Adware is a simple Python Adware with cross platform persistence
# What is it
Simply Adware runs in the background on a target machine and every 5 mins will open the next link in a array then loop back through the loop. Those links are usually to ad websites in order to generate ad revenue. Simply Adware also installs itself to autorun on login on any windows, osx, or some linux machines. persistence is untested on osx and linux platforms.
# Persistence
### Windows
Simply Adware will create a file named startup.bat in the startup folder found at ```%AppData%/Roaming/Microsoft/Windows/Start Menu/Programs/Startup```. That batch file simply runs Simply Adware at its current location. If you move the Simply Adware file it will auto-update the batch file on the next run.
### Linux
Simply Adware will create a file named startup.sh in the startup folder found at ```/etc/profile.d```. That sh file simply runs Simply Adware at its current location. If you move the Simply Adware file it will auto-update the sh file on the next run.
### OSX
Simply Adware will create a file named startup.plist in the startup folder found at ```/Library/LaunchAgents```. That plist file simply runs Simply Adware at its current location. If you move the Simply Adware file it will auto-update the sh file on the next run.
# Dependencies
None!
