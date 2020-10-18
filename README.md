# Why does this repo exist?
I dont know why you are here. But since you stumbled across my little project you might want to take a look. Here I dump my installer scripts for my other projects.
The only current project is my Makrokeyboard. I created it with the help of Luamacros and i currently use it to trigger and control my scripts for Minecraft 
and as a shortcut for certain folders and apps.
The original code was written by Taran van Hemert. I followed this Tutorial https://www.youtube.com/watch?v=Arn8ExQ2Gjg by Taran and modified his code heavily.
In case you want to check out my code, follow this link: https://github.com/EldosHD/2nd-Keyboard
If you want to try out the program itself, you should watch Tarans Tutorial first, since I wont explain how the Program itself functions. 
I will only talk about my Installer for it. You can either install his code manually, or use my installer to download and install Luamacros,
Autohotkey (that´s the language I use to create my makros) and my code.
# What does it do and how do I use it?
The program is written in Python. You should use the .exe file since you probably have to install the Python librarys otherwise. 
It uses the command line, because I think thats cooler than using a GUI. (And its less work) I will explain what the code does and how you
can customize your installation. Since Autohotkey sadly only works on windows, this Installer is Windows only too. But you can try it on Linux and send me the results LOL ;)
## Step 1
Start a cmd or powershell as administrator. The program will install stuff in your C: drive and therefore needs admin privileges.
## Step 2 
Go to the location of the installer script.
## Step 3
You can type SCRIPTNAME -full for a full installation and skip the other steps. Or you can type SCRIPTNAME -custom for a quick custom installation. **BUT** the installer will
change your registry. I wanted to use colored text and the simplest solution was using a class created by Joeld on stack overflow.
(https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-python?page=1&tab=votes#tab-top) To use this color codes I had to make a small tweak to the registry.
I added to HKEY_CURRENT_USER/Console/VirtualTerminalLevel the value 1041. (Idk why, but this makes the colors function) If you dont want to change the registry, use option -nocolor
with -custom or -full. If you want to know more type SCRIPTNAME -help.
## Step 4 (Only for custom installation)
