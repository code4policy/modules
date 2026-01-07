# Shell

> A shell? What?

Good question. A shell is a program that lets you interact with your computer by typing commands instead of clicking buttons. Developers use shells because they are fast, precise, and make it easy to automate repetitive tasks. They (can) also look quite cool.
## macOS
By default, macOS uses the `zsh` shell. Follow these steps to configure it for this class:
1. In your terminal, run `subl ~/.zshrc` to open up your zsh profile in Sublime Text. 
2. Paste the following snippet somewhere in the file. Save the file.

   ```zsh
   alias ls='ls -G'

   # colors
   export CLICOLOR=1
   export LSCOLORS=GxFxCxDxBxegedabagaced

   # editor: sublime
   export EDITOR="subl --wait"

   ## set command line prompt to display git info

   # let zsh see git info 
   autoload -Uz vcs_info
   zstyle ':vcs_info:git:*' formats ' (%b)'
   zstyle ':vcs_info:*' enable git
   
   precmd() {
     vcs_info
   }

   # set propmt
   setopt PROMPT_SUBST
   PROMPT='%n %F{green}%~%F{yellow}${vcs_info_msg_0_}%f $ '
   ```
3. Return to your terminal and type `source ~/.zshrc`. You'll notice that your shell prompt changes! How? Why? Try asking an LLM to break down the snippet above. All the changes you see in your shell result from it!

## Ubuntu/WSL

Ubuntu/WSL friends, we'll use bash as our shell. 

1. Run `subl ~/.bashrc` to open up your bash profile in Sublime Text. This is basically a settings file for your shell (really it's a script that runs when you launch the shell, but ¯\\\_(ツ)\_/¯ )
2. Paste the following snippet at the **end of the file** you opened in Sublime Text. **Make sure to save it!**

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

3. Return to your terminal and type `source ~/.bashrc`. You'll notice that your shell prompt changes! How? Why? Try asking an LLM to break down the snippet above. All the changes you see in your shell result from it!


-----

_Instructions copied/modified from [../commandline/04-unix.md#-example-permanently-setting-an-environment-variable](../commandline/04-unix.md#-example-permanently-setting-an-environment-variable)._
