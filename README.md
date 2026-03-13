# Pi Day Pico Scripts

## Files
| File | Pico | What it does |
|------|------|-------------|
| `pi_morse.py` | Pico #1 | Blinks green LED with Pi digits in Morse code |
| `pi_lcd.py` | Pico #2 | Scrolls Pi digits on 1602 LCD display |
| `i2c_scan.py` | Pico #2 | Finds LCD I2C address (run before pi_lcd.py) |

## Setup
1. Flash MicroPython: hold BOOTSEL → plug USB → drag .uf2 onto RPI-RP2 drive
   Download: https://micropython.org/download/rp2-pico
2. Open Thonny IDE → select "MicroPython (Raspberry Pi Pico)" interpreter

## Experiment 1 (LED Morse)
- Wire: GP15 → 220Ω resistor → LED long leg (+) → LED short leg (-) → GND
- In Thonny: open pi_morse.py → click Run

## Experiment 2 (LCD Scroll)
- Wire: VBUS→VCC, GND→GND, GP4→SDA, GP5→SCL
- Upload lcd_api.py + pico_i2c_lcd.py to Pico first (from github.com/T-622/RPI-PICO-I2C-LCD)
- Run i2c_scan.py to verify address
- Run pi_lcd.py

- **TikTok:** [@ProTechTrader](https://www.tiktok.com/@protechtrader)
