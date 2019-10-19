import influxdb
import ttn
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

class InfluxDB:
    def __init__(self, config):
        self.username = config["INFLUXDB"]["influxdbuser"]
        self.password = config["INFLUXDB"]["influxdbpasswd"]
        self.hostname = config["INFLUXDB"]["influxdbhostname"]
        self.port = config["INFLUXDB"]["influxdbport"]
        self.database = config["INFLUXDB"]["influxdbdatabase"]
        self.client = influxdb.InfluxDBClient(host=self.hostname, port=self.port, username=self.username, password=self.password, database=self.database, ssl=True)

    def send(self, measurement, time, Temperatur, Luftfeuchtigkeit, Luftdruck):
        
        json_body = [
        {
            "measurement": "Sensor_1",
            "tags": {
                "host": "server01",
                "region": "us-west"
            },
            "time": time,
            "fields": {
                "Temperatur": float(Temperatur),
                "Luftfeuchtigkeit": float(Luftfeuchtigkeit),
                "Luftdruck": float(Luftdruck)

            }
        }
    ]        
        print(json_body)
        self.client.write_points(json_body)

