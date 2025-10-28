# requests para requisições HTTP
# Tutorial -> https://youtu.be/Qd8JT0bnJGs
# requirements: pip install requests
# requests é uma biblioteca externa para fazer requisições HTTP de forma simples e eficiente.
import requests

# http:// -> 80
# https:// -> 443
url = 'http://localhost:8000/'
response = requests.get(url)

print(response.status_code)
# print(response.headers)
# print(response.content)
# print(response.json())
print(response.text)