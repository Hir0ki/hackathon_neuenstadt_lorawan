import ttn 
import configparser

config = configparser.ConfigParser()
config.read("config.ini")


def ttn_handler(msg,client):
    print("receive data from "+msg.dev_id)
    print(msg)

handler = ttn.HandlerClient(config["TTN"]["appid"],config["TTN"]["apikey"])

mqtt_client = handler.data()
mqtt_client.set_uplink_callback(uplink_callback)
mqtt_client.connect()
time.sleep(60)
mqtt_client.close()

app_client =  handler.application()
my_app = app_client.get()
print(my_app)
my_devices = app_client.devices()
print(my_devices)