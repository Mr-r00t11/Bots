from instabot import Bot
import getpass
from colorama import *
import time

mi_bot = Bot()

init()
for i in range(4):
    print(" ")
    
print(Fore.MAGENTA +Style.BRIGHT+ " ██████   ██████  ████████               ██ ███    ██ ███████ ████████  █████   ██████  ██████   █████  ███    ███ ")
print(Fore.BLUE + " ██   ██ ██    ██    ██                  ██ ████   ██ ██         ██    ██   ██ ██       ██   ██ ██   ██ ████  ████ ")
print(Fore.GREEN + " ██████  ██    ██    ██        █████     ██ ██ ██  ██ ███████    ██    ███████ ██   ███ ██████  ███████ ██ ████ ██ ")
print(Fore.WHITE + " ██   ██ ██    ██    ██                  ██ ██  ██ ██      ██    ██    ██   ██ ██    ██ ██   ██ ██   ██ ██  ██  ██ ")
print(Fore.GREEN + " ██████   ██████     ██                  ██ ██   ████ ███████    ██    ██   ██  ██████  ██   ██ ██   ██ ██      ██ "+Style.RESET_ALL)
time.sleep(1)
print("\n\t\t\t\t--------------- Login ---------------")
usuario_instagram = input(Fore.CYAN + Style.BRIGHT + "\n[+] Ingres tu nombre de usuario de Instagram>> ")
print(Fore.YELLOW + Style.BRIGHT + "\n[*] Nota: La contraseña no aparecerá en texto plano...\n Intruducela Correctamente")
password_instagram = getpass.getpass(Fore.GREEN + Style.BRIGHT + f"\n[+] Introduce tu contraseña de tu cuenta {[usuario_instagram]}>> "+Style.RESET_ALL)
print("\n\t\t\t--------------- Follow - Followers ---------------")
seguidor_seguidores = input ("\n[+] Ingresa nombre de usuario a seguir>> ")
time.sleep(1)
print(Fore.GREEN + Style.BRIGHT + "\n\t<<<<<<[ Siguiendo - Seguidores ]>>>>>>")

mi_bot.login(username = usuario_instagram, password = password_instagram)    
mi_bot.follow_followers(seguidor_seguidores)

input("Presiona Enter para continuar...")
