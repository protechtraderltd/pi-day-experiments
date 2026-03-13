# pi_lcd.py — Scroll Pi digits on 1602 LCD
# Pi Day TikTok Livestream — ProTechTrader Make: Radio Kit Demo
# PREREQ: Upload lcd_api.py and pico_i2c_lcd.py to Pico first!
# Upload this to Pico #2, run with Thonny

from machine import Pin, SoftI2C
from pico_i2c_lcd import I2cLcd
from time import sleep

# --- CONFIG ---
I2C_ADDR = 0x27    # Most common. Change to 0x3F if yours is different
I2C_ROWS = 2
I2C_COLS = 16
SDA_PIN = 4        # GP4 (Pin 6)
SCL_PIN = 5        # GP5 (Pin 7)
SCROLL_SPEED = 0.3 # Seconds between scroll steps

# --- SETUP ---
i2c = SoftI2C(sda=Pin(SDA_PIN), scl=Pin(SCL_PIN), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_ROWS, I2C_COLS)

# First 100 digits of Pi
PI = ("3.14159265358979323846264338327950288419716939937510"
      "58209749445923078164062862089986280348253421170679")

def scroll_pi():
    """Scroll Pi digits across top row, static message on bottom"""
    lcd.move_to(0, 1)
    lcd.putstr("Happy Pi Day!   ")
    
    pos = 0
    while True:
        display = ""
        for i in range(I2C_COLS):
            display += PI[(pos + i) % len(PI)]
        
        lcd.move_to(0, 0)
        lcd.putstr(display)
        
        pos = (pos + 1) % len(PI)
        sleep(SCROLL_SPEED)

def main():
    print("=== Pi Day LCD Display ===")
    print(f"Scrolling {len(PI)} digits of Pi")
    print(f"I2C Address: {hex(I2C_ADDR)}")
    print(f"SDA: GP{SDA_PIN}, SCL: GP{SCL_PIN}")
    print()
    
    lcd.clear()
    
    # Splash screen
    lcd.move_to(0, 0)
    lcd.putstr("  Pi Day 2026!  ")
    lcd.move_to(0, 1)
    lcd.putstr(" ProTechTrader  ")
    sleep(3)
    
    lcd.clear()
    scroll_pi()

main()
