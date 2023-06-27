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
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzerPin, GPIO.OUT)
GPIO.setwarnings(False)
buzz = GPIO.PWM(buzzerPin, 440) # 440Hz 를 갖는 객체 생성

def buzz_start_end(melody):
  buzz.start(50)
  buzz.ChangeFrequency(melody)
  time.sleep(1)
  buzz.stop()
  time.sleep(0.3)
  print(f"value = {melody}")
while True:
	Key = input("키를 입력해주세요 : ")
	if Key == "1":
		melody=C
		buzz_start_end(melody)
	elif  Key == "2":
	  melody=D
	  buzz_start_end(melody)
	elif  Key == "3":
		melody=E
		buzz_start_end(melody)
	elif  Key == "4":
	  melody=F
	  buzz_start_end(melody)
	elif  Key == "5":
	  melody=G
	  buzz_start_end(melody)
	elif  Key == "6":
	  melody=A
	  buzz_start_end(melody)
	elif  Key == "7":
	  melody=B
	  buzz_start_end(melody)
	else:
		print("1~7 사이 값을 입력해주세요")
