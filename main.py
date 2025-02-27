import os
import requests
import math
from fpdf import FPDF
from dotenv import load_dotenv

#load .env file
load_dotenv()

BASE_URL = "https://api.github.com"

def getHeaders():
    token = os.getenv("GITHUB_TOKEN")
    
    return {
        "Accept":"application/vnd.github+json",
        "Authorization": f"Bearer {token}"

     }

def add_text(pdf, data, total, median):
    pdf.set_font('Arial', '', 14)
    pdf.cell(40, 10, f"Total number of {data}: {total}", border = 0, ln = 1, align = '', fill = False, link = '')
    pdf.cell(40, 10, f"Median number of {data}: {median}", border = 0, ln = 1, align = '', fill = False, link = '')

def get_user_repos(username):
    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()
    pdf.set_margins(0, 0, 0)
    pdf.set_font('Arial', 'B', 20)
    pdf.cell(40, 10, "Github Stats", border = 0, ln = 1, align = '', fill = False, link = '')
    pdf.set_font('Arial', '', 14)
    pdf.cell(40, 10, f"Owner: {username}", border = 0, ln = 1, align = '', fill = False, link = '')
    
    url = f"{BASE_URL}/users/{username}/repos?per_page=100"
    repos = []
    response = requests.get(url, headers=getHeaders())

    if response.status_code == 200:
        #print(f"Length {len(response.json())}")
        repos = response.json()
        

    get_total_forks(pdf,repos)
    get_total_commits(pdf,repos,username)
    get_total_branches(pdf, repos, username)
    get_total_releases(pdf,repos,username)
    get_total_stars(pdf,repos,username),
    get_total_closed_issues(pdf,repos, username)
    pdf.output("github_stats.pdf")



def get_total_forks(pdf, repos):
    data = "forks"
    total_forks = 0
    repos_length = len(repos)
    print(f"repos {repos}")
    for repo in repos:
        total_forks += repo["forks_count"]
    
    median = math.floor(total_forks/repos_length)
    add_text(pdf,data, total_forks, median)    
    print(f"total_forks {total_forks}")

def get_total_commits(pdf, repos, username):
    data = "commits"
    repos_length = len(repos)
    total_commits = 0
    print(f"repos {repos}")
    for repo in repos:
        url = f"{BASE_URL}/repos/{username}/{repo['name']}/commits?per_page=100"
        response = requests.get(url, headers=getHeaders())

        if response.status_code == 200:
            total_commits += len(response.json())

    median = math.floor(total_commits/repos_length)
    add_text(pdf,data, total_commits, median)    
    print(f"total_commits {total_commits}")   

def get_total_releases(pdf, repos, username):
    data = "releases"
    repos_length = len(repos)
    total_releases = 0
    
    print(f"repos {repos}")
    for repo in repos:
        url = f"{BASE_URL}/repos/{username}/{repo['name']}/releases?per_paage=100"
        response = requests.get(url, headers= getHeaders()
        )

        if response.status_code == 200:
            total_releases += len(response.json())
    
    median = math.floor(total_releases/repos_length)
    add_text(pdf,data, total_releases, median)
    print(f"total_releases {total_releases}")   

def get_total_branches(pdf,repos, username):
    total_branches = 0
    data = "branches"
    repos_length = len(repos)

    print(f"repos {repos}")
    for repo in repos:
        url = f"{BASE_URL}/repos/{username}/{repo['name']}/branches?per_page=100"
        response = requests.get(url, headers=getHeaders()
        )

        if response.status_code == 200:
            total_branches += len(response.json())

    median = math.floor(total_branches/repos_length)
    add_text(pdf,data, total_branches, median)     
    print(f"total_branches {total_branches}")  

def get_total_stars(pdf, repos, username):
    total_stars = 0
    data = "branches"
    repos_length = len(repos)
    
    print(f"repos {repos}")
    for repo in repos:
        url = f"{BASE_URL}/repos/{username}/{repo['name']}/stargazers?per_page=100"
        response = requests.get(url, headers=getHeaders()
        )

        if response.status_code == 200:
            total_stars += len(response.json())

    median = math.floor(total_stars/repos_length)
    add_text(pdf,data, total_stars, median)     
    print(f"total_stars {total_stars}")  

def get_total_closed_issues(pdf, repos,username):
    total_closed_issues = 0
    data = "closed_issues"
    repos_length = len(repos)
    for repo in repos:
        url = f"{BASE_URL}/repos/{username}/{repo['name']}/issues"
        response = requests.get(url, headers=getHeaders(),
        params= {
            "state":"closed",
            "per_page": 100
        }
         )

        if response.status_code == 200:
            total_closed_issues += len(response.json())
    median = math.floor(total_closed_issues/repos_length)
    add_text(pdf,data, total_closed_issues, median)         
    print(f"total_issues {total_closed_issues}")  
    


if __name__=='__main__':
   get_user_repos("kaggle")
   