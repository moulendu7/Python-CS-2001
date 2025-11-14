import csv

sensor_readings = [
    ["Name", "Temperature", "Humidity"],
    ["Sensor_A", 25.3, 45],
    ["Sensor_B", 26.1, 48],
    ["Sensor_C", 24.8, 50]
]

try:
    with open("sensor_data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(sensor_readings)
    print("Data written to sensor_data.csv successfully.")
except PermissionError:
    print("Permission denied: Cannot write to sensor_data.csv.")
except Exception as e:
    print("Error writing file:", e)

try:
    print("\nReading sensor_data.csv:\n")
    with open("sensor_data.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
except FileNotFoundError:
    print("Error: sensor_data.csv not found.")
except PermissionError:
    print("Permission denied: Cannot read sensor_data.csv.")
except Exception as e:
    print("Error reading file:", e)
