import random
import time
from python.csv_logger import save_to_csv
from python.calculations import calculate_power, calculate_efficiency

while True:
    voltage = round(random.uniform(11.5, 12.5), 2)
    current = round(random.uniform(0.2, 1.5), 2)
    temperature = round(random.uniform(25, 45), 2)

    power = calculate_power(voltage, current)
    efficiency = calculate_efficiency(power, power + random.uniform(1, 3))

    print(f"Voltage: {voltage} V")
    print(f"Current: {current} A")
    print(f"Temperature: {temperature} °C")
    print(f"Power: {power} W")
    print(f"Efficiency: {efficiency} %")
    print("-" * 40)

    save_to_csv(voltage, current, temperature, power, efficiency)

    time.sleep(2)