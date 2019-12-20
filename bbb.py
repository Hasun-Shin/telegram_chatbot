import http.client

conn = http.client.HTTPSConnection("api.themoviedb.org")

payload = "{\"username\":\"hahahasony\",\"password\":\"tlsgktjs93\",\"request_token\":\"f5b43f6b24b65645a474b8ce4512c0e538fe4865\"}"

headers = { 'content-type': "application/json" }

conn.request("POST", "/3/authentication/token/validate_with_login?api_key=b25f90dff294de0f547a2e5dda41f3e4", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))