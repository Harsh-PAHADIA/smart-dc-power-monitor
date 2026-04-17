import serial
from config import SERIAL_PORT, BAUD_RATE

ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)

def read_serial_data():
    while True:
        try:
            line = ser.readline().decode('utf-8').strip()

            if line:
                data = line.split(',')

                voltage = float(data[0])
                current = float(data[1])
                temperature = float(data[2])

                return voltage, current, temperature

        except:
            continue