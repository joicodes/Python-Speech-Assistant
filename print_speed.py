import sys
from time import sleep

# Prints char by char to simulate typing
def print_slow(txt):
    for c in txt:
        sleep(0.03)
        sys.stdout.write(c)
        sys.stdout.flush()
