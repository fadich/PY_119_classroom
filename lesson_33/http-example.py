import requests


url2 = "https://www.binance.com/"

server_url = "https://api4.binance.com"
api_v3_url = f"{server_url}/api/v3"

url = f'{api_v3_url}/ticker/24hr'
response = requests.post(url)

jsonresp = response.json()

print(response.headers)
print(type(jsonresp))
print(jsonresp[0]["symbol"])

with open("response_json.json", "w") as file:
    file.write(response.text)
