# Windows Setup

1. Update your computer to at least Windows 10, version 2004. (Version 1903 may work but 2004 is ideal.)

   - Use `winver` to check the current version.
   - https://en.wikipedia.org/wiki/Windows_10_version_history

2. Install [Sublime Text 3](https://www.sublimetext.com/3).
   
   - Pin Sublime Text to taskbar.
   - Disable Hot Exit by clicking on Preferences, then Settings. On the right-side pane, enter "hot-exit": "disabled" inside brackets. 

3. Install [Windows Subsystem for Linux (WSL 2)](https://docs.microsoft.com/en-us/windows/wsl/install-win10#manual-installation-steps).

4. Install [Ubuntu](https://www.microsoft.com/store/apps/9nblggh4msv6) from the Microsoft Store.

   - Setup user/pass (launch Ubuntu to do this)
   - Create shortcut to WSL home folder on desktop (if you type 'explorer.exe .' a folder should open)   

5. Install [Windows Terminal](https://aka.ms/terminal) from the Microsoft Store.

   - Pin Windows Terminal to taskbar.
   - Go to setting and change `defaultProfile` to Ubuntu
     
6. Install [wsl-open](https://github.com/4U6U57/wsl-open), by running the following in your terminal

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

7. Install [`wsl-subl`](https://github.com/AlJohri/wsl-subl).

   ```
   # Download the script to a file named 'wsl-subl'
   curl -o ~/bin/subl https://raw.githubusercontent.com/AlJohri/wsl-subl/master/wsl-subl.sh

   # Mark file as safe to run
   chmod +x ~/bin/subl
   ```

8. Go through the instructions at [shell.md](./shell.md).
