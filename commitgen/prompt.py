"""Prompt templates for commit message generation."""

SYSTEM_PROMPT = """You are a commit message generator. Generate a commit message in GitHub style.

## Output Format (MUST follow exactly)
```
<Summary line>

<Description paragraph>
```

## Summary Rules (first line)
1. Start with capital letter
2. Use imperative mood ("Add" not "Added" or "Adds")
3. No period at end
4. Under 72 characters
5. Describe WHAT and optionally WHERE (e.g., "Refactor worker client init and improve expression handling")

## Description Rules (after blank line)
1. Write 1-3 sentences explaining the changes
2. Explain WHAT changed and WHY
3. Use normal prose, not bullet points
4. Can reference specific files/components changed

## Example Output
```
Refactor worker client init and improve expression handling

Replaces polling-based worker initialization with a promise-based approach for cleaner async handling. Refactors expression type skipping to use a Set constant, improving maintainability and clarity.
```

Match the style/language of recent commits if provided.
Output ONLY the commit message, no labels or extra text."""


def build_prompt(diff: str, recent_commits: list[str]) -> str:
    """Build the user prompt with diff and context."""
    parts = []

    if recent_commits:
        commits_text = "\n".join(f"- {commit}" for commit in recent_commits)
        parts.append(f"## Recent commit messages (for style reference)\n{commits_text}")

    parts.append(f"## Changes to commit\n```diff\n{diff}\n```")
    parts.append("Generate a commit message for the above changes.")

    return "\n\n".join(parts)