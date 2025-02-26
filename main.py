import requests

BASE_URL = "https://api.github.com"

def get_user_repos(username):
    url = f"{BASE_URL}/users/{username}/repos?per_page=100"
    repos = []
    response = requests.get(url, headers={
        "Accept":"application/vnd.github+json",
        "Authorization": "Bearer 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"

    })

    if response.status_code == 200:
        #print(f"Length {len(response.json())}")
        return response.json()  #repos = response.json()

    #get_total_forks_user_repos(repos)



def get_total_forks(repos):
    total_forks = 0
    #repos = get_user_repos(username)
    print(f"repos {repos}")
    for repo in repos:
        total_forks += repo["forks_count"]
        
    print(f"total_forks {total_forks}")

def get_total_commits(username):
    total_commits = 0
    repos = get_user_repos(username)
    print(f"repos {repos}")
    for repo in repos:
        url = f"{BASE_URL}/repos/{username}/{repo['name']}/commits"
        response = requests.get(url, headers={
        "Accept":"application/vnd.github+json",
        "Authorization": "Bearer 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"

        })

        if response.status_code == 200:
            total_commits += len(response.json())
        
    print(f"total_commits {total_commits}")   

def get_total_releases(username):
    total_releases = 0
    repos = get_user_repos(username)
    print(f"repos {repos}")
    for repo in repos:
        url = f"{BASE_URL}/repos/{username}/{repo['name']}/releases"
        response = requests.get(url, headers={
        "Accept":"application/vnd.github+json",
        "Authorization": "Bearer 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"

        })

        if response.status_code == 200:
            total_releases += len(response.json())
        
    print(f"total_releases {total_releases}")   

def get_total_branches(username):
    total_branches = 0
    repos = get_user_repos(username)
    print(f"repos {repos}")
    for repo in repos:
        url = f"{BASE_URL}/repos/{username}/{repo['name']}/branches"
        response = requests.get(url, headers={
        "Accept":"application/vnd.github+json",
        "Authorization": "Bearer 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"

        })

        if response.status_code == 200:
            total_branches += len(response.json())
        
    print(f"total_branches {total_branches}")  

def get_total_stars(username):
    total_stars = 0
    repos = get_user_repos(username)
    print(f"repos {repos}")
    for repo in repos:
        url = f"{BASE_URL}/repos/{username}/{repo['name']}/stargazers"
        response = requests.get(url, headers={
        "Accept":"application/vnd.github+json",
        "Authorization": "Bearer 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"

        })

        if response.status_code == 200:
            total_stars += len(response.json())
        
    print(f"total_stars {total_stars}")  


if __name__=='__main__':
   get_user_repos("kaggle")
   get_total_stars("kaggle")
   