from decouple import config
import requests

token = config("TELEGRAM_BOT_TOKEN")
url = "http://api.telegram/org/bot"
ngrok_url = "https://ee7c05b6.ngrok.io"


data = requests.get(f'{url}{token}/setwebhook?url={ngrok_url}/{token}')
print(data)