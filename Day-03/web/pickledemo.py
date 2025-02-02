import requests,json
import pickle

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
users = json.loads(response.text)

with open("C:\\py-tt\\Day-03\\web\\users.pkl",'bw') as fw:
    pickle.dump(users,fw)
    print("Binary ser. done !!")
