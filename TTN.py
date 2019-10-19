import ttn 
import configparser

config = configparser.ConfigParser()
config.read("config.ini")


def ttn_handler(msg,client):
    print("receive data from "+msg.dev_id)
    print(msg)

handler = ttn.HandlerClient(config["TTN"]["apikey"])