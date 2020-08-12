import os
import time
import shutil
from uuid import UUID

# You shouldn't be here, but ok, hello stranger!
user_profile = os.environ['USERPROFILE']
ext_dir_folder = f"{user_profile}\\Documents\\My Games\\Rainbow Six - Siege"
game_uuid = None
for element in os.listdir(ext_dir_folder):
    try:
        UUID(element)
        game_uuid = UUID(element)
    except ValueError:
        continue
if not game_uuid:
    exit(f"Error. UUID not found.")
dir_folder = f"{user_profile}\\Documents\\My Games\\Rainbow Six - Siege\\{game_uuid}"
confirmation = False

while not confirmation:
    print("The RenownGenerator.exe already restores your backup if you let if finish in the correct way")
    print("Only Run this script if you closed it abruptly\n")
    answer = input("Are you sure you want to run this script? (Type \"Y\" to continue, \"N\" to close): ")
    answer = answer.lower()
    if answer == "y":
        confirmation = True
        time.sleep(1)
        os.system("cls")
        print("The RenownGenerator.exe already restores your backup if you let if finish in the correct way")
        print("Only Run this script if you closed it abruptly\n")
        try:
            open(f"{dir_folder}\\GameSettings.bk")
            print("\nRestoring previous configuration...")
            time.sleep(5)
            os.remove(dir_folder + r"\GameSettings.ini")
            time.sleep(2)
            shutil.move(dir_folder + r"\GameSettings.bk", dir_folder + r"\GameSettings.ini")
            print("Configuration restored.")
            time.sleep(3)
        except IOError:
            print("Backup not found, exiting program.")
            time.sleep(3)

    elif answer == "n":
        print("Exiting program.")
        time.sleep(2)
        exit()

    else:
        print("Invalid input, try again.\n")
        time.sleep(1.5)
        os.system("cls")








