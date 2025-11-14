import dht
import machine
import time

sensor = dht.DHT11(machine.Pin(4))

filename = "dht_data.csv"

with open(filename, "w") as f:
    f.write("Temperature,Humidity\n")

for i in range(5):
    sensor.measure()
    t = sensor.temperature()
    h = sensor.humidity()
    with open(filename, "a") as f:
        f.write(f"{t},{h}\n")
    time.sleep(2)

with open(filename, "r") as f:
    data = f.read()
    print(data)
