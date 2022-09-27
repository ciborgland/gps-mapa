#include "TinyGPS++.h"
#include "SoftwareSerial.h"

SoftwareSerial serial_connection(4, 3);
TinyGPSPlus gps;

void setup()
{
  Serial.begin(9600);
  serial_connection.begin(9600);
}

void loop()
{
  while(serial_connection.available())
  {
    gps.encode(serial_connection.read());
  }
  if(gps.location.isUpdated())
  {  
    Serial.println("latitud:"+String(gps.location.lat(), 6));
    Serial.println("longitud:"+String(gps.location.lng(), 6));
    
    delay(5000);
  }
}
