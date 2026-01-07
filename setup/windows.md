# Windows Setup

1. Install the 64-bit version of [Sublime Text 3](https://www.sublimetext.com/3).
   2.  Open the app and disable Hot Exit by clicking on Preferences, then Settings. This will open the settings file in tow editor panes (sorry, the double panes are a bit confusing).
   3.  In the right-hand editor pane, enter "hot-exit": "disabled" inside the curly braces (see screenshot below). Type `ctrl-s` to save the settings file.
     <img width="1123" height="283" alt="image" src="https://github.com/user-attachments/assets/fd0efe2d-5a96-46e7-a450-6ec29f49f5c3" />
3. Now lets install the Windows Subsytem for Linux. We're essentially going to be setting up our computers to run a little Linux machine on your Windows computer. Most programming tools work much more cleanly on Linux and Mac operating systems than Windows, so this'll help us a lot with developme. Should the instructions below not work, check [this](https://docs.microsoft.com/en-us/windows/wsl/install-win10#manual-installation-steps) page for updated instructions.
   1. Open the start menu. Type "PowerShell", then right click the "Windows PowerShell" application search result and click "Run as administrator". PowerShell is a [shell](https://en.wikipedia.org/wiki/Shell_(computing)) program designed for Windows computers.
   2. Once a PowerShell window opens, type `wsl --install` into the dialog prompt. Hit enter. PowerShell may freeze up for a minute or two. You'll know it's done when you see a fresh line in the console that starts with something like `PS C:\Windows\system32`.
   3. You'll also see some text telling you to restart your computer. Go ahead and do that.
   4. Now that we've installed `wsl`, we need to install the distribution of Linux it'll run. 
         1. Re-open PowerShell
         2. Type `wsl.exe --install Ubuntu` and hit enter. This will install the Ubuntu distribution of Linux. It may take a while, but you'll know you're done when you see that fresh `PS C:\Windows...` line
4. Set up Ubuntu
   1. Let's check that we properly set up WSL with the Ubuntu. From the powershell, type `WSL` and hit enter. You'll be proimpted to set up a username and password. Go ahead and do that. Note that you won't be able to see your password as you type it out!
5. Set up Windows Terminal
   1. Check whether Windows Terminal is installed on your computer by opening the start menu and typing "terminal". If an application result shows up, you're good! Click it. Otherwise, Install [Windows Terminal](https://aka.ms/terminal) from the Microsoft Store. We'll use Windows Terminal to access `wsl` from now on instead of going through PowerShell. 
   2. Open windows terminal. Once you're in, type `ctrl-,` (i.e. press the comma key while holding down the `ctrl` key)
   3. Change the "Default profile" selection from Windows Powershell to Ubuntu (see screenshot)
      <img width="1708" height="905" alt="image" src="https://github.com/user-attachments/assets/34b12f39-749c-4968-a4fd-67fd2635f876" />   
7. Install [wsl-open](https://github.com/4U6U57/wsl-open), by copying and pasting the following code into your terminal. This will let us open Windows applications from WSL. 

   ```
   # Make a bin folder in your home directory
   mkdir ~/bin

   # Add the bin folder to your PATH in your bashrc
   echo '[[ -e ~/bin ]] && PATH=$PATH:~/bin' >> .bashrc

   # Download the script to a file named 'wsl-open'
   curl -o ~/bin/open https://raw.githubusercontent.com/4U6U57/wsl-open/master/wsl-open.sh

   # Mark file as safe to run
   chmod +x ~/bin/open
   ```

8. Install [`wsl-subl`](https://github.com/AlJohri/wsl-subl). by copying and pasting the following code into your terminal. This will launch the Sublime Text windows application when we type `subl` into WSL.  

   ```
   # Download the script to a file named 'wsl-subl'
   curl -o ~/bin/subl https://raw.githubusercontent.com/AlJohri/wsl-subl/master/wsl-subl.sh

   # Mark file as safe to run
   chmod +x ~/bin/subl

   # Append a line to the bash config file that adds the `bin` directory where the subl script lives to the  PATH variable
   echo "export PATH=$PATH:$HOME/bin" >> ~/.bashrc

   # reload the shell
   source ~/.bashrc
   ```
   

9. Go through the instructions at [shell.md](./shell.md).
