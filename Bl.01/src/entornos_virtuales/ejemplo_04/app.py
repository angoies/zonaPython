import requests

URL = "https://www.uca.es" # "https://www.uca.es/noexiste"
res = requests.get(URL)

print(res)
print(res.headers)
#print(res.text)