import csv
import os
from datetime import datetime
from config import CSV_FILE

file_exists = os.path.isfile(CSV_FILE)

if not file_exists:
    with open(CSV_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            'Timestamp',
            'Voltage',
            'Current',
            'Temperature',
            'Power',
            'Efficiency'
        ])

def save_to_csv(voltage, current, temperature, power, efficiency):
    with open(CSV_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            datetime.now(),
            voltage,
            current,
            temperature,
            power,
            efficiency
        ])