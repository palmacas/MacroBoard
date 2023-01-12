import supervisor
import board
import digitalio
import storage
import usb_cdc
import usb_hid
import usb_midi

supervisor.set_next_stack_limit(4096 + 4096)

# If the encoder push-button is held during boot, don't run the code which hides the storage and disables serial and midi
button = digitalio.DigitalInOut(board.D0)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

if button.value:
    storage.disable_usb_drive() # Hides device storage
    usb_cdc.disable() # Disables serial comunication
    usb_midi.disable() # Disables midi
    usb_hid.enable(boot_device=1) # Enables keyboard before OS boot
    
button.deinit()