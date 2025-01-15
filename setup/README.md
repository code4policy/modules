# Setup

This folder contains instructions to get your computer set up for this course.

Order:

<!--1. Upload a profile picture to [Github](https://docs.github.com/en/free-pro-team@latest/github/setting-up-and-managing-your-github-profile/personalizing-your-profile#changing-your-profile-picture) and [Slack](https://slack.com/help/articles/115005506003-Upload-a-profile-photo) (instructions linked). Please use the same picture across platforms.-->

1. Start with [macos.md](./macos.md) or [windows.md](./windows.md) based on your operating system.
2. Next set up your shell using [shell.md](./shell.md).
3. Next set up git using [git.md](./git.md).
4. And last, set up your ssh keys using [../git/03-ssh.md](../git/03-ssh.md#setup)
5. Install python and node.
  
    macOS:
    ```
    brew install python
    brew install node
    ```

    Ubuntu/WSL:
    ```
    sudo apt-get update
    sudo apt-get install -y python3 python3-pip nodejs
    ```
follow the following steps to install packages:

# Fix `externally-managed-environment` Error

If you see this error with `pip3 install`:

```bash
error: externally-managed-environment
```

## Fix:

1. **Make the config directory:**

   ```bash
   mkdir -p ~/.config/pip
   ```

2. **Create and edit `pip.conf`:**

   ```bash
   touch ~/.config/pip/pip.conf
   subl ~/.config/pip/pip.conf
   ```

3. **Add this:**

   ```ini
   [global]
   break-system-packages = true
   ```

4. **Save the file and verify:**
   Run the following command:

   ```bash
   pip3 config list
   ```

   What you should see:

   ```
   global.break-system-packages = true
   ```

5. **Install your package:**

   ```bash
   pip3 install pandas
   ```

Done!

_By ChatGPT + Dhrumil_
