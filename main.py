import os
import requests
import math
from fpdf import FPDF
from dotenv import load_dotenv
import statistics

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
    get_total_stars(pdf,repos,username)
    get_total_commits(pdf,repos,username)
    get_total_branches(pdf, repos, username)
    get_total_releases(pdf,repos,username)
    get_total_closed_issues(pdf,repos, username)
    get_total_contributors(pdf, repos, username)
    get_total_environments(pdf, repos, username)
    get_total_tags(pdf, repos, username)
    get_code_lines_per_language(pdf,repos,username)
    pdf.output("github_stats.pdf")



def get_total_forks(pdf, repos):
    data = "forks"
    total_forks = 0
    forks_counts = []
    
    for repo in repos:
        total_forks += repo["forks_count"]
        forks_counts.append(repo["forks_count"])
    print(f"forks counts {forks_counts}")    
    forks_counts = sorted(forks_counts)
    print(f"sorted forks counts {forks_counts}")
    median = statistics.median(forks_counts) if forks_counts else 0 
    add_text(pdf,data, total_forks, median)    
    print(f"total_forks {total_forks} Median {median}")


def get_total_stars(pdf, repos, username):
    data = "stars"
    total_stars = 0
    stars_counts = []

    for repo in repos:
        total_stars += repo["stargazers_count"]
        stars_counts.append(repo["stargazers_count"])
    print(f"stars counts {stars_counts}")    
    stars_counts = sorted(stars_counts)
    print(f"sorted stars counts {stars_counts}")
    median = statistics.median(stars_counts) if stars_counts else 0 
    add_text(pdf,data, total_stars, median)    
    print(f"total_stars {total_stars} Median {median}")


def get_total_commits(pdf, repos, username):
    data = "commits"
    commits_count = []
    total_commits = 0
    
    for repo in repos:
        repo_commits = 0
        page = 1
        
        while True:
            url = f"{BASE_URL}/repos/{username}/{repo['name']}/commits?per_page=30&page={page}"
            response = requests.get(url, headers=getHeaders())

            if response.status_code != 200:
                print(f"Failed to fetch commits for {repo['name']}")
                break

            commits = response.json()
            commit_len = len(commits)  # Store the length of commits in a variable

            if commit_len == 0:  # Exit the loop early if no commits are found
                break

            repo_commits += commit_len
            total_commits += commit_len
            page += 1  

        commits_count.append(repo_commits)
    commits_count = sorted(commits_count)
    median = statistics.median(commits_count)
    add_text(pdf, data, total_commits, median)    
    print(f"Total commits: {total_commits}, Median commits: {median}")  

def get_total_releases(pdf, repos, username):
    data = "releases"
    releases_count = []
    total_releases = 0
    
    for repo in repos:
        repo_releases = 0
        page = 1
        
        while True:
            url = f"{BASE_URL}/repos/{username}/{repo['name']}/releases?per_page=100&page={page}"
            response = requests.get(url, headers=getHeaders())

            if response.status_code != 200:
                print(f"Failed to fetch releases for {repo['name']}")
                break

            releases = response.json()
            release_len = len(releases)  

            if release_len == 0:  
                break

            repo_releases += release_len
            total_releases += release_len
            page += 1

        releases_count.append(repo_releases)

    releases_count = sorted(releases_count)
    median = statistics.median(releases_count)
    add_text(pdf, data, total_releases, median)
    print(f"Total releases: {total_releases}, Median releases: {median}")  


def get_total_branches(pdf, repos, username):
    total_branches = 0
    data = "branches"
    branches = []

    for repo in repos:
        repo_branches = 0
        page = 1  
        
        while True:
            url = f"{BASE_URL}/repos/{username}/{repo['name']}/branches?per_page=100&page={page}"
            response = requests.get(url, headers=getHeaders())

            if response.status_code != 200:
                print(f"Failed to fetch branches for {repo['name']}")
                break

            branch_data = response.json()
            if not branch_data:  
                break  

            branches_count = len(branch_data)
            repo_branches += branches_count
            total_branches += branches_count
            page += 1 

        if repo_branches > 0:  
            branches.append(repo_branches)

    branches = sorted(branches)
    median = statistics.median(branches) if branches else 0

    add_text(pdf, data, total_branches, median)
    print(f"Total branches: {total_branches}, Median branches: {median}")
 

def get_total_closed_issues(pdf, repos, username):
    total_closed_issues = 0
    closed_issues = []
    data = "closed_issues"

    for repo in repos:
        repo_closed_issues = 0
        page = 1 

        while True:
            url = f"{BASE_URL}/repos/{username}/{repo['name']}/issues"
            response = requests.get(url, headers=getHeaders(), params={
                "state": "closed",
                "per_page": 100,
                "page": page
            })

            if response.status_code != 200:
                print(f"Failed to fetch closed issues for {repo['name']}")
                break

            issues = response.json()
            if not issues:  
                break  

            issues_count = len(issues)
            repo_closed_issues += issues_count
            total_closed_issues += issues_count
            page += 1 

        if repo_closed_issues > 0:  
            closed_issues.append(repo_closed_issues)

    closed_issues = sorted(closed_issues)
    median = statistics.median(closed_issues) if closed_issues else 0

    add_text(pdf, data, total_closed_issues, median)
    print(f"Total closed issues: {total_closed_issues}, Median closed issues: {median}")



def get_total_contributors(pdf, repos, username):
    total_contributors = 0
    data = "contributors"
    contributors = []

    for repo in repos:
        repo_contributors = 0
        page = 1  

        while True:
            url = f"{BASE_URL}/repos/{username}/{repo['name']}/contributors"
            response = requests.get(url, headers=getHeaders(), params={
                "per_page": 100,
                "page": page
            })

            if response.status_code != 200:
                print(f"Failed to fetch contributors for {repo['name']}")
                break

            contributors_data = response.json()
            if not contributors_data:  
                break  

            repo_contributors += len(contributors_data)
            total_contributors += len(contributors_data)
            page += 1 

        if repo_contributors > 0:  
            contributors.append(repo_contributors)

    contributors = sorted(contributors)
    median = statistics.median(contributors) if contributors else 0

    add_text(pdf, data, total_contributors, median)
    print(f"Total contributors: {total_contributors}, Median contributors: {median}")   

def get_total_environments(pdf, repos, username):
    data = "environments"
    total_environments = 0
    env_count = []

    for repo in repos:
        url = f"{BASE_URL}/repos/{username}/{repo['name']}/environments"
        response = requests.get(url, headers=getHeaders())

        if response.status_code == 200:
            print(f"Environment ${response.json()}")
            repo_envs = response.json().get("environments", [])
            env_count.append(len(repo_envs))
            total_environments += len(repo_envs)

    median_envs = statistics.median(env_count) if env_count else 0
    add_text(pdf, data, total_environments, median_envs)
    print(f"Total environments: {total_environments}, Median environments: {median_envs}")

def get_total_tags(pdf, repos, username):
    data = "tags"
    total_tags = 0
    tags_count = []

    for repo in repos:
        repo_tags = 0
        page = 1

        while True:
            url = f"{BASE_URL}/repos/{username}/{repo['name']}/tags?per_page=100&page={page}"
            response = requests.get(url, headers=getHeaders())

            if response.status_code != 200:
                print(f"Failed to fetch tags for {repo['name']}")
                break

            tags = response.json()
            if not tags:
                break  

            repo_tags += len(tags)
            total_tags += len(tags)
            page += 1  

        tags_count.append(repo_tags)

    
    median = statistics.median(tags_count) if tags_count else 0

    add_text(pdf, data, total_tags, median)
    print(f"Total tags: {total_tags}, Median tags: {median}")

def get_code_lines_per_language(pdf, repos, username):
    language_stats = {}

    for repo in repos:
        url = f"{BASE_URL}/repos/{username}/{repo['name']}/languages"
        response = requests.get(url, headers=getHeaders())

        if response.status_code == 200:
            languages = response.json()
            

            for lang, lines in languages.items():
                if lang not in language_stats:
                    language_stats[lang] = []
                language_stats[lang].append(lines)

    
    for lang, lines_list in language_stats.items():
        total = sum(lines_list)
        median = statistics.median(lines_list) if lines_list else 0
        data = lang 
        add_text(pdf,data, total,median)
        


if __name__=='__main__':
   username = input("Enter Github Username: ").strip()
   get_user_repos(username)
   