import pandas as pd
import matplotlib.pyplot as plt

file_path = 'data/sensor_data.csv'

df = pd.read_csv(file_path, header=None, names=['Time', 'Voltage', 'Current', 'Temperature', 'Power', 'Efficiency'])

plt.figure(figsize=(10, 5))
plt.plot(df['Voltage'])
plt.title('Voltage vs Time')
plt.xlabel('Reading Number')
plt.ylabel('Voltage (V)')
plt.grid(True)
plt.savefig('graphs/voltage_vs_time.png')

plt.figure(figsize=(10, 5))
plt.plot(df['Current'])
plt.title('Current vs Time')
plt.xlabel('Reading Number')
plt.ylabel('Current (A)')
plt.grid(True)
plt.savefig('graphs/current_vs_time.png')

plt.figure(figsize=(10, 5))
plt.plot(df['Temperature'])
plt.title('Temperature vs Time')
plt.xlabel('Reading Number')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.savefig('graphs/temperature_vs_time.png')

plt.figure(figsize=(10, 5))
plt.plot(df['Power'])
plt.title('Power vs Time')
plt.xlabel('Reading Number')
plt.ylabel('Power (W)')
plt.grid(True)
plt.savefig('graphs/power_vs_time.png')

plt.figure(figsize=(10, 5))
plt.plot(df['Efficiency'])
plt.title('Efficiency vs Time')
plt.xlabel('Reading Number')
plt.ylabel('Efficiency (%)')
plt.grid(True)
plt.savefig('graphs/efficiency_vs_load.png')

print('All graphs saved successfully!')