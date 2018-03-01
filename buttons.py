import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
button_pin = 24
red_LED_pin = 20
yellow_LED_pin = 21 
green_LED_pin = 22
count = 0

GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) #button on GPIO23
GPIO.setup(red_LED_pin, GPIO.OUT)
GPIO.setup(yellow_LED_pin, GPIO.OUT)
GPIO.setup(green_LED_pin, GPIO.OUT)
GPIO.setwarnings(False)

GPIO.output(20,False)
GPIO.output(21,False)
GPIO.output(22,False)
try:
    while True:
        button_state = GPIO.input(button_pin)
        if button_state == False: 
            count = count + 1
            if count == 1:
                print ('First press...')
                GPIO.output(red_LED_pin, True)
                time.sleep(.1)
            elif count == 2:
                print ('Second press...')
                GPIO.output(red_LED_pin,True)
                GPIO.output(yellow_LED_pin,True)
                time.sleep(.1)
            elif count == 3:
                print ('Third press...')
                while True:
                    GPIO.output(red_LED_pin, True)
                    GPIO.output(yellow_LED_pin, True)
                    GPIO.output(green_LED_pin, True)
                    time.sleep(.5)
                    GPIO.output(20,False)
                    GPIO.output(21,False)
                    GPIO.output(22,False)
                    time.sleep(.5)
        else:
            time.sleep(.1)
        
except: 
    GPIO.cleanup()
