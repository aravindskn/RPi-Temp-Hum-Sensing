# coding=utf-8
import RPi.GPIO as GPIO  #Raspberry Pi I/O pins access
import dht11             #Temp/Hum Sensor
import time              #Time
import datetime          #Date&Time
import urllib2
import os                #java execution
import os.path           #java execution
import subprocess        #java execution
from subprocess import STDOUT,PIPE      #java execution
import json
import requests
import pprint

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 22
instance = dht11.DHT11(pin = 22)

#API token and ThingSpeak URL
api_key = "FZRJ1ZLAB3AVFQQE"
base_url = "http://api.thingspeak.com/update?api_key=%s" % api_key

#flag initialisation for java code execution
flag=0

#Loop for reading temperature and humidity
while True:
    result = instance.read()
    if result.is_valid():             #valid result check
        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temperature: %d C" % result.temperature)
        print("Humidity: %d %%" % result.humidity)


        if result.temperature>30:                                         #check if temperature sensed greater than 30 for java execution
            print("WARNING!!!!! OVERHEATING!!! TEMPERATURE ABOVE 30C")
            print("SENDING DATA TO ENTERPRISE ASSET MANAGEMENT TOOL")
            print("WORK REQUEST GENERATED!!")
            print()
            if flag==0:                                                   #flag checked to see if java code already executed
              flag=1                                                      #flag set to 1, java code already executed
              #print(flag)
              def compile_java(test):                                     #call compile java method passing java filename
                subprocess.check_call(['javac', test])                    #command for execution of java code in terminal

              def execute_java(test, stdin):                              #execution of java code parameters:filename,parameter passed
                java_class, ext = os.path.splitext(test)
                cmd = ['java', java_class]
                proc = subprocess.Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
                stdout, stderr = proc.communicate(stdin)
                print(stdout)

              compile_java('test.java')
              execute_java('test.java',str(result.temperature))

              urle='https://apex1-a18513.db.em2.oraclecloudapps.com/apex/transmobileservice/transsendmail/'			#API for email service
              payload={																								#POST method call payload
                       'FROM':'iot@transsys.com',
                        'CC':'aravindskn97@outlook.com',
                       'TO':'aravindsknair@outlook.com',
                       'TEXT_BODY':'Asset ID:FL1010 Overheating. SYSTEM TEMPERATURE ABOVE 30C. Work Request Generated For the Asset. Please Shutdown the Asset or Change Cooling Temperature',
                       'HTML_BODY':'',
                       'SUBJECT':'WARNING! TEMPERATURE ABOVE 30C'
                      }
              headers={'Content-Type': 'application/json','authorization':'Basic aGNtLnVzZXI6T3JhY2xlMTIz'}			#headers for post method api call
              r=requests.post(urle, data=json.dumps(payload), headers=headers)										#call the api
              print(r.content)																						#prints the status from the email after sending
              print("EMAIL NOTIFICATION SENT")																		

        if result.temperature<20:
            print("WARNING!!!! OVERCOOLING!!! TEMPERATURE BELOW 20C")

        try:
            url = base_url + "&field1=%s&field2=%s" % (result.temperature, result.humidity)   #call thingspeak api for data push
            #print(url)
            f = urllib2.urlopen(url)                                                          #open url for pushing data
            print f.read()
            f.close()
        except:
            print("error")
            pass
    time.sleep(5)                                                                             #time interval for sensor read


