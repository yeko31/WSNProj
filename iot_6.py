import thingspeak
import time
import Adafruit_DHT

channel_id = 2298341
write_key = "Y8N7QGY3RDXVE31T"

pin=18
sensor= Adafruit_DHT.DHT11

def measure(channel):
    try:
        humidity,temperature = Adafruit_DHT.read_retry(sensor,pin)

        if humidity is not None and temperature is not None:
            print("Temperature={0:0.1f}*C Humidity={1:0.1f}%".format(temperature,humidity))

        else:
            print("Did not receive any reading from sensor.Please Check!")

        response=channel.update({"field1":temperature,"field2":humidity})
    except:
        print("connection failure")


if __name__ =="__main__":
    channel = thingspeak.Channel(id=channel_id, api_key=write_key)

    while True:
        measure(channel)

        time.sleep(15)

        



            
