import requests

url = "https://api.github.com/search/repositories"

params = {
    "q" : "language:python",
    "sort" : "stars",
    "per_page" : 5
}

response = requests.get(url, params = params)

if response.status_code == 200:
    print("Success", response.status_code)
    data = response.json()
    repos = data["items"]
    for repo in repos:
        print(repo["full_name"])
else:
    print("Error",response.status_code)

