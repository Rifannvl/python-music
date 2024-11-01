import sys
from time import sleep
import time 

def print_lyrics():
    lines = [
        ("She's been my queens ", 0.06),
        ("Since we were sixteen", 0.07),
        ("We want the same things ", 0.06),
        ("We dreeam the same dreams", 0.07),
        ("Alrightt", 0.1),
        ("Alright", 0.2),
        ]

    delays = [0.1, 0.3, 0.3, 0.5, 0.4, 0.5, 5]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics()