import os

def  installEssentials():
    os.system("sudo apt-get update")
    os.system("sudo apt-get upgrade")
    os.system("sudo apt-get install firefox")
    os.system("sudo apt-get install gedit")
    os.system("sudo apt-get install clamtk")
def removeUnauthorizedUsers(user):
    os.system("sudo deluser " + user)

def removeAdmin(user):
    pass

def createUsers(user):
    os.system("sudo adduser" + user)

def changeRootPass():
    pass

def disableGuestAccount():
    pass

def enableFirewall():
    os.system("sudo nfw enable")

def allowPort(port):
    pass

def denyPort(port):
    pass

def automaticUpdates():
    pass

def securityUpdates():
    pass

def updateAll():
    pass

def disableSSHRootLogin():
    os.system("sudo gedit /etc/ssh/sshd_config")


def main():
    os.system("gksudo")
    removeUnauthorizedUsers()
    removeAdmin()
    createUsers()
    changeRootPass()
    disableGuestAccount()
    enableFirewall()
    allowPort()
    denyPort()
    automaticUpdates()
    securityUpdates()
    updateAll()
    disableSSHRootLogin()

if __name__ == '__main__':
    main()