import os
import sys
import random
import textwrap

def cd(path):
    try:
        os.chdir(path)
    except FileNotFoundError:
        print(f"No such directory: {path}")

def mkdir(directory):
    try:
        os.mkdir(directory)
    except FileExistsError:
        print(f"Directory already exists: {directory}")

def touch(file):
    with open(file, 'a'):
        os.utime(file, None)

def rm(file):
    try:
        os.remove(file)
    except FileNotFoundError:
        print(f"No such file: {file}")

def rmdir(directory):
    try:
        os.rmdir(directory)
    except FileNotFoundError:
        print(f"No such directory: {directory}")
    except OSError:
        print(f"Directory not empty: {directory}")

def pwd():
    print(os.getcwd())

def custom_command1():
    print("Welcome to the custom command 1")

def custom_command2():
    print("Here is a random number:", random.randint(1, 100))

def custom_command3():
    art = textwrap.dedent("""
    /\_/\\
   ( o.o )
    > ^ <
    """)
    print(art)

def get_colored_prompt():
    return "\033[95mcustom-shell$\033[0m "

def main():
    while True:
        try:
            command = input(get_colored_prompt()).strip().split()
            if not command:
                continue
            cmd = command[0]
            args = command[1:]

            if cmd == 'cd':
                cd(args[0] if args else os.path.expanduser('~'))
            elif cmd == 'mkdir':
                mkdir(args[0])
            elif cmd == 'touch':
                touch(args[0])
            elif cmd == 'rm':
                rm(args[0])
            elif cmd == 'rmdir':
                rmdir(args[0])
            elif cmd == 'pwd':
                pwd()
            elif cmd == 'custom1':
                custom_command1()
            elif cmd == 'custom2':
                custom_command2()
            elif cmd == 'custom3':
                custom_command3()
            elif cmd == 'exit':
                sys.exit()
            else:
                print(f"Unknown command: {cmd}")

        except KeyboardInterrupt:
            print("\nExiting custom shell...")
            break

if __name__ == "__main__":
    main()
