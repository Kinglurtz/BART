#import RPi.GPIO as GPIO
import time

FLOW_RATE = 60.0/100.0
class Pump():

    def __init__(self, pumpNumber, line):
        input = [x.strip() for x in line.split(',')]
        self.pumpNumber = pumpNumber
        self.ingredient = input[0]
        #TODO add pin number to init and config file

    def Pour(self, pourTime):
        print("Pouring from pump " + str(self.pumpNumber))
        print("Pour time in seconds: " + str(pourTime))
        #GPIO.output(pin, GPIO.LOW)
        time.sleep(pourTime)
        print("Done pouring from pump")
        #GPIO.output(pin, GPIO.HIGH)