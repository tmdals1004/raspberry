#!/usr/bin/python3

import sys, serial, time
import requests, json
from influxdb import InfluxDBClient as influxdb


device = serial.Serial('/dev/ttyACM0', 9600, timeout=5)

while(True):
    try:
        rcvBuf = device.readline()
#        device.reset_input_buffer()
#        rcvBuf = device.read_until(size=12)
#        rcvBuf = rcvBuf.decode()
#        print(rcvBuf.decode())
        rcvBuf = rcvBuf.decode()
        humi = rcvBuf.split(' ')[0]
        temp = rcvBuf.split(' ')[1]
        print(rcvBuf)
        
        
        
        data = [{
            'measurement':'tt',
            'tags':{
                'hgcom':'1111',
                },
            'fields':{
                'humi':float(humi),
                'temp':float(temp),
                }
            }]
        client = None
        try:
            client = influxdb('localhost', 8086,'roor','root','temp')
        except Exception as e:
            print("Exception" + str(e))
        if client is not None:
            try:
                client.write_points(data)
            except Exception as e:
                print("Exception write" + str(e))
            finally:
                print("influxdb write OK")
                client.close()

    except Exception as e:
        print("Exception read" + str(e))

    time.sleep(1)

