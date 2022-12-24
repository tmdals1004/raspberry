# raspberry
## hangul
```
$ sudo apt-get install fonts-unfonts-core
$ sudo apt-get install ibus ibus-hangul
$ sudo reboot
```


# arduino
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
