import requests

url = "https://api.github.com/users/Nitin59295/repos"

response = requests.get(url)

if response.status_code == 200:
    print("Success", response.status_code)
    data = response.json()
    for repo in data:
        if repo["language"] != None:
            print("Repo: ",repo["name"], "Language: ", repo["language"])
else:
    print("Error")
