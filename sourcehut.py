import requests, os
from dotenv import load_dotenv

load_dotenv()

authentication = { "Authorization": "token {}".format(os.getenv("sourcehut_api_key")) }

def initialize():
	cwd = os.getcwd()
	repos_folder = os.path.join(cwd, "repos")

	if os.path.isdir(repos_folder):
		os.chdir(repos_folder)
	else:
		os.mkdir(repos_folder)
		os.chdir(repos_folder)

	repos_raw = requests.get("https://api.github.com/users/{}/repos".format(os.getenv("github_username")))

	repos = repos_raw.json()

	return repos

def create_new_repository(repo):
	print(repo["private"])
	data = {
		"name": repo["name"],
		"description": repo["description"],
		"visibility": "public" if repo["private"] == False else "private"
	}

	create_repo = requests.post("https://git.sr.ht/api/repos", data = data, headers = authentication)

def check_for_repo_on_sourcehut(repo):
	check_for_repo = requests.get("https://git.sr.ht/api/repos/" + repo["name"], headers = authentication)
	if check_for_repo.status_code == 404:
		create_new_repository(repo)
	else:
		pass

def retrieve_code_from_original(repo_url, new_url, folder):
	os.chdir(folder)
	os.system("git push --mirror " + new_url + " >/dev/null 2>&1")

	os.chdir("..")

def get_urls(r):
	repo_url = "https://github.com/" + os.getenv("github_username") + "/" + r["name"]
	new_url = "git@git.sr.ht:~" + os.getenv("sourcehut_username") + "/" + r["name"]
	folder = r["name"] + ".git/"

	return repo_url, new_url, folder