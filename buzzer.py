from gpiozero import Buzzer
from time import sleep
buzzer = Buzzer(12)
while True:
    buzzer.on()
    sleep(2)
    buzzer.off()
    sleep(1)
while True:
    buzzer.beep()

