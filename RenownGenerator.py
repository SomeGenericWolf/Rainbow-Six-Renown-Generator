# Made by SomeGenericWolf uwu
import os
import sys
import time
import shutil
import pyautogui
import subprocess
import configparser
from uuid import UUID

print("Rainbow Six Siege - Automatic Renown Generator\n")
time.sleep(1.5)
user_profile = os.environ['USERPROFILE']
ext_dir_folder = f"{user_profile}\\Documents\\My Games\\Rainbow Six - Siege"
game_uuid = None
r6s_launcher = None
fd = "Files\\"
for element in os.listdir(ext_dir_folder):
    try:
        UUID(element)
        game_uuid = UUID(element)
    except ValueError:
        continue
if not game_uuid:
    print(f"Error. UUID not found.")
    time.sleep(2)
    exit(0)


def search_for_path(gpath):
    global r6s_launcher
    if os.path.exists(f"C:{gpath}"):
        r6s_launcher = f"C:{gpath}\\RainbowSix.exe"
    elif os.path.exists(f"D:{gpath}"):
        r6s_launcher = f"D:{gpath}\\RainbowSix.exe"


dir_folder = f"{user_profile}\\Documents\\My Games\\Rainbow Six - Siege\\{game_uuid}"
search_for_path("\\Program Files (x86)\\Steam\\steamapps\\common\\Tom Clancy's Rainbow Six Siege")
search_for_path("\\Steam\\steamapps\\common\\Tom Clancy's Rainbow Six Siege")
search_for_path("\\Program Files (x86)\\Ubisoft\\Ubisoft Game Launcher\\games\\Tom Clancy's Rainbow Six Siege")
search_for_path("\\Games\\Tom Clancy's Rainbow Six Siege")
if r6s_launcher is None:
    try:
        r6s_launcher = open(f"{fd}R6S_Path.txt").read().strip()
    except IOError:
        print(f"Enter the path of the folder where \"Rainbow Six\" is installed.\n")
        print("Example: \"C:\\Program Files (x86)\\Steam\\steamapps\\common\\Tom Clancy's Rainbow Six Siege\"")
        r6s_launcher = input("\nEnter the path: ")
        r6s_launcher = r6s_launcher.replace('\"', '')
        print(f"\nLooking for \"RainbowSix.exe\" in: \"{r6s_launcher}\"")
        if os.path.isfile(f"{r6s_launcher}\\RainbowSix.exe"):
            print("\"RainbowSix.exe\" found.")
            r6s_launcher = f"{r6s_launcher}\\RainbowSix.exe"
            try:
                with open(f"{fd}R6S_Path.txt", 'w') as f:
                    f.write(r6s_launcher)
            except IOError:
                print("Couldn't create the R6S_Path.txt")
        else:
            print("\"RainbowSix.exe\" not found inside the path you provided. Exiting")
            time.sleep(3.3)
            exit(0)


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
        config.set("CUSTOM_PRESET_SETTINGS", "TextureFiltering", "0")
        config.set("DISPLAY", "FPSLimit", "30")
        config.set("AUDIO", "Volume", "0")
        print(f"New parameters written.")
        with open(f'{dir_folder}\\GameSettings.ini', 'w') as configfile:
            config.write(configfile)


def search_and_click(image_name, max_tries=200, time_sleep=0.0, timeout_restart=False):
    tries = 0
    while tries < max_tries:
        ig_element = pyautogui.locateCenterOnScreen(f"{fd}{image_name}", confidence=0.8)
        if ig_element is not None:
            time.sleep(time_sleep)
            pyautogui.mouseDown(ig_element, button='left')
            pyautogui.mouseUp(ig_element, button='left')
            return True
        else:
            tries += 1
    if timeout_restart and tries > max_tries:
        try_menu = search_and_click("menu_button.PNG", max_tries=20)
        if try_menu:
            search_and_click("th_button.PNG")
            search_and_click("lone_wolf.PNG")
            search_and_click("normal.PNG")
            renown_generator()
        else:
            starting_game()
            renown_generator()


def starting_game():
    print("\nStarting RainbowSix.exe, please wait.")
    subprocess.Popen(r6s_launcher)
    search_and_click("warning.PNG", 1000, timeout_restart=True)
    while not pyautogui.locateCenterOnScreen(f"{fd}servers_text.PNG", confidence=0.8):
        pyautogui.press("u", presses=5, interval=0.01)
        time.sleep(0.3)
    while not pyautogui.locateCenterOnScreen(f"{fd}menu_button.PNG", confidence=0.8):
        pass
    print("Starting a Terrorist Hunt match.")
    time.sleep(1)
    search_and_click("menu_button.PNG")
    search_and_click("th_button.PNG")
    search_and_click("lone_wolf.PNG")
    search_and_click("normal.PNG")


def renown_generator(retry=0, num_matches=0):
    if retry is 0:
        print("\nRenown Generator Started. - (To stop, press \"Esc\" while in-game.)")
    matches = num_matches
    menu_bts = pyautogui.locateCenterOnScreen(f"{fd}menu_button.PNG", confidence=0.8)
    safe = True
    while not menu_bt:
        match_end = False
        search_and_click("res.PNG", 250, timeout_restart=True)
        search_and_click("rook.PNG")
        search_and_click("confirm.PNG")
        while not match_end:
            failure_text = pyautogui.locateCenterOnScreen(f"{fd}failure.PNG", confidence=0.8)
            quit_to_desk = pyautogui.locateCenterOnScreen(f"{fd}quit.PNG", confidence=0.8)
            menu_bts = pyautogui.locateCenterOnScreen(f"{fd}menu_button.PNG", confidence=0.8)
            if quit_to_desk:
                print(f"Closing Program, {matches} Matches Played.")
                search_and_click("quit.PNG")
                search_and_click("confirm_quit.PNG")
                menu_bts = True
                match_end = True
                safe = False
            if failure_text:
                matches += 1
                match_end = True
                search_and_click("close.PNG", time_sleep=0.5, timeout_restart=True)
                search_and_click("bonus.PNG")
                search_and_click("votefor.PNG", timeout_restart=True)
            if menu_bts:
                match_end = True
                menu_bts = True
    if safe:
        time.sleep(2)
        search_and_click("menu_button.PNG", timeout_restart=True)
        search_and_click("th_button.PNG")
        search_and_click("lone_wolf.PNG")
        search_and_click("normal.PNG")
        renown_generator(1, num_matches=matches)


def restoring_config():
    try:
        open(f"{dir_folder}\\GameSettings.bk")
        print("\nRestoring previous configuration...")
        time.sleep(5)
        os.remove(dir_folder + r"\GameSettings.ini")
        time.sleep(2)
        shutil.move(dir_folder + r"\GameSettings.bk", dir_folder + r"\GameSettings.ini")
        print("Configuration restored.")
        print("\nThank you for using this script!\nMade by SomeGenericWolf.")
        time.sleep(4)
        exit(0)
    except IOError:
        print(f"\nBackup not found, check the {dir_folder} folder.\nExiting program.")
        time.sleep(4)
        exit(0)


try:
    setting_config()
    starting_game()
    renown_generator()
    restoring_config()
except KeyboardInterrupt:
    print("You pressed CTRL+C.")
    restoring_config()
    sys.exit(0)
