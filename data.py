## IMPORTANT NOTICE: YOU MUST ADD THE BELOW LINE TO THE 'REQUIREMENTS.TXT' FILE AND PROPERLY INSTALL IT
#   adafruit-circuitpython-ahtx0


# Author: Colby Sawyer 11-18-2021

## NOTICE: this file is intended for the AHT20 to be connected via I2C

from typing import Sequence
import board
import time
import adafruit_ahtx0


# Create sensor object, using the board's default I2C bus.
i2c = board.I2C()   # uses board.SCL and board.SDA
sensor = adafruit_ahtx0.AHTx0(i2c)

def get_data():
    sensor_data = bytearray(7)
    FEATHER_ID = 1

    # Get sensor readings
    temp_val = int(sensor.temperature * 100)
    print("\nTemperature: %0.1f C" % sensor.temperature)
    humid_val = int(sensor.humidity * 100)
    print("Humidity: %0.1f %%" % sensor.humidity)

    sensor_data[0] = FEATHER_ID
    # Temperature data
    sensor_data[1] = (temp_val >> 8) & 0xff
    sensor_data[2] = temp_val & 0xff
    # Humidity data
    sensor_data[3] = (humid_val >> 8) & 0xff
    sensor_data[4] = humid_val & 0xff

    return sensor_data
