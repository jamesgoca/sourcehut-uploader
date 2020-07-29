import requests, os
from dotenv import load_dotenv

load_dotenv()

authentication = { "Authorization": "token {}".format(os.getenv("sourcehut_api_key")) }

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