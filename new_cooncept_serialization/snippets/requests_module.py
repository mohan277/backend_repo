import requests

url = 'http://localhost:8000/snippets/all/'
response = requests.get(url=url, headers={'Content-type': 'application/json'})
print(response.content)