import RPi.GPIO as GPIO
import time

btnPin = 24
# BCM 모드 
# BOARD 모드 = GPIO 핀번호를 쓰면 안된다.
GPIO.setmode (GPIO.BCM)
count = 0
def handler(chennel):
	global count
	count = count + 1
	print(count)
	
# pull_up_down=GPIO.PUD_DOWN이거 때문에 연결이 된다.
GPIO.setup(btnPin, GPIO.IN)
GPIO.add_event_detect(btnPin, GPIO.RISING, callback=handler)
while True:
	time.sleep(1)
