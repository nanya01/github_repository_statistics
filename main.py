import requests

BASE_URL = "https://api.github.com"

def get_user_repos(username):
    url = f"{BASE_URL}/users/{username}/repos"

    response = requests.get(url, headers={
        "Accept":"application/vnd.github+json"
    })

    if response.status_code == 200:
        # print(f"Length {len(response.json())}")
        return response.json()


def get_total_forks_user_repos(username):
    #url = f"{BASE_URL}/repos/{username}/{repo}/forks"
    total_forks = 0
    repos = get_user_repos(username)
    print(f"repos {repos}")
    for repo in repos:
        total_forks += repo["forks_count"]
        #print(f"repo {repo["forks_count"]}")
        
    #print(f"total_forks {total_forks}")
    


if __name__=='__main__':
   get_user_repos("kaggle")
   get_total_forks_user_repos("kaggle")