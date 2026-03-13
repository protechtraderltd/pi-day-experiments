# pi_morse.py — Blink Pi digits in Morse Code
# Pi Day TikTok Livestream — ProTechTrader Make: Radio Kit Demo
# Upload to Pico #1, run with Thonny

from machine import Pin
from time import sleep

led = Pin(15, Pin.OUT)  # GP15

# Morse code timing (seconds)
DOT = 0.15        # Short flash
DASH = 0.45       # Long flash (3x dot)
SYMBOL_GAP = 0.15 # Gap between dots/dashes
CHAR_GAP = 0.45   # Gap between digits
WORD_GAP = 1.0    # Gap between repetitions

# Morse code for digits 0-9 + decimal point
MORSE = {
    '0': '-----',   # 5 dashes
    '1': '.----',   # 1 dot, 4 dashes
    '2': '..---',   # 2 dots, 3 dashes
    '3': '...--',   # 3 dots, 2 dashes
    '4': '....-',   # 4 dots, 1 dash
    '5': '.....',   # 5 dots
    '6': '-....',   # 1 dash, 4 dots
    '7': '--...',   # 2 dashes, 3 dots
    '8': '---..',   # 3 dashes, 2 dots
    '9': '----.',   # 4 dashes, 1 dot
    '.': '.-.-.-',  # Decimal point
}

PI_DIGITS = "3.14159265358979323846"

def blink_morse(char):
    """Blink one character in Morse code"""
    pattern = MORSE.get(char, '')
    for i, symbol in enumerate(pattern):
        led.on()
        if symbol == '.':
            sleep(DOT)
        else:
            sleep(DASH)
        led.off()
        if i < len(pattern) - 1:
            sleep(SYMBOL_GAP)

def main():
    print("=== Pi Day Morse Code ===")
    print(f"Blinking: {PI_DIGITS}")
    print("Dot = short flash, Dash = long flash")
    print("Watch the LED on GP15!")
    print()
    
    while True:
        for char in PI_DIGITS:
            morse = MORSE.get(char, '?')
            print(f"  {char}  {morse}")
            blink_morse(char)
            sleep(CHAR_GAP)
        
        print("\n--- Looping ---\n")
        sleep(WORD_GAP)

main()
