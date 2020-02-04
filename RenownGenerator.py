import os
import sys
import time
import shutil
import pyautogui
import subprocess
import configparser
from uuid import UUID

# You shouldn't be here, but ok, hello stranger!
print("Rainbow Six Siege - Automatic Renown Generator\n")
time.sleep(1.5)
user_profile = os.environ['USERPROFILE']
ext_dir_folder = f"{user_profile}\\Documents\\My Games\\Rainbow Six - Siege"
game_uuid = None
fd = "Files\\"
for element in os.listdir(ext_dir_folder):
    try:
        UUID(element)
        game_uuid = UUID(element)
    except ValueError:
        continue
if game_uuid is None:
    exit(f"Error. UUID not found.")
dir_folder = f"{user_profile}\\Documents\\My Games\\Rainbow Six - Siege\\{game_uuid}"
steam_dir = "\\Program Files (x86)\\Steam\\steamapps\\common\\Tom Clancy's Rainbow Six Siege"
uplay_dir = "\\Program Files (x86)\\Ubisoft\\Ubisoft Game Launcher\\games\\Tom Clancy's Rainbow Six Siege"

if os.path.exists(f"C:{steam_dir}"):
    r6s_launcher = f"C:{steam_dir}\\RainbowSix.exe"
elif os.path.exists(f"D:{steam_dir}"):
    r6s_launcher = f"D:{steam_dir}\\RainbowSix.exe"
elif os.path.exists(f"C:{uplay_dir}"):
    r6s_launcher = f"C:{uplay_dir}\\RainbowSix.exe"
elif os.path.exists(f"D:{uplay_dir}"):
    r6s_launcher = f"D:{uplay_dir}\\RainbowSix.exe"
else:
    try:
        r6s_launcher = open("Files\\R6S_Path.txt").read().strip()
    except IOError:
        print(f"Enter the path of the folder where \"Rainbow Six\" is installed.")
        r6s_launcher = input(f"\nExample: C:{steam_dir}\nEnter the path: ")
        r6s_launcher = r6s_launcher.replace('\"', '')
        print(f"\nLooking for \"RainbowSix.exe\" in: \"{r6s_launcher}\"")
        if os.path.isfile(f"{r6s_launcher}\\RainbowSix.exe"):
            print("\"RainbowSix.exe\" found.")
            r6s_launcher = f"{r6s_launcher}\\RainbowSix.exe"
            with open("Alternative stuff\\R6S_Path.txt", 'w') as f:
                f.write(r6s_launcher)
        else:
            print("\"RainbowSix.exe\" not found inside the path you provided. Exiting")
            time.sleep(3.3)
            exit()


def setting_config():
    try:
        open(dir_folder + r"\GameSettings.bk")
        print(f"There's a backup of the Configuration already at \"{dir_folder}\".")
    except IOError:
        print(f"Creating a backup of the Configuration at \"{dir_folder}\\GameSettings.bk\"...")
        shutil.copy(f"{dir_folder}\\GameSettings.ini", f"{dir_folder}\\GameSettings.bk")
        config = configparser.ConfigParser()
        config.read(f"{dir_folder}\\GameSettings.ini")
        config.set("DISPLAY_SETTINGS", "WindowMode", "1")
        config.set("DISPLAY_SETTINGS", "ResolutionWidth", "1280")
        config.set("DISPLAY_SETTINGS", "ResolutionHeight", "720")
        config.set("DISPLAY_SETTINGS", "DefaultFOV", "60")
        config.set("DISPLAY_SETTINGS", "InitialWindowPositionX", "-1")
        config.set("DISPLAY_SETTINGS", "InitialWindowPositionY", "-1")
        config.set("QUALITY_SETTINGS", "TexturePresetName", "Low")
        config.set("CUSTOM_PRESET_SETTINGS", "Shadow", "0")
        config.set("CUSTOM_PRESET_SETTINGS", "Reflection", "0")
        config.set("CUSTOM_PRESET_SETTINGS", "LOD", "0")
        config.set("CUSTOM_PRESET_SETTINGS", "AO", "0")
        config.set("CUSTOM_PRESET_SETTINGS", "Shading", "0")
        config.set("CUSTOM_PRESET_SETTINGS", "MotionBlur", "0")
        config.set("CUSTOM_PRESET_SETTINGS", "LensEffects", "0")
        config.set("CUSTOM_PRESET_SETTINGS", "DepthOfField", "0")
        config.set("DISPLAY", "FPSLimit", "30")
        config.set("AUDIO", "Volume", "0")
        print(f"New parameters written.")
        with open(f'{dir_folder}\\GameSettings.ini', 'w') as configfile:
            config.write(configfile)


def skipping_intro():
    print("\nStarting RainbowSix.exe, please wait.")
    subprocess.Popen(r6s_launcher)
    st_presence = False
    main_menu_presence = False
    search_and_click("warning.PNG", 1000)
    while st_presence is False:
        if pyautogui.locateCenterOnScreen(f"{fd}servers_text.PNG", confidence=0.8) is None:
            pyautogui.press("u", presses=5, interval=0.01)
            time.sleep(0.3)
        else:
            st_presence = True
    while main_menu_presence is False:
        if pyautogui.locateCenterOnScreen(f"{fd}menu_button.PNG", confidence=0.8) is None:
            pass
        else:
            time.sleep(1)
            main_menu_presence = True


def search_and_click(image_name, max_tries=200):
    tries = 0
    while tries < max_tries:
        ig_element = pyautogui.locateCenterOnScreen(f"{fd}{image_name}", confidence=0.8)
        if ig_element is None:
            tries += 1
            pass
        else:
            pyautogui.mouseDown(ig_element, button='left')
            pyautogui.mouseUp(ig_element, button='left')
            return True


def starting_game():
    print("Starting a Terrorist Hunt match.")
    search_and_click("menu_button.PNG")
    search_and_click("th_button.PNG")
    search_and_click("lone_wolf.PNG")
    search_and_click("normal.PNG")


def renown_generator():
    print("\nRenown Generator Started. - (To stop, press \"Esc\" while in-game. or CTRL+C)")
    matches = 0
    stop = False
    while stop is False:
        match_end = False
        search_and_click("res.PNG", 300)
        search_and_click("rook.PNG")
        search_and_click("confirm.PNG")
        while match_end is False:
            failure_text = pyautogui.locateCenterOnScreen(f"{fd}failure.PNG", confidence=0.8)
            quit_to_desk = pyautogui.locateCenterOnScreen(f"{fd}quit.PNG", confidence=0.8)
            if quit_to_desk is None:
                pass
            else:
                print(f"Closing Program, {matches} Matches Played.")
                search_and_click("quit.PNG")
                search_and_click("confirm_quit.PNG")
                stop = True
                match_end = True
            if failure_text is None:
                continue
            else:
                matches += 1
                match_end = True
                search_and_click("close.PNG")
                search_and_click("bonus.PNG")
                search_and_click("votefor.PNG")


def restoring_config():
    try:
        open(f"{dir_folder}\\GameSettings.bk")
        print("\nRestoring previous configuration...")
        time.sleep(5)
        os.remove(dir_folder + r"\GameSettings.ini")
        time.sleep(2)
        shutil.move(dir_folder + r"\GameSettings.bk", dir_folder + r"\GameSettings.ini")
        print("Configuration restored.")
        print("\nThank you for using this script!\nMade by Mia.")
        time.sleep(4)
        exit()
    except IOError:
        print(f"Backup not found, check the {dir_folder} folder.\nExiting program.")
        time.sleep(4)
        exit()


try:
    setting_config()
    skipping_intro()
    starting_game()
    renown_generator()
    restoring_config()
except KeyboardInterrupt:
    print("You pressed CTRL+C.")
    restoring_config()
    sys.exit(0)
