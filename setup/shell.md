# Shell

1. The first step is different for macOS vs Ubuntu/WSL:

   a. macOS
   
   Ensure you are using `bash` instead of `zsh`. Newer macOS versions come with `zsh` as the default. We will switch it back to bash.

   - Check if you are on bash by opening the Terminal and run: `echo "$SHELL"`. If the result ends with "zsh", continue to the next step.
   - Run `chsh -s /bin/bash` to switch the default shell back to bash. It will prompt you for the password which you can type in and press enter.
   - Run `touch ~/.bash_profile` create the bash profile.
   - Run `subl ~/.bash_profile` to open up the bash profile in Sublime Text.

   b. Ubuntu/WSL
   
   Run `subl ~/.bashrc` to open the bash profile in Sublime Text.

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
