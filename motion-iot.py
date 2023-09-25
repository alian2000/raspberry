# this code will detect motion using PIR sensor on pin 18 anf then set other GPIO's to 1 such as LED, Buzzer and relay
# i connected the relay to a car motor operated by battery and worked well.
import RPi.GPIO as io
import time
io.setmode(io.BCM)
io.setmode(io.BCM)

pir_sensor = 18
piezo = 24
st17=22
bLed=27
relay=21
io.setup(relay,io.OUT)
io.setup(piezo,io.OUT)
io.setup(st17,io.OUT)
io.setup(bLed,io.OUT)
io.setup(pir_sensor,io.IN)
current_state = 0
io.output(st17,current_state)
try:
     while True:
        time.sleep(1.1)
        current_state = io.input(pir_sensor)

#Read the Current_State of the Sensor and immediately set the GPIOs to that val$
        io.output(piezo,current_state)
        io.output(st17,current_state)
        io.output(bLed,current_state)
        io.output(relay,current_state)
        time.sleep(5.5)
        io.output(piezo,False)
#Provide verbose output on the states if needed
        if current_state == 1:
            print("MOTION ALARM ACTIVATED GPIO pin %s is %s" % (pir_sensor, curr                                                                                        ent_state))
            time.sleep(1)
        else:      #current_state==0:
            io.output(piezo,False)
            print("GPIO pin %s is %s" % (pir_sensor, current_state))
            print('NO ACTIVITY,current state zerooooooo')

#Make sure we do not have a ripple effect, give sometime for other HW to read G$
           # time.sleep(2)

except KeyboardInterrupt:

    pass
    io.output(st17,0)
    io.output(bLed,0)
    io.output(relay,0)
finally:
    io.output(st17,0)
    io.cleanup()
