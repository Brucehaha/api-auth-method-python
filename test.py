import requests
import hashlib
import time

current_time = time.time()

data = {
    "name": "bruce",
    "age": 30,
}

auth_key = "456kbasdcy9lansdeeefasdfl.{004kk;"
# create dynamic key to post data
auth_time_key = "%s|%s"%(auth_key, current_time)

h = hashlib.md5()
h.update(bytes(auth_time_key, encoding="utf-8"))
h_key = "%s|%s"%(h.hexdigest(), current_time)
response = requests.post(
    url='http://127.0.0.1:8000/api',
    json=data,
    headers={
        'auth-key': h_key}
    )

print(response.text)