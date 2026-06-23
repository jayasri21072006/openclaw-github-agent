from mcp.server.fastmcp import FastMCP
from github_tools import (
    list_issues,
    create_issue,
    list_pr_comments,
    create_pr_comment,
)

mcp = FastMCP("github-mcp")

@mcp.tool()
def list_repo_issues():
    """List issues from the configured GitHub repository."""
    return list_issues()

@mcp.tool()
def create_repo_issue(title: str, body: str):
    """Create a new issue in the configured GitHub repository."""
    return create_issue(title, body)

@mcp.tool()
def list_issue_comments(pr_number: int):
    """List comments on a GitHub issue or pull request."""
    return list_pr_comments(pr_number)

@mcp.tool()
def create_issue_comment(pr_number: int, comment_text: str):
    """Add a comment to a GitHub issue or pull request."""
    return create_pr_comment(pr_number, comment_text)

if __name__ == "__main__":
    mcp.run()