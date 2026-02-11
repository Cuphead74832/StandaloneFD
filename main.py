import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import os
import atexit

# =========================
# CONFIG
# =========================
GAME_NAME = "GAME_NAME_HERE"
AUTHOR_NAME = "YOURNAME"
WINDOW_TITLE = "StandaloneBlox"
EXECUTABLE = "RFD-windows-latest.exe"

# Store child processes
child_processes = []

# =========================
# Process Handling
# =========================

def executable_path():
    """Return correct path whether running normally or via PyInstaller"""
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, EXECUTABLE)
    return EXECUTABLE

def start_process(args):
    try:
        proc = subprocess.Popen(
            args,
            creationflags=subprocess.CREATE_NEW_PROCESS_GROUP
        )
        child_processes.append(proc)
    except FileNotFoundError:
        messagebox.showerror("Error", f"{EXECUTABLE} not found.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to start process:\n{e}")

def kill_rfd_only():
    """Kill only RFD-windows-latest.exe"""
    try:
        subprocess.call(
            ["taskkill", "/F", "/IM", EXECUTABLE],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
    except:
        pass

def cleanup():
    # Terminate tracked processes
    for proc in child_processes:
        try:
            proc.terminate()
        except:
            pass

    # Force kill related processes
    kill_list = [
        "RCCService.exe",
        "RFD-windows-latest.exe",
        "RobloxPlayerBeta.exe"
    ]

    for process_name in kill_list:
        try:
            subprocess.call(
                ["taskkill", "/F", "/IM", process_name],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
        except:
            pass

atexit.register(cleanup)

# =========================
# Button Commands
# =========================

def get_playername():
    name = username_entry.get().strip()
    if not name:
        messagebox.showwarning("Input Required", "Please enter a username.")
        return None
    return name

def start_server_client():
    player = get_playername()
    if not player:
        return

    cmd = [
        executable_path(),
        "server",
        "--run_client",
        "--user_code", player,
        "--config", "GameConfig.toml"
    ]
    start_process(cmd)

def start_server():
    player = get_playername()
    if not player:
        return

    cmd = [
        executable_path(),
        "server",
        "--user_code", player,
        "--config", "GameConfig.toml"
    ]
    start_process(cmd)

def start_client():
    player = get_playername()
    if not player:
        return

    cmd = [
        executable_path(),
        "player",
        "-h", "localhost",
        "-p", "2005",
        "--user_code", player
    ]
    start_process(cmd)

# =========================
# GUI Setup
# =========================

root = tk.Tk()
root.title(WINDOW_TITLE)
root.geometry("600x320")
root.resizable(False, False)

# Title
title_label = tk.Label(root, text=GAME_NAME, font=("Arial", 18, "bold"))
title_label.pack(pady=(20, 5))

author_label = tk.Label(root, text=f"Game by {AUTHOR_NAME}", font=("Arial", 12))
author_label.pack(pady=(0, 20))

# Username Entry
username_label = tk.Label(root, text="Username:")
username_label.pack()

username_entry = tk.Entry(root, width=30)
username_entry.pack(pady=10)

# Buttons Frame
button_frame = tk.Frame(root)
button_frame.pack(side="bottom", pady=30)

btn1 = tk.Button(button_frame, text="Start Server+Client", width=20, command=start_server_client)
btn1.grid(row=0, column=0, padx=5, pady=5)

btn2 = tk.Button(button_frame, text="Start Server", width=20, command=start_server)
btn2.grid(row=0, column=1, padx=5, pady=5)

btn3 = tk.Button(button_frame, text="Start Client", width=20, command=start_client)
btn3.grid(row=0, column=2, padx=5, pady=5)

# NEW BUTTON
btn4 = tk.Button(button_frame, text="Kill Server", width=20, command=kill_rfd_only, bg="#aa3333", fg="white")
btn4.grid(row=1, column=1, pady=10)

# Proper shutdown
def on_close():
    cleanup()
    root.destroy()
    sys.exit(0)

root.protocol("WM_DELETE_WINDOW", on_close)

root.mainloop()
