# GITHUB REPOSITORY STATISTICS

The **GitHub Repository Statistics** tool is a Python-based solution designed to provide in-depth analysis of GitHub repositories. It efficiently gathers and presents key repository metrics, making it an invaluable resource for evaluating repository activity and engagement using the (Github Api)[https://docs.github.com].

This tool offers comprehensive insights by calculating the total and median counts of essential repository elements, including:

- Forks
- Stars
- Contributors
- Commits
- Branches
- Releases
- Closed issues
- Tags
- Environments
- Source code lines per programming language

  By leveraging this tool, developers and analysts can easily assess repository health, activity trends, and community involvement. 

---

## Installation

### Prerequisites


- Python 3.8 or higher.

### Clone the Repository

```
git clone https://github.com/nanya01/github_repository_statistics.git
```

Create a Virtual Environment (Recommended)
```
python -m venv venv

source venv/bin/activate  # For macOS/Linux

venv\Scripts\activate     # For Windows
```

Install all dependencies using:

```
pip install -r requirements.txt
```

Generate Github Personal Token (PAT)

To generate Github Personal token Click on [Github Apps](https://github.com/settings/personal-access-tokens)

1 Go to GitHub Token Settings:
-  GitHub Personal Access Tokens

2️ Click "Generate new token" (or "Generate new token (classic)").

3️ Select "All Repositories".

4️ Grant the following permissions (at minimum):
   -  Read access to administration
   - Read access to code
   - Read access to metadata
     
5️ Click "Generate token" and copy it immediately.

⚠️ You won’t be able to see it again after you leave the page!

6️ Create a .env file in the project directory and paste the token.


---

## Usages
Use the command-line to run the program
```
python main.py
```

Output Example

PDF Report: github_stats.pdf



---

