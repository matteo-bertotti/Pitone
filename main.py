import gpiozero
import time 
import signal

# Create a variable called led and set it to an LED
led = gpiozero.LED(26)

# # Turn the LED on
# while True:
#     led.on()
#     time.sleep(1)
#     led.off()
#     time.sleep(1)
#     # signal.pause()

button = gpiozero.Button(19)

# Define a function to toggle the LED state
def toggle_led():
    if led.is_lit:
        led.off()
    else:
        led.on()

# Attach the toggle_led function to the button's pressed event
button.when_pressed = toggle_led

# Pause the script to keep it running
while True:
    time.sleep(1)
