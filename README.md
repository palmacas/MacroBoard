# MacroBoard

![MacroBoard](https://i0.wp.com/palmacas.com/wp-content/uploads/post6708_4.jpeg?resize=1536%2C1152&ssl=1)

MacroBoard is a 9-key hot-swappable mechanical macropad powered by [Seeed Studio XIAO RP2040](https://www.seeedstudio.com/XIAO-RP2040-v1-0-p-5026.html). The keyboard has 9 Kailh hot-swappable sockets compatible with any 3-pin or 5-pin MX switch, giving you the ability to choose the switches that suit you best. The keyboard also includes a rotary encoder with a push button and each key is backlit with an RGB LED.

## Features

- Uses Seeed XIAO RP2040, a small form factor board based on the Raspberry Pi RP2040 microcontroller.
- Supports MicroPython and CircuitPython.
- Kailh hot-swappable sockets compatible with 3-pin and 5-pin MX switches.
- Rotary quadrature encoder with push button.
- SK6812 reverse-mounted addressable RGB LEDs to backlight each key.
- Power and communication through a USB-C type port.
- Compatible with KMK keyboard firmware.
- Compatible with Windows, macOS, and Linux operating systems.
- Dimensions: 61mm x 81mm x 31mm (without case), 66mm x 86mm x 35mm (with 3D-printed case).

## Hardware Overview

![MacroBoard](https://i0.wp.com/palmacas.com/wp-content/uploads/post6708_5.png)

## Getting Started

To set up the keyboard to work with CircuitPython and KMK Firmware, follow these steps:

### CircuitPython Installation

1. Enter Bootloader Mode
   - Press and hold the "BOOT" button.
   - Connect the Seeed XIAO RP2040 to your computer while still holding the button.
   - Your computer should now show a new drive, RPI-RP2.
2. Download the [firmware](https://circuitpython.org/board/seeeduino_xiao_rp2040/) for Seeed Studio XIAO RP2040.
3. Drag the .uf2 file to the drive RPI-RP2.
4. Check the drive. The name should now have changed to CIRCUITPY.

### NeoPixel Support 

5. Download the file [*neopixel.py*](https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel/blob/main/neopixel.py) and copy it to the root directory on drive CIRCUITPY.

### KMK Installation

6. Download the [KMK Firmware](https://github.com/KMKfw/kmk_firmware) repository as a ZIP file.
7. Extract all files from de ZIP file and copy the *kmk* folder to the root directory on drive CIRCUITPY.
8. Download the files *code.py* and *boot.py* from the [firmware](firmware) folder.
9. Copy the files to the drive CIRCUITPY.
10. Restart the keyboard by pressing the "RESET" button or disconnecting and reconnecting to the computer.

### Keyboard Configuration

The key mapping defines the function and behavior of each key using a keycode or set of keycodes. The following code, which can be found in the file *code.py*, shows the key mapping for MacroBoard.

```python
# Keymap
keyboard.keymap = [
    [KC.LCTRL(KC.LSHIFT(KC.TAB)), KC.LCTRL(KC.M), KC.LCTRL(KC.TAB),
     KC.MEDIA_PREV_TRACK, KC.MEDIA_PLAY_PAUSE, KC.MEDIA_NEXT_TRACK,
     KC.LCTRL(KC.C), KC.LCTRL(KC.V), KC.LGUI(KC.SPACE),
    ]
]
```
In this example, the keys in the first row can switch between browser tabs and mute a tab. The keys in the second row can control the media player, and the keys in the third row function as `Ctrl+C`, `Ctrl+V`, and `GUI+SPACE`.

||COLUMN 1 |COLUMN 2 | COLUMN 3|
|---|---|---|---|
|ROW 1|CTRL+SHIFT+TAB |CTRL+M |CTRL+TAB |
|ROW 2|PREV TRACK |PLAY/PAUSE |NEXT TRACK |
|ROW 3|CTRL+C |CTRL+V |GUI+SPACE|

You can find a list of all available keycodes at the [KMK Firmware's](http://kmkfw.io/docs/keycodes) wiki.

## Disclaimer

The CircuitPython firmware, KMK Firmware, and NeoPixel library are managed and maintained by their respective developers.

---
More information:  
[MacroBoard – Design and Assembly](https://palmacas.com/macroboard-design/) [[Spanish]](https://palmacas.com/macroboard-diseno/)  
[MacroBoard – Configuration](https://palmacas.com/macroboard-configuration/) [[Spanish]](https://palmacas.com/macroboard-configuracion/)
