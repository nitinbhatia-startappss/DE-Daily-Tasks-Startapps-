import requests

url = "https://api.github.com/users/torvalds"

response = requests.get(url)

if response.status_code == 200:
    print("Success", response.status_code)
    data = response.json()
else:
    print("Error", response.status_code)

print("Username : ",data["login"])
print("Name : ", data["name"])
print("Followers : ", data["followers"])
print("Repos : ", data["public_repos"])

