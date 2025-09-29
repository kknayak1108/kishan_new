import requests

# url = "https://api.github.com/users/philips-software/repos"
url = "https://api.github.com/users/Netflix/repos"
 
github_repos = []
page = 1
 
while True:
    # Fetch 100 repos at a time (maximum allowed)
    response = requests.get(url, params={"per_page": 100, "page": page})
    data = response.json()
   
    if not data:  # no more repos
        break
   
    for item in data:
        github_repos.append(item["name"])
   
    page += 1
 
# Print all repos
for repo in github_repos:
    print(repo)
