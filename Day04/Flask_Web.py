from flask import Flask, request

app = Flask(__name__) # 객체 생성

@app.route('/') # IP만 가지고 접속하면 다음 함수 출력
def Hello_World():
	print("Hello World!")

if __name__ == "__main__":
  app.run(host="0.0.0.0", port="8800", debug=True)
