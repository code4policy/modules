# Making Your Terminal ✨PrEtTy✨

Making your terminal pretty makes working on the command line much easier, especially when working with git.
The instructions below will get you set up with a terminal that always shows what folder and git branch you are
on so you never get lost.

<p align="center">
  <img src="https://i.imgur.com/g0mvFWa.gif">
</p>

1. Download [starship](https://starship.rs/), a cross-shell prompt.

    - On macOS: `brew install starship`
    - On Linux: `curl -fsSL https://starship.rs/install.sh | bash`

2. Create the starship configuration file at `~/.config/starship.toml`:

    ```bash
    mkdir ~/.config
    touch ~/.config/starship.toml
    subl ~/.config/starship.toml
    ```

3. Copy and paste the following into the blank file that just opened up in Sublime:
    
    ```toml
    [python]
    disabled = true
    
    [directory]
    truncate_to_repo = false
    truncation_length = 8
    
    [git_branch]
    symbol = ""
    
    [git_status]
    disabled = true
    
    [package]
    disabled = true
    
    [aws]
    disabled = true
    ```

4. Edit your shell profile to enable starship.

    - On macOS 10.15+ (Catalina):
    
    ```bash
    subl ~/.zshrc
    ```
    
    Add this to the end of the file:

    ```bash
    eval "$(starship init zsh)"
    ```

    - On macOS 10.14 and lower:
    
    ```
    subl ~/.bash_profile
    ```

    Add this to the end of the file:

    ```bash
    eval "$(starship init bash)"
    ```

    - On Linux:
    
    ```bash
    subl ~/.bashrc
    ```
    
    Add this to the end of the file:

    ```bash
    eval "$(starship init bash)"
    ```

5. Open a new tab in your Terminal and navigate (`cd`) to a git repository. See the pretty colors!
