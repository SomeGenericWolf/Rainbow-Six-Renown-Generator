# About Rainbow Six Renown Generator:
This is an image recognition based program, it finds paterns in the screen and performs actions on them, used to generate the in-game currency by playing countless Terrorist Hunt matches by itself.

# Usage:
- No need to install. It's a portable program. Just download the files and extract.
- Some In-Game settings have to be changed before running the program, please see first the "Instructions" folder.
- Once you have configured the matchmaking preferences, close the game and run the "RenownGenerator.exe".
- Press "CTRL+C" into the console to end the program. Otherwise, press "Esc" while in a match.

# Usage with Python (for debugging if needed):
You'll need the following packages (Install with PIP):
```
pyautogui
python-opencv
```
And use the main script "RenownGenerator.py".

# What does it exactly do?
Performs automatically the following actions:
  - Finds the UUID folder of the configuration file, creates a backup of it.
  - Changes the settings of the game to put it into a "low_performance" mode.
  - Opens the game and then starts a Terrorist Hunt match in Normal difficulty.
  - Gets into a loop where everytime a match ends, it restarts into the correct site and operator, generating about 30 renown per match.
  - When pressing "Esc" while in a match, it closes the game and then restores the original configuration file.
  - Pressing "CTRL+C" in the console does the same thing as above.
