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
            shutil.move('luaMacros.zip', path)
    return path

def removeSlashAndDash(arrayToEdit):
    for string in arrayToEdit:
        string = string.replace('-','')
        string = string.replace('/','')
        string = string.replace(' ','')
        string = string.lower()
    return arrayToEdit

def helpAndExit():
    print(' \n')
    print('This is EldosHD´s installer script. You can use it to install his 2nd-Keyboard-Scripts, LuaMacros and Autohotkey.')
    print("The script doesn´t work right now in normal mode. Please run it in NoColor or NoDelete Mode.")
    print('To do that type the name of the script and give it the Option "-nocolor" or "-nodelete". You can also use a "/" instead of the "-".')
    print('BTW the options are not case sensetiv.')
    print('To see the options with an explanation, use "-options".\n')
    print('The script will make an entry in your registry so your terminal can display colors. However the install will delete the entry afterwards!')
    print('If you dont want it to delete the entry, run it in -NoDelete mode.')
    print('If you dont want the script to edit your registry at all, use -NoColor mode.')
    print('If you want to check the code for yourself, or learn more about the script in general, check out my GitHub repo for the script! --> https://github.com/EldosHD/myInstallers')
    print('Thank you for using this installer. Have a good day ;)')
    sys.exit()

def optionsAndExit():
    print(' \n')
    print('Please use an valid Option! The possible options are:\n')
    print('-NoColor if you dont want colors in the installer.')
    print('-NoDelete if you dont want to delete the registry entry for the colors.')
    print('You can also use a "/" instead of a "-".')
    print('The options are not case sensitiv!')
    sys.exit()


#----------------End of Functions----------------

#----------------Beginn of Program---------------
def main(options):

    noColorMode = False
    deleteMode = False
    customInstall = False

    options = removeSlashAndDash(options)

    for string in options:
        if string == 'full':
            customInstall = False
        elif string == 'custom':
            customInstall = True
        elif string == 'nocolor':
            noColorMode = True
        elif string == 'nodelete':
            deleteMode = False
        elif string == 'delete':
            deleteMode = True
        elif string == 'help':
            helpAndExit()
        elif string == 'options' or 'option':
            optionsAndExit()
        else:
            optionsAndExit()

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
        access_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r"Console",0,winreg.KEY_ALL_ACCESS | winreg.KEY_WOW64_64KEY)
        sub_key = r'supertest'
        winreg.SetValueEx(access_key, sub_key,0,winreg.REG_DWORD,1041)            



    print(bcolors.BOLD + 'Welcome to this installer Script for Valis scripts. I will guide you through all of this. \n' +bcolors.ENDC)

    print(bcolors.WARNING + 'NOTE: If you want to install my Scripts or Install LuaMacros in the Program Files or Program Files (86x) Folder, you should run this Script as administrator \n' + bcolors.ENDC)

    if customInstall == True:
        allScripts = input('Do you want to install all of Valis scripts? (Y/N) \n')
        autoHotkey = input('Do you want to install Autohotkey? (Y/N) \n')
        luaMacros = input('Do you want to install LuaMacros? (Y/N) \n')
    else:
        allScripts = 'y'
        autoHotkey = 'y'
        luaMacros = 'y'


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
    if deleteMode==True:
        #winreg.DeleteKeyEx(access_key, sub_key)
        #print('the delete function doesn´t work right now')  #You shouldn´t see this LOL ;)
        pass


    time.sleep(3)

    if autoHotkey.lower() == 'y':
        os.system("AutoHotkeyInstaller.exe")


if __name__ == "__main__":
    if len(sys.argv) >=2:
        options = sys.argv      #so verändern, dass noColorsNoDelete ein array ist und options heisst
    elif len(sys.argv) == 1:
        print('Please start the script with an argument from the command line. Type "SCRIPTNAME -help" for help!')
        input("Press any key to exit!")
        sys.exit()
    else:
        optionsAndExit()
    options.pop(0)
    main(options)


