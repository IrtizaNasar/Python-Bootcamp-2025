# Anaconda Installer errors

## `The path /opt/anaconda3 already exists`

1. ```sudo rm -rf /opt/anaconda3```
1. Then try the installer again

## Installer stuck on "Running scripts"

Wait 5 minutes, it's normal for this step to take some time

# Terminal errors
## `command not found: conda`

### Mac
1. Fully quit terminal (⌘Q)
1. and reopen

or

1. Run ```source ~/.zshrc```

### Windows
1. Open Anaconda's GUI
1. Run the terminal from there with the play button

### Explanation

This means your terminal can't turn the command `conda` into a executable file to run, because the right path isn't found. Reopening the terminal or re-`source`-ing `.zshrc` reloads the relevant configuration, called `PATH`.

## `conda` commands take a long time

1. Make sure conda hasn't asked you a question that you haven't responded to; i.e. `Would you like to continue (y/n)?`
1. If it has asked the above, respond by typing `y` then `Enter`

# VSCode errors

## General Troubleshooting

Make sure you've completed the following:

1. Install [jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) and [python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) extensions for VSCode
1. Quit VSCode
1. Reopen VSCode
1. (if still not working) Toggle the Python extension Disabled and re-Enable and reopen VSCode

## VSCode's kernel dropdown asks you to install Python

Follow the steps in General Troubleshooting

# Python errors

## `FileNotFoundError`

### Mac

1. Right click on the file whose path you need
1. Hold option (⌥) and choose `Copy ______ as pathname`
1. Paste into your code where the path is needed

### Windows

1. Hold shift
1. Right click on the file whose path you need and choose `Copy as path`
1. Paste into your code where the path is needed

## `NameError`

Most likely you've typed the name of whatever variable or function you're trying to use wrong, double check for typos.
