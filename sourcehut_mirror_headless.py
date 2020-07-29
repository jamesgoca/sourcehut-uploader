import logging
import sourcehut
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(filename="headless.log", level=logging.DEBUG)

repos = sourcehut.initialize()

def main():
	for r in repos:
		sourcehut.check_for_repo_on_sourcehut(r)
		if r["fork"] == False:
			repo_url, new_url, folder = sourcehut.get_urls(r)

			sourcehut.retrieve_code_from_original(repo_url, new_url, folder)
			logging.debug("Repository {} has been updated and uploaded to sourcehut.".format(r["name"]))

if __name__ == "__main__":
	main()
	print("Uploading completed.")