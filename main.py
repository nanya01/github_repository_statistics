import requests

BASE_URL = "https://api.github.com"

def get_user_repos(username):
    url = f"{BASE_URL}/users/{username}/repos"

    response = requests.get(url, headers={
        "Accept":"application/vnd.github+json"
    })

    if response.status_code == 200:
        print(response.json())
        print(f"Length {len(response.json())}")





if __name__=='__main__':
   get_user_repos("kaggle")