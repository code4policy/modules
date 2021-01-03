# Shell

## macOS

1. Ensure you are using `bash` instead of `zsh`. Newer macOS versions come with `zsh` as the default. We will switch it back to bash.

   - Check if you are on bash by opening the Terminal and run: `echo "$SHELL"`. If the result ends with "zsh", continue to the next step.
   - Run `brew install bash` to get the latest bash.
   - Run `sudo subl /etc/shells` file add `/usr/local/bin/bash` as the last line of the file.
   - Run `chsh -s /usr/local/bin/bash` to switch the default shell back to bash. It will prompt you for the password which you can type in and press enter.
   - Run `touch ~/.bash_profile` create the bash profile.
   - Run `subl ~/.bash_profile` to open up the bash profile in Sublime Text.

2. Paste the following snippet at the **end of the file** and save.

   ```bash
   # add colors
   alias ls='ls -G'
   export CLICOLOR=1
   export LSCOLORS=GxFxCxDxBxegedabagaced   

   # set EDITOR as sublime text
   export EDITOR="subl --wait"

   # Define a function that returns your current git branch
   parse_git_branch() {
    git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
   }

   # Display present working directory and git path in bash prompt with colors
   export PS1="\u \[\033[32m\]\w\[\033[33m\]\$(parse_git_branch)\[\033[00m\] $ "
   ```

3. Close and reopen the terminal to see the changes.

## Ubuntu/WSL
   
1. Run `subl ~/.bashrc` to open the bash profile in Sublime Text.

2. Paste the following snippet at the **end of the file** and save.

   ```bash
   # set EDITOR as sublime text
   export EDITOR="subl --wait"

   # Define a function that returns your current git branch
   parse_git_branch() {
    git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
   }

   # Display present working directory and git path in bash prompt with colors
   export PS1="\u \[\033[32m\]\w\[\033[33m\]\$(parse_git_branch)\[\033[00m\] $ "
   ```

3. Close and reopen the terminal to see the changes.


-----

_Instructions copied/modified from [../commandline/04-unix.md#-example-permanently-setting-an-environment-variable](../commandline/04-unix.md#-example-permanently-setting-an-environment-variable)._
