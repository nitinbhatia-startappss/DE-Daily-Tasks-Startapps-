import requests

url = "https://api.github.com/users/torvalds/repos"

response = requests.get(url)

if response.status_code == 200:
    print("Success", response.status_code)
    data = response.json()
    for stars in data:
        if stars["stargazers_count"] > 0:
            print("Stargazers_count: ", stars["stargazers_count"], "Repo_name: ",stars["name"],"Language: ", stars["language"])
else:
    print("Error")
