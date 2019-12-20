from flask import Flask, render_template, request
from decouple import config
import requests

app = Flask(__name__)

token =config("TELEGRAM_BOT_TOKEN")
chat_id =config("CHAT_ID")


url = "http://api.telegram.org/bot"


@app.route('/')
def hello():
    return ('hi')


@app.route('/write')
def write(): 
    return render_template('write.html')

@app.route('/send')
def send():
    text = request.args.get('text')
    requests.get(f'{url}{token}/sendmessage?chat_id={chat_id}&text={text}')
    return render_template('send.html')

@app.route(f'/{token}', methods=["POST"])
def telegram():
    chat_id = request.get_json.[][][] #나에게 메세지를 보낸 상대방의 아이디를 입력하는 방법. 
    if text == "로또"
    return "ok", 200  #웹에게 잘 전송했다는 뜻 한 번의 메세지에 한 번의 응답.  200이 안되어있으면 똑같은 메세지가 계속 보내지게 됨.


if __name__ == ("__main__"):
    app.run(debug=True)
