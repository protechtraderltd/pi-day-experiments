# i2c_scan.py — Find your LCD's I2C address
# Run this FIRST before pi_lcd.py to verify wiring!
# Most LCDs are 0x27, some are 0x3F

from machine import Pin, SoftI2C

i2c = SoftI2C(sda=Pin(4), scl=Pin(5), freq=400000)
devices = i2c.scan()

print("=== I2C Scanner ===")
if devices:
    print(f"Found {len(devices)} device(s):")
    for d in devices:
        print(f"  Address: {hex(d)} ({d})")
    print()
    if 0x27 in devices:
        print("LCD at 0x27 — default, no code changes needed!")
    elif 0x3F in devices:
        print("LCD at 0x3F — change I2C_ADDR in pi_lcd.py to 0x3F")
    else:
        print("Unexpected address — update I2C_ADDR in pi_lcd.py")
else:
    print("No I2C devices found!")
    print("Check wiring:")
    print("  SDA -> GP4 (Pin 6)")
    print("  SCL -> GP5 (Pin 7)")
    print("  VCC -> VBUS (Pin 40) — must be 5V!")
    print("  GND -> GND (Pin 38)")
