from colorama import init, Fore

# Initialize Colorama with Auto-reset on
init(autoreset=True)

# Prints colored text to terminal in the following colors:

# Red 
def print_red(str):
  print(Fore.RED + str)

# Green
def print_green(str):
  print(Fore.GREEN + str)

# Yellow
def print_yellow(str):
  print(Fore.YELLOW + str)

# Blue
def print_blue(str):
  print(Fore.BLUE + str)

# Magenta
def print_magenta(str):
  print(Fore.MAGENTA + str)

# Cyan
def print_cyan(str):
  print(Fore.CYAN + str)

# Black
def print_black(str):
  print(Fore.BLACK + str)

# White
def print_white(str):
  print(Fore.WHITE + str)   

# Default
def print_default(str):
  print(Fore.RESET + str)
