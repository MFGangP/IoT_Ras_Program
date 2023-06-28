from flask import Flask

app = Flask(__name__) # 객체 생성

@app.route('/') # IP만 가지고 접속하면 다음 함수 출력
def home():
	return "Flask Server Test"

@app.route('/user/<username>') # name 이라는 웹페이지에 username을 출력
def show_username(username):
    return "User : %s" % username

'''
@app.route('/user/<state>') # 이런 식으로 쓸 수 있다.
def show_username(state):
    if state == 'on':
        return "User : %s"
    elif state == 'off':
        return "User : %s"
'''

@app.route('/post/<int:post_id>') # name 이라는 웹페이지에 username을 출력
def show_post(post_id):
    return "User : %s" % post_id

if __name__ == "__main__":
	app.run(host="0.0.0.0", port="8800")

	
