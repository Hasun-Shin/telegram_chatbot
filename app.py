from flask import Flask, render_template, request
from decouple import config
import random
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
    data = request.get_json()
    chat_id = data['message']['chat']['id']
    text = data['message']['text']
    
    if text == "안녕":
        return_text = "안녕하세요"
    elif "로또" in text:
        numbers = range(1,46)
        return_text = sorted(random.sample(numbers, 6))
    
    
    else : 
        return_text = "지금 지원하는 채팅은 안녕입니다."
    
    
    requests.get(f'{url}{token}/sendmessage?chat_id={chat_id}&text={return_text}')
    return "ok", 200  #웹에게 잘 전송했다는 뜻 한 번의 메세지에 한 번의 응답.  200이 안되어있으면 똑같은 메세지가 계속 보내지게 됨.
    

if __name__ == ("__main__"):
    app.run(debug=True)
