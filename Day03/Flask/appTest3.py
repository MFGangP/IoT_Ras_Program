from flask import Flask, request

app = Flask(__name__) # 객체 생성

@app.route('/') # IP만 가지고 접속하면 다음 함수 출력
def get():
	val1 = request.args.get("이름", "user")
	val2 = request.args.get("주소", "부산")
	return val1 + " : " + val2
 
if __name__ == "__main__":
	app.run(host="0.0.0.0", port="8800")

	
