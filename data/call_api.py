import requests
import json

r = requests.get(url='https://data.nasa.gov/resource/y77d-th95.json').json()

data = json.dumps(r)
print(data)


with open('data.json', 'w') as f:
     json.dump(data, f)