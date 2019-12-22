# 텔레그램 쳇봇만들기 

>https://core.telegram.org/bots/api#authorizing-your-bot



1. 텔레그램 설치
2. @Botfather 찾아서 /newbot 입력
3. 이름 설정 
4. bot 이름 다시 추가 
5. 토큰 번호가 생성되는데, 이건 절대 다른 사람에게 공개하면 안됨. 
6. 내 이름의 bot 을 검색하여 채팅 시작함. /start
7. app.py 생성함

```python
from flask import flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World"
    

if __name__ == ("__main__"):
    app.run(debug=True)
```



8. 검색창에 입력 : https://api.telegram.org/bot토큰주소/getMe 

결과 잘 보려면 JSON 뷰어 프로그램 깔기. (구글 앱스토어)

```json
{
"ok": true,
"result": {
"id": 숫자들,
"is_bot": true,
"first_name": "hasony",
"username": "hasunny_bot"
}
}
```



카톡에는 재전송 버튼이 있음.

텔레그램은 상대방에게 갈때까지 계속 보냄. 



9. 챗봇에게 말을 걸어봄.

말을 걸면 챗봇의 변화가 생김. 그 변화를 보려면 getUpdates 를 이용한다.

검색창 입력 : https://api.telegram.org/bot토큰주소/getUpdates

결과 창으로부터 내 계정 아이디 (bot 말고 사람) 아이디 메모장에 복사해 놓음. 

내 계정 아이디도 다른 사람한테 보여지면 안됨. 



10. sendMassege

    [https://api.telegram.org/bot1047012805:AAGFsYHyS4-FE32dNveHMiWW84fdkmKTWGs/sendMessage?chat_id=내 아이디 숫자&text=%EC%95%88%EB%85%95%ED%95%98%EC%84%B8%EC%9A%94](https://api.telegram.org/bot1047012805:AAGFsYHyS4-FE32dNveHMiWW84fdkmKTWGs/sendMessage?chat_id=993919931&text=안녕하세요)



## 토큰과 쳇아이디 숨기는 방법

1. `pip install python-decouple`

2. 파이썬 파일 상단에 `from decouple import config`

3. .env 파일 생성 및 입력

   CHAT_ID=""
   TELEGRAM_BOT_TOKEN =""

4.  ```python
   from flask import Flask
   from decouple import config
   
   app = Flask(__name__)
   
   token =config("TELEGRAM_BOT_TOKEN")
   chat_id =config("CHAT_ID")
   ```

-----------------------------

## app.py 코드

```python
from flask import Flask, render_template, request
from decouple import config
import requests

app = Flask(__name__)

#token 은 나의 bot id
#chat_id 는 나(사람)의 id
token =config("TELEGRAM_BOT_TOKEN") #.env 파일에 있는 변수 . 내 정보를 숨겨줌. 
chat_id =config("CHAT_ID") #.env 파일에 있는 변수 


url = "http://api.telegram.org/bot"


@app.route('/')
def hello():
    return ('hi')


@app.route('/write')
def write():
    return render_template('write.html')

@app.route('/send')
def send():
    text = request.args.get('text') #'text' 는 write.html 의 name! 요청하기
    requests.get(f'{url}{token}/sendmessage?chat_id={chat_id}&text={text}') # 요청한 것에 대한 응답받기 
    return render_template('send.html')


if __name__ == ("__main__"):
    app.run(debug=True)

```

## write.html 코드

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <form action="/send">
        <input type ="text" name="text">
        <input type ="submit" value="메세지 보내기">
    </form>
</body>
</html>
```

-----------------

## git ignore 후에 git hub 에 올리기

1. git init : 현재 작업하고 있는 telegram_chatbot 폴더

2. git hub에 새 저장소 생성(telegram_chatbot)

3. git ignore.io  홈페이지에서 windows, Flask, Python, (가상환경작동하고 있으면)venv, visualstudiocode. 를 입력한다

4. 코드를 vs code 에 복붙 하여 저장한다.



---------------------

## Webhook 설치

1. ngrok 설치

https://ngrok.com/

2. window cmd 에서 `ngrok http  5000` 입력

3. 출력된 결과 중 https 주소 복사함.

```python
from decouple import config
import requests

token = config("TELEGRAM_BOT_TOKEN")
url = "https://api.telegram.org/bot"
ngrok url = "https://041207d2.ngrok.io"

data = requests.get(f'{url}{token}/setwebhook?url={ngrok_url}/{token}')

print(data)
```



## 챗봇과 대화나누기

### (1) 내 말 따라하기

```python
from flask import Flask, render_template, request
from decouple import config
import random
import requests

app = Flask(__name__)

token =config("TELEGRAM_BOT_TOKEN")
chat_id =config("CHAT_ID")

url = "http://api.telegram.org/bot"


@app.route(f'/{token}', methods=["POST"])
def telegram():
    data = request.get_json()
    chat_id = data['message']['chat']['id']
    text = data['message']['text']

    requests.get(f'{url}{token}/sendmessage?chat_id={chat_id}&text={text}')
    
    return "ok", 200  #웹에게 잘 전송했다는 뜻 한 번의 메세지에 한 번의 응답.  200이 안되어있으면 똑같은 메세지가 계속 보내지게 됨.
    
    
    

if __name__ == ("__main__"):
    app.run(debug=True)

```





### (2) 로또 번호 묻고 대답하기

```python
from flask import Flask, render_template, request
from decouple import config
import random
import requests

app = Flask(__name__)

token =config("TELEGRAM_BOT_TOKEN")
chat_id =config("CHAT_ID")

url = "http://api.telegram.org/bot"


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
```



### 최종적인 종합 코드

```python
#최종으로 처음부터 끝까지 포함된 코드들 (write,로또,말 따라하기 다 포함)

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

```

