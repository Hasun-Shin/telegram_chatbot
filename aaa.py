import requests

url = "https://api.themoviedb.org/3/authentication/session/new"

payload = "{\"request_token\":\"f5b43f6b24b65645a474b8ce4512c0e538fe4865\"}"
headers = {'content-type': 'application/json'}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)




import http.client

conn = http.client.HTTPSConnection("api.themoviedb.org")

payload = "{\"request_token\":\"f5b43f6b24b65645a474b8ce4512c0e538fe4865\"}"

headers = { 'content-type': "application/json" }

conn.request("POST", "/3/authentication/session/new?api_key=b25f90dff294de0f547a2e5dda41f3e4", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))