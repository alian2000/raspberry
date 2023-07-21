import requests

# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: 2019 Mikey Sklar for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import glob
import time

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f

#while True:
#    print(read_temp())
#    time.sleep(1)

import board
import busio
import adafruit_tsl2561

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the TSL2561 instance, passing in the I2C bus
tsl = adafruit_tsl2561.TSL2561(i2c)

# Print chip info
print("Chip ID = {}".format(tsl.chip_id))
print("Enabled = {}".format(tsl.enabled))
print("Gain = {}".format(tsl.gain))
print("Integration time = {}".format(tsl.integration_time))

print("Configuring TSL2561...")

# Enable the light sensor
tsl.enabled = True
time.sleep(1)

# Set gain 0=1x, 1=16x
tsl.gain = 0

# Set integration time (0=13.7ms, 1=101ms, 2=402ms, or 3=manual)
tsl.integration_time = 1
while True:
    print("Getting readings...")
    id=0

    # Get raw (luminosity) readings individually
    broadband = tsl.broadband
    infrared = tsl.infrared

    # Get raw (luminosity) readings using tuple unpacking
    # broadband, infrared = tsl.luminosity

    # Get computed lux value (tsl.lux can return None or a float)
    lux = tsl.lux


    # Print results
    print("Enabled = {}".format(tsl.enabled))
    print("Gain = {}".format(tsl.gain))
    print("Integration time = {}".format(tsl.integration_time))
    print("Broadband = {}".format(broadband))
    print("Infrared = {}".format(infrared))
    print(read_temp())
    time.sleep(1)
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)

    print("----------------------------")
    if lux is not None:
        print("Lux = {}".format(lux))
        r = requests.post('http://192.168.86.148/posts', json={"lux":int(lux),"sensor_name": "kitchen","time":current_time})
        print (r.status_code )
    else:
        print("Lux value is None. Possible sensor underrange or overrange.")

# Disble the light sensor (to save power)
tsl.enabled = False
