from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="../.env")

github_token = os.getenv("GITHUB_TOKEN")

print(github_token)