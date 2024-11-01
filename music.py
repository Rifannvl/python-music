import sys
from time import sleep
import time 

def print_lyrics():
    lines = [
        ("And I Dont Know ", 0.1),
        ("What Im Cryin for", 0.2),
        ("i dont think i cloud love you more ", 0.1),
        ("it might not be long but baby i", 0.1),
        ("i'll love you ", 0.1),
        ("till the day that i die", 0.1),
        ("till the day that i dieee", 0.2),
        ("till the ligth leaves in my eyes", 0.2)
    ]

    delays = [0.1, 0.3, 0.5, 0.2, 0.6, 0.1, 0.1, 0.1, 5]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics()