"""
MacroBoard

* Cristian Palma (palmacas)
"""

import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.RGB import RGB, AnimationModes
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.encoder import EncoderHandler

# Pinout
COL1 = board.D10
COL2 = board.D9
COL3 = board.D8
ROW1 = board.D3
ROW2 = board.D4
ROW3 = board.D5
PUSHBUTTON = board.D0
ROTA = board.D2
ROTB = board.D1
NEOPIXEL = board.D7

keyboard = KMKKeyboard()

# Basic matrix settings
keyboard.col_pins = (COL1, COL2, COL3)
keyboard.row_pins = (ROW1, ROW2, ROW3)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# RGB LEDs settings
rgb_ext = RGB( 
    pixel_pin = NEOPIXEL,
    num_pixels = 9,
    hue_default = 100,
    sat_default = 255,
    val_default = 15,
    val_limit = 25,
    animation_speed = 1,
    animation_mode=AnimationModes.RAINBOW,
    refresh_rate = 30,
)
keyboard.extensions.append(rgb_ext)
keyboard.extensions.append(MediaKeys())

# Encoder settings
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
encoder_handler.pins = ((ROTA, ROTB, PUSHBUTTON, False),)
encoder_handler.map = (((KC.VOLD, KC.VOLU, KC.MUTE),),)

# Keymap
keyboard.keymap = [
    [KC.LCTRL(KC.LSHIFT(KC.TAB)), KC.LCTRL(KC.M), KC.LCTRL(KC.TAB),
     KC.MEDIA_PREV_TRACK, KC.MEDIA_PLAY_PAUSE, KC.MEDIA_NEXT_TRACK,
     KC.LCTRL(KC.C), KC.LCTRL(KC.V), KC.LGUI(KC.SPACE),
    ]
]

if __name__ == '__main__':
    keyboard.go()