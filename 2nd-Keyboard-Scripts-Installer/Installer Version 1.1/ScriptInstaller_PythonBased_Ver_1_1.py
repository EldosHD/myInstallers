import requests
import shutil
import os ,sys
import zipfile
import getpass
import winshell
import time
#----------------My Own Librarys-----------------


#-------------------Variables--------------------
standardPathForLuaMacros = 'C:/Program Files (x86)/'

#-------------------Functions--------------------

def downloadFile(url, nameFile):
    r = requests.get(url)

    with open(nameFile , 'wb') as f:                    #öffnet ein neues file namens unzip_test.bat in write bytes (wb) modus im filemanegaer (f)
        f.write(r.content)
    print('--Finished Download--\n')
        
def unZipFiles(fileToUnzip, directoryToUnzipTo):
    print('--Unpacking Zip File--')
    with zipfile.ZipFile(fileToUnzip, 'r') as zipFileToExtract:
        zipFileToExtract.extractall(directoryToUnzipTo)
    print('--Finished Unpacking--\n')  

def getPathAndMove():
    print('Where do you want to install it? (If no path is specefied it will be installed in C:\Program Files (x86))\n')
    path = input('NOTE THAT THE PATH HAS TO BE WRITTEN LIKE THIS C:/Folder/Folder/Folder ')
    if path == '':
        path = standardPathForLuaMacros

    print('--Moving luaMacros.zip to ' + path + '--')
    try:
        shutil.move('luaMacros.zip', path)
    except:
        print('you specified an invalid Path!')
        tryAgain = input('Do you want to specify another path? (NOTE if you dont specify a path it will be installed to C:/Program Files (x86)/) (Y/N)')
        if tryAgain.lower() == 'y':
            path = getPathAndMove()
        else:
            path = standardPathForLuaMacros
    return path

#----------------End of Functions----------------


#--------------------Console --------------------


print('Welcome to this installer Script for Valis scripts. I will guide you through all of this. \n')

allScripts = input('Do you want to install all of Valis scripts? (Y/N) \n')
autoHotkey = input('Do you want to install Autohotkey? (Y/N) \n')
luaMacros = input('Do you want to install LuaMacros? (Y/N) \n')



#--------------Start of Installing---------------

if allScripts.lower() == 'y':
    print('--Downloading GitHub Repo--' + '')
    downloadFile('https://github.com/EldosHD/2nd-Keyboard/archive/master.zip', 'master.zip')
    print('--Moving master.zip to C:--')
    shutil.move('master.zip', "C:/")
    print('--Finished Moving--\n')
    unZipFiles('C:/master.zip', 'C:/AHK')
    print('--Installing Scripts--')
    os.rename('C:/AHK/2nd-Keyboard-master', 'C:/AHK/2nd-keyboard' )
    os.rename('C:/AHK/2nd-keyboard/2nd-Keyboard-Scripts','C:/AHK/2nd-keyboard/LUAMACROS')
    os.remove('C:/AHK/2nd-keyboard/LUAMACROS/.gitattributes')
    os.remove('C:/AHK/2nd-keyboard/README.md')
    os.remove('C:/master.zip')
    print('--Finished Installing Scripts--\n')
    print('NOTE: YOU SHOULD CREATE A SHORTCUT FOR YOUR STARTUP FOLDER!!!\n')


if autoHotkey.lower() == 'y':
    print('--Downloading Autohotkey--')
    downloadFile('https://www.autohotkey.com/download/ahk-install.exe', 'AutoHotkeyInstaller.exe')
    print('The AHK installer will run once this application finishes\n')


if luaMacros.lower() == 'y':
    print('--Downloading LuaMacros--')
    downloadFile('http://www.hidmacros.eu/luamacros.zip', 'luaMacros.zip')
    path = getPathAndMove()

    print('--Finished Moving--\n')

    unZipFiles(path + 'luaMacros.zip', path + 'luaMacros')
    os.remove(path + 'luaMacros.zip')









print('Thank you for using this installer the programm will exit in 3 seconds')

#---------------End of Installing----------------

time.sleep(3)

if autoHotkey.lower() == 'y':
    os.system("AutoHotkeyInstaller.exe")


