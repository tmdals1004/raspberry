## jodo sensor
```c
void setup(){
  Serial.begin(9600);
  }
  
void loop(){
  int cds = analogRead(A1);
  Serial.prinln(cds);
  }
```

## dht 11 sensor
```c
#include <DHT11.h>
int pin = A1;
DHT11 dht11(pin);

void setup(){
  int i;
  float humi, temp;
  if((i = dht11.read(humi, temp)) == 0){
    Serial.print("humidity:");
    Serial.prinln(humi);
    Serial.print("temperature:");
    Serial.println(temp);
    }
  else{
    Serial.print("Error:");
    Serial.print(i);
    }
  delay(1000);
}
```



```c
#!/usr/bin/python

import time
import RPi.GPIO as GPIO
import requests, json
from influxdb import InfluxDBClient as influxdb

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)

def interrupt_fired(channel):
    print("interrupt Fired")
    a = 5
    data = [{
        'measurement' : 'pir',        
        'tags':{
            'VisionUni' : '2410',
        },
        'fields':{
            'pir' : a,
        }
    }]
    client = None
    try:
        client = influxdb('localhost',8086,'root','root','pir')
    except Exception as e:
        print "Exception" + str(e)
    if client is not None:
        try:
            client.write_points(data)
        except Exception as e:
            print "Exception write " + str(e)
        finally:
            client.close()
    print(a)
GPIO.add_event_detect(4, GPIO.FALLING, callback=interrupt_fired)

while(True):
    time.sleep(1)
    a = 1
    data = [{
        'measurement' : 'temp',        
        'tags':{
            'VisionUni' : '2410',
        },
        'fields':{
            'temp' : a,
        }
    }]
    client = None
    try:
        client = influxdb('localhost',8086,'root','root','temp')
    except Exception as e:
        print "Exception" + str(e)
    if client is not None:
        try:
            client.write_points(data)
        except Exception as e:
            print "Exception write " + str(e)
        finally:
            client.close()
    print("running influxdb OK")
```
