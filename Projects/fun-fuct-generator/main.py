import requests
import json

url = "https://uselessfacts.jsph.pl/random.json?language=en"

request = requests.get(url)
response_data = json.loads(request.text)

fun_fact = response_data["text"]
print(fun_fact)
