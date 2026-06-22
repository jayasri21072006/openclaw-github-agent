# OpenClaw GitHub MCP Agent

A custom GitHub MCP (Model Context Protocol) server integrated with OpenClaw using Python and FastMCP.

## Features

* Fetch GitHub repository issues
* Create new GitHub issues
* Retrieve pull request comments
* Add comments to pull requests
* Integrate custom GitHub tools with OpenClaw

## Technologies Used

* Python
* FastMCP
* OpenClaw
* GitHub REST API
* Requests
* Python-dotenv

## MCP Tools

* `get_issues()` - Fetch all repository issues
* `add_issue(title, body)` - Create a new issue
* `get_pr_comments(pr_number)` - Retrieve comments from a pull request
* `add_pr_comment(pr_number, comment_text)` - Add a comment to a pull request

## Setup

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install the required dependencies.
4. Configure GitHub credentials in the `.env` file.
5. Run the MCP server.

## Run

```bash
python server.py
```

## Author

Jayasri
