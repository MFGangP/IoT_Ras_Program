import RPi.GPIO as GPIO
import time

Gpio_Sig_Port=14
Gpio_Pin_Num=[20,21,22,23,24,25,26]
Seven_Seg_Num=((1,1,1,1,1,1,0), #0
							 (0,1,1,0,0,0,0), #1
							 (1,1,0,1,1,0,1), #2
							 (1,1,1,1,0,0,1), #3
							 (0,1,1,0,0,1,1), #4
							 (1,0,1,1,0,1,1), #5
							 (1,0,1,1,1,1,1), #6
							 (1,1,1,0,0,0,0), #7
							 (1,1,1,1,1,1,1), #8
							 (1,1,1,1,0,1,1), #9
							 (1,1,1,0,1,1,1), #A
							 (1,1,1,1,1,1,1), #B
							 (1,0,0,1,1,1,0), #C
							 (1,1,1,1,1,1,0), #D
							 (1,0,0,1,1,1,1), #E
							 (1,1,1,0,0,0,1)) #F

GPIO.setmode(GPIO.BCM) # GPIO 모드 설정
GPIO.setup(Gpio_Pin_Num[0],GPIO.OUT) # 20번핀 출력
GPIO.setup(Gpio_Pin_Num[1],GPIO.OUT) # 21번핀 출력
GPIO.setup(Gpio_Pin_Num[2],GPIO.OUT) # 22번핀 출력
GPIO.setup(Gpio_Pin_Num[3],GPIO.OUT) # 23번핀 출력
GPIO.setup(Gpio_Pin_Num[4],GPIO.OUT) # 24번핀 출력
GPIO.setup(Gpio_Pin_Num[5],GPIO.OUT) # 25번핀 출력
GPIO.setup(Gpio_Pin_Num[6],GPIO.OUT) # 26번핀 출력
GPIO.setup(Gpio_Sig_Port, GPIO.IN) # 18번핀 입력
i = 0
while True:
	Value = GPIO.input(Gpio_Sig_Port)
	if Value == True:
	# 출력(핀번호, 세그먼트 신호(0 또는 1))
		GPIO.output(Gpio_Pin_Num[0], Seven_Seg_Num[i][0])
		GPIO.output(Gpio_Pin_Num[1], Seven_Seg_Num[i][1])
		GPIO.output(Gpio_Pin_Num[2], Seven_Seg_Num[i][2])
		GPIO.output(Gpio_Pin_Num[3], Seven_Seg_Num[i][3])
		GPIO.output(Gpio_Pin_Num[4], Seven_Seg_Num[i][4])
		GPIO.output(Gpio_Pin_Num[5], Seven_Seg_Num[i][5])
		GPIO.output(Gpio_Pin_Num[6], Seven_Seg_Num[i][6])
		if i!=15:
			i = i + 1
		else:
			i = 0
	# 1초 대기
	time.sleep(0.3)

GPIO.cleanup()
