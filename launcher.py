from tkinter import Tk, Button, Label, Toplevel
import subprocess

def show_about():
    about_window = Toplevel()
    about_window.title("About")
    Label(about_window, text="Custom Terminal\nCreated by [Your Name]").pack()

def show_version():
    version_window = Toplevel()
    version_window.title("Version")
    Label(version_window, text="Custom Terminal Version 1.0").pack()

def launch_terminal():
    subprocess.run(['xterm', '-e', 'python3', 'terminal.py'])

root = Tk()
root.title("Custom Terminal Launcher")

Button(root, text="Launch Terminal", command=launch_terminal).pack()
Button(root, text="About", command=show_about).pack()
Button(root, text="Version", command=show_version).pack()

root.mainloop()
