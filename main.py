import requests

BASE_URL = "https://api.github.com"

def get_user_repos(username):
    url = f"{BASE_URL}/users/{username}/repos?per_page=100"

    response = requests.get(url, headers={
        "Accept":"application/vnd.github+json",
        "Authorization": "Bearer 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"

    })

    if response.status_code == 200:
        #print(f"Length {len(response.json())}")
        return response.json()


def get_total_forks_user_repos(username):
    total_forks = 0
    repos = get_user_repos(username)
    print(f"repos {repos}")
    for repo in repos:
        total_forks += repo["forks_count"]
        
    print(f"total_forks {total_forks}")

def get_total_commits_user_repos(username):
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
        
    print(f"total_forks {total_commits}")   


if __name__=='__main__':
   get_user_repos("kaggle")
   get_total_commits_user_repos("kaggle")