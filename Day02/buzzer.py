import RPi.GPIO as GPIO
import time

C=262
D=294
E=330
F=349
G=392
A=440
B=494

buzzerPin = 13
melody = [G,G,A,A,G,G,E,G,G,E,E,D,G,G,A,A,G,G,E,G,E,D,E,C]
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzerPin, GPIO.OUT)

buzz = GPIO.PWM(buzzerPin, 440) # 440Hz 를 갖는 객체 생성

try:
	while True:
		buzz.start(50)	# duty cycle 50으로 PWM 출력시작
		for i in range(0, len(melody)):
			buzz.ChangeFrequency(melody[i]) # 주파수 변경
			time.sleep(0.3)
		buzz.stop()	# PWM 종료
		time.sleep(1)

except KeyboardInterrupt:	# 키보드 인터럽트
	GPIO.cleanup()
