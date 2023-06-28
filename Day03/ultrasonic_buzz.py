import RPi.GPIO as GPIO
import time

Buzzer_Pin = 25
Trig_Pin = 24
Echo_Pin = 23

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(Buzzer_Pin, GPIO.OUT) # Buzzer=25
GPIO.setup(Trig_Pin, GPIO.OUT) # Trig=24
GPIO.setup(Echo_Pin, GPIO.IN)  # Echo=23

buzz = GPIO.PWM(Buzzer_Pin, 440)

print ("Press SW or input Ctrl+C to quit")

def make_noise(Hz, Time):
	buzz.start(50)
	buzz.ChangeFrequency(Hz)
	time.sleep(Time)
	buzz.stop()
	time.sleep(Time)

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
            
            if 4 < distance < 6:
            	make_noise(800, 0.1)
            elif distance <= 4:
            	make_noise(2000, 0.1)

            print (f"Distance => , {distance}, cm")

except KeyboardInterrupt:
    GPIO.cleanup()
    Print("bye~")
