#!/bin/python3

from rich import print
from rich.console import Console

console = Console()

# Banner page for CORS-Clover

def banner():
    Author_identity = {
        'Author_name' :"Suraj Das",
        'Created_Date' :"23-December-2020"
        }

    print(""" 
        ╔═══╗╔═══╗╔═══╗╔═══╗     ╔═══╗╔╗
        ║╔═╗║║╔═╗║║╔═╗║║╔═╗║     ║╔═╗║║║
        ║║ ╚╝║║ ║║║╚═╝║║╚══╗     ║║ ╚╝║║ ╔══╗╔╗╔╗╔══╗╔═╗
        ║║ ╔╗║║ ║║║╔╗╔╝╚══╗║╔═══╗║║ ╔╗║║ ║╔╗║║╚╝║║╔╗║║╔╝
        ║╚═╝║║╚═╝║║║║╚╗║╚═╝║╚═══╝║╚═╝║║╚╗║╚╝║╚╗╔╝║║═╣║║
        ╚═══╝╚═══╝╚╝╚═╝╚═══╝     ╚═══╝╚═╝╚══╝ ╚╝ ╚══╝╚╝

            """)
    console.print("Use the tool for the good of infosec :heart:")
    console.log("[magenta]=============== Description ================[/magenta]", log_locals=True)
