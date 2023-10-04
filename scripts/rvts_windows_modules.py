import os
import time

def get_current_user():
    return os.getenv("USERNAME")

def cmd_size(columns, lines):
    command1 = f"mode con cols={columns} lines={lines}"
    os.system(command1)
    
def clear_cmd():
    command2 = f"cls"
    os.system(command2)
    
def simulate_typing(text, delay):
    for char in text:
        print(char, end='', flush=True) 
        time.sleep(delay)
        
def cmd_title(new_title):
    title_text = new_title.replace("|", "^|")
    command3 = "title " + title_text
    os.system(command3)
    
def hidecursor():
    os.system("<nul set /p=[?25l")

def showcursor():
    os.system("<nul set /p=[?25h")
    
if __name__ == "__main__":
    print()
    print("────────────────────────────────────────────")
    print(" [-] This is a Module, not a Script to run.")
    print("────────────────────────────────────────────")
    time.sleep(3)
    exit()