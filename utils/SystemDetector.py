import platform


class SystemInfo:
    def __init__(self):
        self.type = platform.system()
        if self.type == "Darwin":
            self.version = platform.mac_ver()[0]
            self.commandFilePath = "./data/OSX.json"
        else:
            #todo check type for windows and linux
            if self.type == "Windows":
                self.commandFilePath = "./data/Windows.json"
            if self.type == "linux":
                self.commandFilePath = "./data/Linux.json"
            self.version = platform.release()

def getSystemInfo():
    return SystemInfo()

