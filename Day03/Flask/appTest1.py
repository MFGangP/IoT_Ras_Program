from flask import Flask

app = Flask(__name__) # 객체 생성

@app.route('/') # IP만 가지고 접속하면 다음 함수 출력
def hello_World():
	return "Hello World"

@app.route('/name')#name 이라는 웹페이지를 띄운다
def namefunc():
    return "Hong kil-dong"

if __name__ == "__main__":
	app.run(host="0.0.0.0", port="9000")

	
