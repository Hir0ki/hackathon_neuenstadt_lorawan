import influxdb
import ttn
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

username = config["INFLUXDB"]["influxdbuser"]
password = config["INFLUXDB"]["influxdbpasswd"]
hostname = config["INFLUXDB"]["influxdbhostname"]
port = config["INFLUXDB"]["influxdbport"]
database = config["INFLUXDB"]["influxdbdatabase"]

client = influxdb.InfluxDBClient(host=hostname, port=port, username=username, password=password, database=database)



