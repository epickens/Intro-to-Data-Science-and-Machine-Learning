# WSL (Linux on Windows)

If you're using Windows, I highly recommend install WSL. WSL allows Windows users to access the power of Linux.

Although WSL is not strictly required for developers using Windows, it will ensure that this repository works as intended.

## (Recommended) Install the Windows Terminal

Install the Windows Terminal by downloading it from the Microsoft Store. The link can be found here: [Windows Terminal](https://apps.microsoft.com/detail/9n0dx20hk701?hl=en-US&gl=US)

## Installation

1. If you have already installed the `Windows Terminal`, open a new `PowerShell` tab in **administrator mode**. Otherwise, open the `PowerShell` application in admin mode.

2. Type `wsl --install` into PowerShell and press enter to install WSL. This will install Ubuntu by default.

3. Check your installation by running `wsl -l -v`

4. Type `Ubuntu` into the start menu and open the application. Once it opens up you will be asked to create an account.

5. Once your account is set up, you should be able to open a new `Ubuntu` tab in `Windows Terminal`. You may need to restart the terminal app for the option to show up.

6. In your `Ubuntu` tab, update the packages you installed by running `sudo apt update && sudo apt upgrade`

## Installing Git on WSL

1. Run `sudo apt-get install git` in an `Ubuntu` terminal

2. Set your username with `git config --global user.name "Your Name"`

3. Set your email with `git config --global user.email "youremail@domain.com"`

## Install VS Code and the WSL Extension

1. Download and install VS Code here: [Download VS Code](https://code.visualstudio.com/download)

2. When prompted to **Select Additional Tasks**, check the **Add to PATH** option to enable the `code` command in WSL

3. Install the [Remote Development extension pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack)

4. In `Ubuntu` run `sudo apt-get install wget ca-certificates` to install some additional tools

## Launching WSL for VS Code

Option 1: In an `Ubuntu` terminal run `code`. This should launch VS Code in WSL.

Option 2: In VS Code use the shortcut `CTRL+SHIFT+P` to bring up the commands interface. Type `WSL` and then launch a new `WSL` window.

## Useful Resources

- [Set up a WSL development environment](https://learn.microsoft.com/en-us/windows/wsl/setup/environment#set-up-your-linux-username-and-password)

- [Git on WSL](https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-git)

- [VS Code for WSL](https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-vscode)
