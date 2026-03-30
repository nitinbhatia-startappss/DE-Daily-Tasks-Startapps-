import requests

url = "https://api.github.com/users/torvalds/repos"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    sorted_repos = sorted(data, key=lambda repo: repo["stargazers_count"], reverse=True)

    for star in sorted_repos:
        if star["stargazers_count"] > 0:
            print("Stargazers_count:", star["stargazers_count"], "| Repo:", star["name"], "| Language:", star["language"])
else:
    print("Error")
        