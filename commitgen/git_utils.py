"""Git utility functions for commitgen."""

import subprocess


def run_git_command(args: list[str]) -> str:
    """Run a git command and return its output."""
    result = subprocess.run(
        ["git"] + args,
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout.strip()


def get_staged_diff() -> str:
    """Get the diff of staged changes."""
    return run_git_command(["diff", "--staged"])


def get_staged_files() -> list[str]:
    """Get list of staged files."""
    output = run_git_command(["diff", "--staged", "--name-only"])
    if not output:
        return []
    return output.split("\n")


def get_recent_commits(n: int = 5) -> list[str]:
    """Get the last n commit messages."""
    try:
        output = run_git_command(
            ["log", f"-{n}", "--pretty=format:%s"]
        )
        if not output:
            return []
        return output.split("\n")
    except subprocess.CalledProcessError:
        # No commits yet
        return []


def has_staged_changes() -> bool:
    """Check if there are any staged changes."""
    return bool(get_staged_diff())