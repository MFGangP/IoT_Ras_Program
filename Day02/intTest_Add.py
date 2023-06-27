import RPi.GPIO as GPIO
import time

swPin=13
Led_Pin=14
Buzzer_Pin=15

count = 1
Hz = 149

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM)
GPIO.setup(swPin, GPIO.IN)
GPIO.setup(Buzzer_Pin, GPIO.OUT)
GPIO.setup(Led_Pin, GPIO.OUT)
buzz = GPIO.PWM(Buzzer_Pin, 440)

def callbackfunc(channel):
	global count 
	count += 1

GPIO.add_event_detect(swPin, GPIO.RISING, callback=callbackfunc)

try:
	while True:
		if(count % 2 == 0):
			GPIO.output(Led_Pin, 0)
			buzz.stop()
			time.sleep(1)			
		elif(Hz >= 1800):
			for i in range(1800, 149, -1):
				buzz.start(50)
				buzz.ChangeFrequency(i)
				time.sleep(0.001)
				GPIO.output(Led_Pin, 1)
				time.sleep(0.001)
				GPIO.output(Led_Pin, 0)
				time.sleep(0.001)
				print(f"{i},{Hz}")				
				Hz -= 1
				if(count % 2 == 0):
					GPIO.output(Led_Pin, 0)
					buzz.stop()
					time.sleep(2)		
		elif(Hz < 1800):
			for i in range(150, 1801):
				buzz.start(50)
				buzz.ChangeFrequency(i)
				time.sleep(0.001)
				GPIO.output(Led_Pin, 1)
				# buzz.ChangeFrequency(i)
				time.sleep(0.001)
				GPIO.output(Led_Pin, 0)
				time.sleep(0.001)
				Hz += 1
				print(f"{i},{Hz}")
				if(count % 2 == 0):
					GPIO.output(Led_Pin, 0)
					buzz.stop()
					time.sleep(2)

except KeyboardInterrupt:
	GPIO.cleanup()
