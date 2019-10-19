#include "Arduino.h"
#include "RfmTTN.h"

//#include <Adafruit_Sensor.h>
//#include <DHT.h>

#include <Wire.h>
#include "cactus_io_BME280_I2C.h"

//#define DHTPIN		9
//#define DHTTYPE		DHT22
//DHT dht(DHTPIN, DHTTYPE);

BME280_I2C bme(0x76);

void setup()
{
	Serial.begin(115200);
	Serial.println(F("Startup..."));
	RfmTTN::init();
	Serial.println(F("...done."));
	// dht.begin();
	if (!bme.begin()) {
		Serial.println("Could not find a valid BME280 sensor, check wiring!");
		while (1);
	}
	bme.setTempCal(-1);// Temp was reading high so subtract 1 degree
	}

uint8_t buffer[100];

void loop()
{
	bme.readSensor();
	int16_t h = bme.getHumidity()*100;
	int16_t p = bme.getPressure_MB()*10;
	int16_t t = bme.getTemperature_C()*100;
	
	bool t_prefix;
		if (t<0){
			t_prefix = 1;
		}
		else{
			t_prefix = 0;
		}

	
	int8_t h_LO = lowByte(h);
	int8_t h_HI = highByte(h);

	int8_t p_LO = lowByte(p);
	int8_t p_HI = highByte(p);
	
	Serial.println(t);
	int8_t t_LO = lowByte(abs(t));
	int8_t t_HI = highByte(abs(t));
	Serial.println(t);

	Serial.print("Humidity: ");
	Serial.println(h);
	Serial.print("Pressure: ");
	Serial.println(p);
	Serial.print("Temp: ");
	Serial.println(t);


	uint8_t humi = (uint8_t)h;
	int8_t temp = (int8_t)t;
	uint16_t pres = (uint16_t)p;

	buffer[0] = h_HI;
 	buffer[1] = h_LO;
	buffer[2] = p_HI;
	buffer[3] = p_LO;
	buffer[4] = t_HI;
	buffer[5] = t_LO;
	buffer[6] = t_prefix;

	RfmTTN::sendData(buffer, 7);

	delay(60000);
}
