import requests
import os
import logging
import sourcehut
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(filename="app.log", level=logging.DEBUG)

cwd = os.getcwd()
repos_folder = os.path.join(cwd, "repos")

if os.path.isdir(repos_folder):
	os.chdir(repos_folder)
else:
	os.mkdir(repos_folder)
	os.chdir(repos_folder)

repos_raw = requests.get("https://api.github.com/users/jamesgoca/repos")

repos = repos_raw.json()

user_choice = input(
"""
Welcome to the sourcehut Uploader!

What would you like to do?

[1] Clone new repositories.
[2] Update existing repositories.
"""
)

if user_choice == "1":
	clone_new = True
elif user_choice == "2":
	clone_new = False
else:
	print("Please choose a valid option")

def create_repos():
	print("Uploading your projects. This may take a while.")
	for r in repos:
		if r["fork"] == False:
			repo_url = "https://github.com/" + os.getenv("github_username") + "/" + r["name"]
			new_url = "git@git.sr.ht:~" + os.getenv("sourcehut_username") + "/" + r["name"]
			folder = r["name"] + ".git/"

			sourcehut.check_for_repo_on_sourcehut(r)

			if os.path.isdir(folder):
				if clone_new == True:
					logging.debug("The repository {} exists. Skipping creation.".format(new_url))
				else:
					sourcehut.retrieve_code_from_original(repo_url, new_url, folder)
					logging.debug("Repository {} has been updated and uploaded to sourcehut.".format(r["name"]))
			else:
				if clone_new == True:
					logging.debug("The repository {} does not exist in your local working directory. Creating.".format(new_url))
					os.system("git clone --bare " + repo_url)
					sourcehut.retrieve_code_from_original(repo_url, new_url, folder)
					logging.debug("Repository {} has been created and uploaded to sourcehut.".format(r["name"]))
				else:
					logging.debug("The repository {} does not exist in your local working directory. Skipping.".format(new_url))

if __name__ == "__main__":
	create_repos()
	print("Uploading completed.")