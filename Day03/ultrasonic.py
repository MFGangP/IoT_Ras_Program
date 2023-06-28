import RPi.GPIO as GPIO
import time

Trig_Pin = 24
Echo_Pin = 23

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(Trig_Pin, GPIO.OUT) # Trig=24
GPIO.setup(Echo_Pin, GPIO.IN)  # Echo=23

print ("Press SW or input Ctrl+C to quit")

try:
    while True:
            GPIO.output(24, False)
            time.sleep(0.5)

            GPIO.output(24, True)
            time.sleep(0.00001)
            GPIO.output(24, False)

            while GPIO.input(23) == 0:
               start = time.time()

            while GPIO.input(23) == 1:
               stop = time.time()

            time_interval = stop - start
            distance = time_interval * 17000
            distance = round(distance, 2)

            print (f"Distance => , {distance}, cm")

except KeyboardInterrupt:
    GPIO.cleanup()
    Print("bye~")
