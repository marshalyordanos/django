import requests 

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "http://httpbin.org"
endpoint = 'http://127.0.0.1:8000/api'

res = requests.get(endpoint,params={"abc":123},json={"query":"hello"})

# print(res.text)
print(res.text)
# print(res.json())
print("****************************")
print(res.headers['content-type'])
print(res.json())

print(res.status_code)


