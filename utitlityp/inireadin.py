import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\harcode.ini")

class readconfig:
    @staticmethod
    def readcon(self):
        baseurl = ""

