import RPi.GPIO as GPIO
import dht11
import time
import datetime
import urllib2
import json
import requests
import os
import os.path
import subprocess
from subprocess import STDOUT,PIPE

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 22
instance = dht11.DHT11(pin = 22)

api_key = "FZRJ1ZLAB3AVFQQE"
base_url = "http://api.thingspeak.com/update?api_key=%s" % api_key

#edited part starts
flag=0
CHANNELID= "283442"
APIKEY= "9Y6MZFCXUM47XOXF"
now = datetime.datetime.now()
today12am = now.replace(hour=11, minute=39, second=0, microsecond=0)
hour="13"
minute="42"
eminute="43"
ihour=int(hour)
iminute=int(minute)
ieminute=int(eminute)
#edited part ends

while True:
    result = instance.read()
    if result.is_valid():
        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temperature: %d C" % result.temperature)
        print("Humidity: %d %%" % result.humidity)
        #edited part starts
        print(flag)
        cur_hour = datetime.datetime.now().hour
        curr_minute = datetime.datetime.now().minute
        print(cur_hour)
        print(curr_minute)
        print(today12am)
        print(now)
        if ihour == cur_hour and curr_minute >= iminute  and curr_minute < ieminute :
            flag = 0
            print("test")
        if result.temperature>25:
            print("Overheating")
            if flag==0:
             flag=1
             print(flag)
             def compile_java(str):
                subprocess.check_call(['javac', str])

             def execute_java(str, stdin):
                java_class, ext = os.path.splitext(str)
                cmd = ['java', java_class]
                proc = subprocess.Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
                stdout, stderr = proc.communicate(stdin)
                print(stdout)

             compile_java('str.java')
             execute_java('str.java',str(result.temperature))
            url1= "https://api.thingspeak.com/channels/283442/feeds.json?api_key=9Y6MZFCXUM47XOXF&results=2"
            #headers = {'content-type': 'application/json', "Oracle-Mobile-Backend-Id":"35ecb548-c797-48a4-b1c9-cd18e60dc1d8" ,"authorization":"Basic R1NFMDAwMTAxNjBfTUNTX01PQklMRV9BTk9OWU1PVVNfQVBQSUQ6YjRzaXR6WWcwbF9lYnk="}
            #url = 'https://mcs-gse00010160.mobileenv.us2.oraclecloud.com:443/mobile/custom/thingspeakapi/lasttemp'+CHANNELID+'/feeds.json?api_key='+APIKEY+'&results=1'

            #data = {"eventType": "AAS_PORTAL_START", "data": {"uid": "hfe3hf45huf33545", "aid": "1", "vid": "1"}}
            #params = {'CHANNELID':'283442', 'APIKEY':'9Y6MZFCXUM47XOXF'}

            #requests.post(url, params=params , headers=headers)
            print(url1)
            f = urllib2.urlopen(url1)
            print f.read()
            f.close()
        if result.temperature<20:
            print("Overcooling")
        #edited part ends
        try:
            url = base_url + "&field1=%s&field2=%s" % (result.temperature, result.humidity)
            print(url)
            f = urllib2.urlopen(url)
            print f.read()
            f.close()           
        except:
            print("error")
            pass
    time.sleep(5)


