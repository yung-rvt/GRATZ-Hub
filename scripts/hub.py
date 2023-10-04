#         .                  .-.    .  _   *     _   .
#                *          /   \     ((       _/ \       *    .
#              _    .   .--'\/\_ \     `      /    \  *    ___
#          *  / \_    _/ ^      \/\'__        /\/\  /\  __/   \ *
#            /    \  /    .'   _/  /  \  *' /    \/  \/ .`'\_/\   .
#       .   /\/\  /\/ :' __  ^/  ^/    `--./.'  ^  `-.\ _    _:\ _
#          /    \/  \  _/  \-' __/.' ^ _   \_   .'\   _/ \ .  __/ \
#        /\  .-   `. \/     \ / -.   _/ \ -. `_/   \ /    `._/  ^  \
#       /  `-.__ ^   / .-'.--'    . /    `--./ .-'  `-.  `-. `.  -  `.
#     @/        `.  / /      `-.   /  .-'   / .   .'   \    \  \  .-  \%
#     @&8jgs@@%% @)&@&(88&@.-_=_-=_-=_-=_-=_.8@% &@&&8(8%@%8)(8@%8 8%@)%
#     @88:::&(&8&&8:::::%&`.~-_~~-~~_~-~_~-~~=.'@(&%::::%@8&8)::&#@8::::
#     `::::::8%@@%:::::@%&8:`.=~~-.~~-.~~=..~'8::::::::&@8:::::&8:::::'
#      `::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::.'
#
#                 #################
#                 # Script by rvt #
#                 #################
#                 # ver 1.0       #
#                 #################

#▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#▓▓▓▓▓▓Imports▓▓▓▓▓
#▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
from rvts_windows_modules import hidecursor, showcursor, cmd_size, cmd_title, clear_cmd, simulate_typing
import ctypes
from ctypes import wintypes
import os
import subprocess
#▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#▓▓end of imports▓▓
#▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

def update_from_github():
    # Specify your GitHub repository URL
    repo_url = 'https://github.com/YourGitHubUsername/YourRepositoryName.git'

    # Specify the directory where your application is located
    app_directory = '/path/to/your/application'

    try:
        # Use Git to fetch the latest changes from the repository
        subprocess.check_call(['git', 'pull', repo_url], cwd=app_directory)

        print('Update completed successfully.')
    except Exception as e:
        print(f'Error updating: {e}')

if __name__ == "__main__":
    update_from_github()


user32 = ctypes.WinDLL('user32')

MB_OK = 0x00000000
MB_ICONERROR = 0x00000010
MB_ICONINFORMATION = 0x00000040
MB_ICONWARNING = 0x00000030
MB_ICONQUESTION = 0x00000020
MB_YESNO = 0x00000004

# ctypes.windll.user32.MessageBoxW(0, f"Welcome to Money Printer!", f"Money Printer V2", MB_OK)

