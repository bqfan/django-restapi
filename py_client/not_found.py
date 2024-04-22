import requests


endpoint = "http://localhost:8000/api/products/123456789/"

get_response = requests.get(endpoint)

print(get_response.json())
