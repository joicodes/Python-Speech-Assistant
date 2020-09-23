from colorama import init, Fore, Style

# Initialize Colorama with Auto-reset on
init(autoreset=True)

# Prints colored text to terminal in the following colors:

# Red 
def print_red(txt):
  print(Fore.RED + txt)

# Green
def print_green(txt):
  print(Fore.GREEN + txt)

# Yellow
def print_yellow(txt):
  print(Fore.YELLOW + txt)

# Blue
def print_blue(txt):
  print(Fore.BLUE + txt)

# Magenta
def print_magenta(txt):
  print(Fore.MAGENTA + txt)

# Cyan
def print_cyan(txt):
  print(Fore.CYAN + txt)

# Black
def print_black(txt):
  print(Fore.BLACK + txt)

# White
def print_white(txt):
  print(Fore.WHITE + txt)   

# Default
def print_default(txt):
  print(Fore.RESET + txt)
  
# Dimmed Default
def print_dim(txt):
  print(Style.DIM + txt)
