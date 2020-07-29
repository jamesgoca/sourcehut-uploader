import requests
import os
import logging
import sourcehut
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(filename="app.log", level=logging.DEBUG)

repos = sourcehut.initialize()

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
			repo_url, new_url, folder = sourcehut.get_urls(r)

			sourcehut.check_for_repo_on_sourcehut(r)

			if os.path.isdir(folder):
				if clone_new == True:
					logging.debug("The repository {} exists. Skipping creation.".format(new_url))
					print("The repository {} exists. Skipping creation.".format(new_url))
				else:
					sourcehut.retrieve_code_from_original(repo_url, new_url, folder)
					logging.debug("Repository {} has been updated and uploaded to sourcehut.".format(r["name"]))
					print("Repository {} has been updated and uploaded to sourcehut.".format(r["name"]))
			else:
				if clone_new == True:
					logging.debug("The repository {} does not exist in your local working directory. Creating.".format(new_url))
					os.system("git clone --bare " + repo_url + " >/dev/null 2>&1")
					sourcehut.retrieve_code_from_original(repo_url, new_url, folder)
					print("Repository {} has been created and uploaded to sourcehut.".format(r["name"]))
					logging.debug("Repository {} has been created and uploaded to sourcehut.".format(r["name"]))
				else:
					logging.debug("The repository {} does not exist in your local working directory. Skipping.".format(new_url))

if __name__ == "__main__":
	create_repos()
	print("Uploading completed.")
