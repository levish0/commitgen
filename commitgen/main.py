"""commitgen - AI-powered Git commit message generator."""

import click

from .ai_client import generate_commit_message
from .git_utils import get_recent_commits, get_staged_diff, get_staged_files, has_staged_changes
from .prompt import build_prompt


@click.command()
@click.option(
    "--context-depth",
    "-n",
    default=5,
    help="Number of recent commits to use as context (default: 5)",
)
def main(context_depth: int) -> None:
    """Generate AI-powered commit message for staged changes."""
    # Check for staged changes
    if not has_staged_changes():
        click.echo("No staged changes found.")
        click.echo("Stage your changes with: git add <files>")
        raise SystemExit(1)

    # Get git info
    staged_files = get_staged_files()
    click.echo(f"Analyzing {len(staged_files)} staged file(s)...")

    diff = get_staged_diff()
    recent_commits = get_recent_commits(context_depth)

    # Build prompt and generate
    user_prompt = build_prompt(diff, recent_commits)

    try:
        click.echo("Generating commit message...\n")
        message = generate_commit_message(user_prompt)

        # Parse and display the result
        click.echo("=" * 50)
        click.echo(message)
        click.echo("=" * 50)
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)
        raise SystemExit(1)
    except Exception as e:
        click.echo(f"Failed to generate commit message: {e}", err=True)
        raise SystemExit(1)


if __name__ == "__main__":
    main()