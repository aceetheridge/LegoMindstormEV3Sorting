import RPi.GPIO as GPIO
import time

class BinaryLEDController:
    def __init__(self, led_pins):
        self.led_pins = led_pins
        self.current_value = None

        # Set up GPIO
        GPIO.setmode(GPIO.BCM)
        for pin in led_pins:
            GPIO.setup(pin, GPIO.OUT)

    def display_binary(self, value):
        # Ensure that the input is within the valid range
        if 0 <= value < 16:
            self.current_value = value
            binary_value = format(value, '04b')  # Convert to 4-bit binary string
            for i, pin in enumerate(self.led_pins):
                # Turn on or off the LED based on the binary value
                GPIO.output(pin, GPIO.HIGH if binary_value[i] == '1' else GPIO.LOW)
        else:
            print("Invalid input. Please enter a number between 0 and 15.")

    def set_current_value(self, value):
        if value != self.current_value:
            self.display_binary(value)

    def cleanup(self):
        # Turn off all LEDs
        for pin in self.led_pins:
            GPIO.output(pin, GPIO.LOW)

        # Clean up GPIO
        GPIO.cleanup()