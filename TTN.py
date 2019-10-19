import ttn 
import configparser
import time
import test

config = configparser.ConfigParser()
config.read("config.ini")


def ttn_handler(msg,client):
    print("receive data from "+msg.dev_id)
    Time = msg.metadata.time
    Temperature = msg.payload_fields.temperature
    Humidity = msg.payload_fields.humidity
    Pressure = msg.payload_fields.pressure
    print(Time)
    print(Temperature)
    print(Humidity)
    print(Pressure)

    influx.send("Sensor_1",Time,Temperature,Humidity,Pressure)
    print("tests")

handler = ttn.HandlerClient(config["TTN"]["appid"],config["TTN"]["apikey"])

influx = test.InfluxDB(config)
print(influx)
mqtt_client = handler.data()
mqtt_client.set_uplink_callback(ttn_handler)
mqtt_client.connect()
while True: time.sleep(1)
mqtt_client.close()



print("closing client")

