# Pi Day 2026 — Raspberry Pi Pico Experiments 🥧

**Two fun electronics experiments to celebrate Pi Day (March 14th) using the Raspberry Pi Pico and MicroPython.**

Built by [ProTechTrader](https://www.protechtrader.com) — a small electronics education company from New Jersey specializing in STEM kits and components.

## 📺 TikTok LIVE Demo

**Monday, March 17 at 2:30 PM EST** — Watch us build both experiments live on TikTok!

👉 Follow [@ProTechTrader on TikTok](https://www.tiktok.com/@protechtrader) to get notified when we go live.

## 🧪 Experiments

### Experiment 1: LED Morse Code Pi
Blink the digits of Pi (3.14159...) in Morse code using a green LED. Perfect beginner project — only 2 components and 1 wire!

- **File:** [`pi_morse.py`](pi_morse.py)
- **Difficulty:** Beginner
- **Setup Time:** 2 minutes
- **Components:** Raspberry Pi Pico, green LED, 470Ω resistor

### Experiment 2: LCD Scrolling Pi Digits
Display the first 100 digits of Pi scrolling across a 1602 LCD display with an I2C backpack.

- **File:** [`pi_lcd.py`](pi_lcd.py)
- **Helper:** [`i2c_scan.py`](i2c_scan.py) — scan for I2C address
- **Difficulty:** Intermediate
- **Setup Time:** 10 minutes
- **Components:** Raspberry Pi Pico, 1602 LCD with I2C, breadboard, 4 jumper wires

**LCD Display Shows:**
- Splash screen: `Pi Day 2026!` / `@ProTechTrader`
- Scrolling mode: Pi digits on top, `Happy Pi Day from ProTechTrader.com` scrolling on bottom

## 📌 Wiring (Experiment 2)

| Pico Pin | GPIO | Wire Color | LCD Pin |
|----------|------|------------|---------|
| Pin 40 | VBUS | 🔴 Red | VCC (5V) |
| Pin 38 | GND | ⚫ Black | GND |
| Pin 6 | GP4 | 🔵 Blue | SDA |
| Pin 7 | GP5 | 🟡 Yellow | SCL |

See the [full interactive pinout diagram](https://www.protechtrader.com/pi-day/) on our website with all 40 pins labeled and highlighted connections.

## 📸 Reference Images

The [`images/`](images/) directory contains 10 AI-generated connection reference photos:
- Top-down overview of complete setup
- 3D angle showing breadboard connections  
- Close-up of Pico pin connections with jumper wires
- LCD I2C backpack detail
- Cartoon-style wiring diagram
- Lifestyle desk shot with laptop running Thonny
- Multiple alternate angles for verification

## 🎓 Complete Beginner Walkthrough

Never programmed a microcontroller before? The [full online guide](https://www.protechtrader.com/pi-day/) includes a 5-part beginner walkthrough:

1. **Part A:** Setting up your Pico — Installing [Thonny IDE](https://thonny.org), flashing MicroPython firmware
2. **Part B:** Breadboard wiring — Step-by-step with pin diagram and color-coded instructions
3. **Part C:** Uploading LCD libraries — How to save `lcd_api.py` and `pico_i2c_lcd.py` to the Pico
4. **Part D:** Testing your wiring — Run `i2c_scan.py` to verify I2C connections
5. **Part E:** Running the Pi scroller — Launch, troubleshoot contrast dial, set to auto-run on boot

## 🧰 What You Need

All components are included in the [Make: Radio Electronics Component Kit](https://www.protechtrader.com/electronic-components-kits/Electronic-Kits/Make-Radio-Electronics-Component-Kit) from ProTechTrader:

- 2x Raspberry Pi Pico + USB cables
- 1602 LCD Display with I2C backpack
- Breadboards
- Jumper wires (male-to-female)
- LEDs, resistors, and more

You can also purchase just the components you need from our [Electronics Components & Kits](https://www.protechtrader.com/electronic-components-kits) catalog.

## 📥 Prerequisites

The LCD experiment requires two helper libraries uploaded to your Pico first:
- [`lcd_api.py`](https://github.com/T-622/RPI-PICO-I2C-LCD) by T-622
- [`pico_i2c_lcd.py`](https://github.com/T-622/RPI-PICO-I2C-LCD) by T-622

## 🔗 Links

| Resource | URL |
|----------|-----|
| **Full Interactive Guide** | [protechtrader.com/pi-day/](https://www.protechtrader.com/pi-day/) |
| **Buy the Digital Guide** | [Product Page ($9.99)](https://www.protechtrader.com/index.php?route=product/product&product_id=7570) |
| **Make: Radio Kit** | [All Components Included](https://www.protechtrader.com/electronic-components-kits/Electronic-Kits/Make-Radio-Electronics-Component-Kit) |
| **All Electronics Kits** | [Browse Catalog](https://www.protechtrader.com/electronic-components-kits) |
| **TikTok LIVE Demo** | [@ProTechTrader — Mar 17 @ 2:30 PM](https://www.tiktok.com/@protechtrader) |
| **ProTechTrader Home** | [protechtrader.com](https://www.protechtrader.com) |

## 📄 License

MIT License — free to use, modify, and share. If you build something cool with it, tag us on TikTok [@ProTechTrader](https://www.tiktok.com/@protechtrader)!

---

**Made with ❤️ by [ProTechTrader](https://www.protechtrader.com)** — Electronics kits, components & STEM education from New Jersey.

Happy Pi Day! 🥧🎉
