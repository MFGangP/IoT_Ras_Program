from flask import Flask, request, render_template
import RPi.GPIO as GPIO

app = Flask(__name__)

BUZZ_Pin = 24
BUZZ_State = 0
LED_Pin = 23
LED_State = 0
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZ_Pin, GPIO.OUT)
GPIO.setup(LED_Pin, GPIO.OUT)

buzz = GPIO.PWM(BUZZ_Pin, 440)

@app.route('/')
def home(): # home 화면에 들어갔을 때 
	return "Hello Flask"
@app.route('/test')
def get(): # test 화면에 들어갔을 때
	if request.args.get('LED_ON_OFF')=='LED':
		global LED_State		
		if(LED_State==0):
			GPIO.output(LED_Pin, 1)
			LED_State = 1
		elif(LED_State!=0):
			GPIO.output(LED_Pin, 0)
			LED_State = 0
	if request.args.get('BUZZ_ON_OFF') == 'BUZZ':
		global BUZZ_State
		if(BUZZ_State==0):
			buzz.start(50)
			buzz.ChangeFrequency(200)
			BUZZ_State = 1
		else:
			buzz.stop()
			BUZZ_State = 0
	return render_template('get.html')

@app.route('/post')
def post():
	return render_template('default.html')

if __name__ == "__main__":
	app.run(host='0.0.0.0', port='8080', debug=True)
