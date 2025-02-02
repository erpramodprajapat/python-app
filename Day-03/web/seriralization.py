import requests,json

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
users = response.json()  # Directly parse JSON response

# Memory serialization
data = json.dumps(users, indent=2)
#print(data)  # Optional, to verify output

# File-level serialization (saving JSON properly)
with open("users.json", "w") as fw:
    json.dump(users, fw, indent=2)  # Write actual JSON, not string

with open("users.json",'r') as fr:
    data=json.load(fr)
    print(data)