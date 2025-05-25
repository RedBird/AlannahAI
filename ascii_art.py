#This page is where all the cool art for the CLI is (Command Line Interface)
import pyfiglet


def show_banner():
    cat = [
        "           ▄   ▄                  ▄   ▄",
        "           █▀█▀█                  █▀█▀█",
        "           █▄█▄█                  █▄█▄█",
        "            ███  ▄▄                ███  ▄▄",
        "            ████▐█ █               ████▐█ █",
        "            ████   █               ████   █",
        "            ▀▀▀▀▀▀▀                ▀▀▀▀▀▀▀"
    ]

    for line in cat:
        print(line)

  

    banner = pyfiglet.figlet_format("AlannahAI")
    print(banner)

