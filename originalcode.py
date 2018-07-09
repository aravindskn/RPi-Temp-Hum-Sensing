import RPi.GPIO as GPIO
import dht11
import time
import datetime
import urllib2

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 14
instance = dht11.DHT11(pin = 22)

api_key = "FZRJ1ZLAB3AVFQQE"
base_url = "http://api.thingspeak.com/update?api_key=%s" % api_key

while True:
    result = instance.read()
    if result.is_valid():
        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temperature: %d C" % result.temperature)
        print("Humidity: %d %%" % result.humidity)
        try:
            url = base_url + "&field1=%s&field2=%s" % (result.temperature, result.humidity)
            print(url)
            f = urllib2.urlopen(url)
            print f.read()
            f.close()           
        except:
            print("error")
            pass
    time.sleep(60) 
