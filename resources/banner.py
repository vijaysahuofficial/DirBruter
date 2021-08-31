import pyfiglet
from colorama import init, Fore
init()
def credits():
    print(Fore.RED + pyfiglet.figlet_format("dirBruter"))
    print("https://github.com/vijaysahuofficial/DirBruter\n\n")
    created_by = '''Vijay Sahu''' 
    banner = pyfiglet.figlet_format(created_by, font='small')
    print (Fore.GREEN + "Created By:\n", created_by + '\nhttps://www.github.com/vijaysahuofficial\n\n')