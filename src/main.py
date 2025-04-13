import os
from pystyle import *
from core import *
from tools import *
import threading
import asyncio

async def menu():
    clear()

    while True:

        clear()

        banner = """
    ██████╗ ██╗   ██╗███╗   ██╗███╗   ██╗███████╗██████╗ ████████╗ ██████╗  ██████╗ ██╗     
    ██╔══██╗██║   ██║████╗  ██║████╗  ██║██╔════╝██╔══██╗╚══██╔══╝██╔═══██╗██╔═══██╗██║     
    ██████╔╝██║   ██║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝   ██║   ██║   ██║██║   ██║██║     
    ██╔══██╗██║   ██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗   ██║   ██║   ██║██║   ██║██║     
    ██║  ██║╚██████╔╝██║ ╚████║██║ ╚████║███████╗██║  ██║   ██║   ╚██████╔╝╚██████╔╝███████╗
    ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝"""

        for line in banner.splitlines():
            print(Colorate.Horizontal(Colors.green_to_white, line, 1))

        print("    v1.0\n\n")

        options = """
            
    [1] Nuke Webhook     [2] Nuke Server with Bot
    [3] Delete Webhook   [4] Get Webhook Info
    [5] Credits          [e] Exit"""

        for line in options.splitlines():
            print(Colorate.Horizontal(Colors.green_to_white, line, 1))

    

        choice = input(Colorate.Horizontal(Colors.green_to_white, "\n    Input >> "))

        if choice == "1":
            webhook = input(Colorate.Horizontal(Colors.green_to_white, "\n    Webhook URL >> "))
            nukewh(webhook)
            pause()
        elif choice == "2":
            token = input(Colorate.Horizontal(Colors.green_to_white, "\n    Bot Token >> "))
            await nukesv(token)
        elif choice == "3":
            webhook = input(Colorate.Horizontal(Colors.green_to_white, "\n    Webhook URL >> "))
            delwebhook(webhook)
        elif choice == "4":
            webhook = input(Colorate.Horizontal(Colors.green_to_white, "\n    Webhook URL >> "))
            hookinfo(webhook)
        elif choice == "5":
            print("""
    Credits:
    
    Creator: runnn3rr
    Github: github.com/runnn3rr/RunnerTool

    Press any key to continue
""")
            pause()
        elif choice == "e":
            exit()
        else:
            print(f"{Colors.red}    Error:{Colors.reset} Invalid choice. Press any key to return.")
            pause()
        

def main():
    title(" RunnerTool v1.0 ^| github.com/runnn3rr/RunnerTool ")
    asyncio.run(menu())

if __name__ == "__main__":
    main()
else:
    title("Error")
    print(f"{Colors.red}    Error:{Colors.reset} You can not import this script. Press any key to exit.")
    os.system("pause >nul && exit")