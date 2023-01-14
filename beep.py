import time
import RPi.GPIO as gpio

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(12,gpio.OUT)

try:

	while True:
                gpio.output(12,0)
		time.sleep(0.1)
		gpio.output(12,1)
		time.sleep(0.1)
except KeyboardInterrupt:
		gpio.cleanup()
		exit


