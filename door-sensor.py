import RPi.GPIO as GPIO
import time
 
pir_sensor = 26
piezo = 27
st17=17
 
GPIO.setmode(GPIO.BCM)
 
GPIO.setup(piezo,GPIO.OUT)
GPIO.setup(st17,GPIO.OUT)
GPIO.setup(pir_sensor,GPIO.IN)
 
current_state = 0
GPIO.output(st17,current_state)
try:
     while True:
        time.sleep(0.1)
        current_state = GPIO.input(pir_sensor)
 
#Read the Current_State of the Sensor and immediately set the GPIOs to that value
        GPIO.output(piezo,current_state)       
        GPIO.output(st17,current_state)
 
#Provide verbose output on the states if needed
        if current_state == 1:
            print("GPIO pin %s is %s" % (pir_sensor, current_state))
       
        else:      #current_state==0:
            GPIO.output(piezo,False)
            print("GPIO pin %s is %s" % (pir_sensor, current_state))
            print('current state zerooooooo')
                               
#Make sure we do not have a ripple effect, give sometime for other HW to read GPIO values and for the Piezo to sound
            time.sleep(2)
 
except KeyboardInterrupt:
 
    pass
    GPIO.output(st17,0)
finally:
    GPIO.output(st17,0)
    GPIO.cleanup()
