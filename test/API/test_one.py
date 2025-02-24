import requests
import json
from jsonschema import validate

url = "https://reqres.in/api/users"

payload = {
  "name": "morpheus",
  "job": "leader"
}

def test():
  response = requests.post(url, data=payload)
  body = response.json()
  assert response.status_code == 201
  with open("../../post_users.json") as file:
    validate(body,schema=json.loads(file.read()))

