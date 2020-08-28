import requests
import shutil
import os ,sys
import zipfile
import getpass
import winshell
import time
import winreg
#----------------My Own Librarys-----------------
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#-------------------Variables--------------------
standardPathForLuaMacros = 'C:/Program Files (x86)/'

#-------------------Functions--------------------

def downloadFile(url, nameFile):
    r = requests.get(url)

    with open(nameFile , 'wb') as f:                    #öffnet ein neues file namens unzip_test.bat in write bytes (wb) modus im filemanegaer (f)
        f.write(r.content)
    print(bcolors.OKBLUE + '--Finished Download--\n' + bcolors.ENDC)
        
def unZipFiles(fileToUnzip, directoryToUnzipTo):
    print('--Unpacking Zip File--')
    with zipfile.ZipFile(fileToUnzip, 'r') as zipFileToExtract:
        zipFileToExtract.extractall(directoryToUnzipTo)
    print(bcolors.OKBLUE + '--Finished Unpacking--\n' + bcolors.ENDC)  

def getPathAndMove():
    print('Where do you want to install it? (If no path is specefied it will be installed in C:\Program Files (x86))\n')
    path = input('NOTE THAT THE PATH HAS TO BE WRITTEN LIKE THIS C:/Folder/Folder/Folder/  <--- Dont forget the last slash\n')
    if path == '':
        path = standardPathForLuaMacros
    elif path.find('/', len(path)-2) == -1:
        path = path + '/'

    
    if os.path.exists(path):
        print('--Moving luaMacros.zip to ' + path + '--')
        if os.path.exists(path + 'luaMacros.zip'):
            return path
        else:
            shutil.move('luaMacros.zip', path)
    else:
        print(bcolors.FAIL + 'you specified an invalid Path!' + bcolors.ENDC)
        tryAgain = input('Do you want to specify another path? (NOTE if you dont specify a path it will be installed to C:/Program Files (x86)/) (Y/N)')
        if tryAgain.lower() == 'y':
            path = getPathAndMove()
        else:
            path = standardPathForLuaMacros
    return path

def removeSlashAndDash(stringToEdit):
    returnString = stringToEdit.replace('-','')
    returnString = returnString.replace('/','')
    returnString = returnString.replace(' ','')
    return returnString

def printPossibleOptionsAndExit():
    print(' \n')
    print('Please use an valid Option! The possible options are:\n \n-NoColor if you dont want colors in the installer\n-NoDelete if you dont want to delete the registry entry for the colors\nYou can also use a / instead of a -\nThe options are not case sensitiv!')
    exit()
#----------------End of Functions----------------




#----------------Beginn of Program---------------
def main(noColorsNoDelete):

    noColorMode = False
    noDeleteMode = False

    if noColorsNoDelete == None:
        print("The delete function doesn´t work right now. Please run the script in No Delete mode!")
        exit()
    elif removeSlashAndDash(noColorsNoDelete).lower() == 'nocolor':
        noColorMode = True
    elif removeSlashAndDash(noColorsNoDelete).lower() == 'nodelete':
        noDeleteMode = False
    else:
        printPossibleOptionsAndExit()

    #------------------Registry Edit-----------------
    if noColorMode ==True:
        bcolors.HEADER = ''
        bcolors.OKBLUE = ''
        bcolors.OKGREEN = ''
        bcolors.WARNING = ''
        bcolors.FAIL = ''
        bcolors.ENDC = ''
        bcolors.BOLD = ''
        bcolors.UNDERLINE = ''
    else:
        access_registry = winreg.ConnectRegistry(None,winreg.HKEY_CURRENT_USER)
        access_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r"Console",0,winreg.KEY_WRITE | winreg.KEY_WOW64_64KEY)
        sub_key = r'VirtualTerminalLevel'
        winreg.SetValueEx(access_key, sub_key,0,winreg.REG_DWORD,1041)            



    print(bcolors.BOLD + 'Welcome to this installer Script for Valis scripts. I will guide you through all of this. \n' +bcolors.ENDC)

    print(bcolors.WARNING + 'NOTE: If you want to install my Scripts, you should run this Script as administrator \n' + bcolors.ENDC)

    allScripts = input('Do you want to install all of Valis scripts? (Y/N) \n')
    autoHotkey = input('Do you want to install Autohotkey? (Y/N) \n')
    luaMacros = input('Do you want to install LuaMacros? (Y/N) \n')



#--------------Start of Installing---------------

    if allScripts.lower() == 'y':
        print('--Downloading GitHub Repo--' + '')
        downloadFile('https://github.com/EldosHD/2nd-Keyboard/archive/master.zip', 'master.zip')
        print('--Moving master.zip to C:--')
        shutil.move('master.zip', "C:/")
        print(bcolors.OKBLUE + '--Finished Moving--\n'+ bcolors.ENDC)
        unZipFiles('C:/master.zip', 'C:/AHK')
        print('--Installing Scripts--')
        os.rename('C:/AHK/2nd-Keyboard-master', 'C:/AHK/2nd-keyboard' )
        os.rename('C:/AHK/2nd-keyboard/2nd-Keyboard-Scripts','C:/AHK/2nd-keyboard/LUAMACROS')
        os.remove('C:/AHK/2nd-keyboard/LUAMACROS/.gitattributes')
        os.remove('C:/AHK/2nd-keyboard/README.md')
        os.remove('C:/master.zip')
        print(bcolors.OKBLUE +'--Finished Installing Scripts--\n' + bcolors.ENDC)
        print(bcolors.WARNING + 'NOTE: YOU SHOULD CREATE A SHORTCUT FOR YOUR STARTUP FOLDER!!!\n' + bcolors.ENDC)


    if autoHotkey.lower() == 'y':
        print('--Downloading Autohotkey--')
        downloadFile('https://www.autohotkey.com/download/ahk-install.exe', 'AutoHotkeyInstaller.exe')
        print(bcolors.WARNING + 'The AHK installer will run once this application finishes\n' + bcolors.ENDC)


    if luaMacros.lower() == 'y':
        print('--Downloading LuaMacros--')
        downloadFile('http://www.hidmacros.eu/luamacros.zip', 'luaMacros.zip')
        path = getPathAndMove()

        print(bcolors.OKBLUE + '--Finished Moving--\n' + bcolors.ENDC)

        unZipFiles(path + 'luaMacros.zip', path + 'luaMacros')
        os.remove(path + 'luaMacros.zip')









    print(bcolors.OKGREEN + 'Thank you for using this installer the programm will exit in 3 seconds' + bcolors.ENDC)

#---------------End of Installing----------------
    if noDeleteMode!=False:
        #winreg.DeleteKeyEx(access_key, sub_key)
        print('the delete function doesn´t work right now')



    time.sleep(3)

    if autoHotkey.lower() == 'y':
        os.system("AutoHotkeyInstaller.exe")


if __name__ == "__main__":
    if len(sys.argv) ==2:
        noColorsNoDelete = sys.argv[1]
    elif len(sys.argv) == 1:
        noColorsNoDelete = None
    else:
        printPossibleOptionsAndExit()
    main(noColorsNoDelete)


