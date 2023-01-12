# MacroBoard

![MacroBoard](https://i0.wp.com/palmacas.com/wp-content/uploads/post6708_4.jpeg?resize=1536%2C1152&ssl=1)

MacroBoard is a 9-key hotswap mechanical macropad powered by Seeed XIAO RP2040. The keyboard features 9 Kailh hotswap sockets compatible with any 3 or 5-pin MX switch, so you can choose the switches you are more confortable with. The keyboard also features a rotary encoder with push-button, and each key is backlit with a RGB LED.

## Features

- Uses the small form factor board Seeed XIAO RP2040, based on the Raspberry Pi RP2040 microcontroller.
- Supports MicroPython and CircuitPython.
- Kailh hotswap sockets compatible with 3-pin and 5-pin MX switches.
- Rotary quadrature encoder with push-button.
- SK6812 reverse mount addresable RGB LEDs to backlit each key.
- Power and communicaction via USB-C type port.
- Compatible with KMK keyboard firmware.
- Compatible with Windows, macOS and Linux operative systems.
- Dimensions: 61mm x 81mm x 20mm (without case), 61mm x 81mm x 20mm (with case).

## Hardware Overview

![MacroBoard](https://i0.wp.com/palmacas.com/wp-content/uploads/post6708_5.png)

## Getting Started

This sample shows how to setup te keyboard to work with CircuitPython and KMK Firmware.

### CircuitPython Installation

1. Enter Bootloader Mode
   - Press and hold the "BOOT" button.
   - Connect the Seeed XIAO RP2040 to your computer while you still hold the button.
   - The computer then will show a new drive RPI-RP2.
2. Download the [firmware](https://circuitpython.org/board/seeeduino_xiao_rp2040/) for Seeed Studio XIAO RP2040.
3. Drag the .uf2 file to the drive RPI-RP2.
4. Check the drive, the name now has changed to CIRCUITPY.

### NeoPixel Support 

1. Download the file [*neopixel.py*](https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel/blob/main/neopixel.py) and copy it to the root directory in drive CIRCUITPY.

### KMK Installation

1. Download the [KMK Firmware](https://github.com/KMKfw/kmk_firmware) repository as a ZIP file.
2. Extract all the files from de ZIP file, and copy the *kmk* folder to the root directory in drive CIRCUITPY.
3. Download the files *code.py* and *boot.py* from the folder [firmware](firmware).
4. Copy the files to the drive CIRCUITPY.
5. Restart the keyboard by pressing the "RESET" button or disconnect and connect to the computer.

### Keyboard Configuration

The key mapping defines the function and behaviour of each key using a keycode or a set of keycodes. The following code can be found in the file *code.py*, showing the key mapping for the MacroBoard.

```python
# Keymap
keyboard.keymap = [
    [KC.LCTRL(KC.LSHIFT(KC.TAB)), KC.LCTRL(KC.M), KC.LCTRL(KC.TAB),
     KC.MEDIA_PREV_TRACK, KC.MEDIA_PLAY_PAUSE, KC.MEDIA_NEXT_TRACK,
     KC.LCTRL(KC.C), KC.LCTRL(KC.V), KC.LGUI(KC.SPACE),
    ]
]
```
In this example the keys in the first row can switch between browser tabs and mute a tab. The keys from the second row can control de media player. And the keys from the third row work as Ctrl+C, Ctrl+V, and GUI+SPACE.

||COLUMN 1 |COLUMN 2 | COLUMN 3|
|---|---|---|---|
|ROW 1|CTRL+SHIFT+TAB |CTRL+M |CTRL+TAB |
|ROW 2|PREV TRACK |PLAY/PAUSE |NEXT TRACK |
|ROW 3|CTRL+C |CTRL+V |GUI+SPACE|

All the available keycodes can be found at [KMK Firmware's](http://kmkfw.io/docs/keycodes) wiki.

## Disclaimer

CircuitPython firmware, KMK Firmware, and the NeoPixel library are managed and maintained by their developers.

---
More information:  
[MacroBoard – Design and Assembly](https://palmacas.com/macroboard-design/) [[Spanish]](https://palmacas.com/macroboard-diseno/)  
[MacroBoard – Configuration](https://palmacas.com/macroboard-configuration/) [[Spanish]](https://palmacas.com/macroboard-configuracion/)