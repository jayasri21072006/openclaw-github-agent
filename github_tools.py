import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("GITHUB_TOKEN")
OWNER = os.getenv("OWNER")
REPO = os.getenv("REPO")

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json"
}


def list_issues():
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/issues"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return [
            {
                "number": i["number"],
                "title": i["title"],
                "state": i["state"]
            }
            for i in response.json()
        ]
    return {"error": response.text}


def create_issue(title, body):
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/issues"
    data = {"title": title, "body": body}

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 201:
        res = response.json()
        return {
            "message": "Issue created",
            "url": res["html_url"]
        }
    return {"error": response.text}


def list_pr_comments(pr_number):
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/issues/{pr_number}/comments"

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return [
            {
                "user": c["user"]["login"],
                "body": c["body"]
            }
            for c in response.json()
        ]
    return {"error": response.text}


def create_pr_comment(pr_number, comment_text):
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/issues/{pr_number}/comments"

    data = {"body": comment_text}

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 201:
        return {"message": "Comment added"}
    return {"error": response.text}