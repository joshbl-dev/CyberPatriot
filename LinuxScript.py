import os

def installEssentials():
    os.system("sudo apt-get update")
    os.system("sudo apt-get upgrade")
    os.system("sudo apt-get install firefox")
    os.system("sudo apt-get install gedit")
    os.system("sudo apt-get install clamtk")

def removeUnauthorizedUsers(user):
    os.system("sudo deluser " + user)

def removeAdmin(user):
    print("Remove non-admins from admin group")
    os.system("sudo gedit /etc/group")

def createUsers(user):
    os.system("sudo adduser" + user)

def changeRootPass():
    os.system("sudo passwd")
    os.system("sudo passwd -l root")

def passwordRestsrictions():
    os.system("sudo gedit /etc/pam.d/common-password")
    print("Add “remember=5” to the end of the line that has “pam_unix.so” in it.")
    print("Add “minlen=8” to the end of the line that has “pam_unix.so” in it")

    os.system("sudo gedit /etc/login.defs")
    print("PASS_MAX_DAYS 90")
    print("PASS_MIN_DAYS 10")
    print("PASS_WARN_AGE 7")

    os.system("sudo gedit /etc/pam.d/common-auth")

    print("Add to end of file: 'auth required pam_tally2.so deny=5 onerr=fail unlock_time=1800'")
def disableGuestAccount():
    os.system("sudo gedit /etc/lightdm/lightdm.conf")
    print("insert line 'allow-guest=false'")

def enableFirewall():
    os.system("sudo nfw enable")

def allowPort(port):
    print("Enter a port: ", end="")
    port = input()

def denyPort(port):
    print("Enter a port: ", end="")
    port = input()

def automaticUpdates():
    print("settings > Software & Updates > Updates > Automatically check for updates: daily")
    print("Check: Important security updates, recommended updates")

def securityUpdates():
    pass

def updateAll():
    pass

def disableSSHRootLogin():
    os.system("sudo gedit /etc/ssh/sshd_config")

def auditLogs():
    os.system("apt-get install auditd")
    os.system("sudo auditctl –e 1")
    os.system("")

def sudoers():
    print("Check users allowed to use sudo")
    os.system("sudo /etc/sudoers.d")

def findMediaFiles():
    os.system("cd /home")
    os.system("sudo locate '.mp3'")