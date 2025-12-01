# commitgen

AI-powered Git commit message generator using Google Gemini.

Analyzes your staged changes and generates meaningful commit messages following [Conventional Commits](https://www.conventionalcommits.org/) format.

## Features

- Generates both **summary** and **description** for commits
- Follows Conventional Commits format (`feat`, `fix`, `docs`, etc.)
- Uses recent commit history to match your project's style
- Powered by Google Gemini API

## Installation

### Using pipx (recommended)
```bash
pipx install git+https://github.com/levish0/commitgen.git
```

### Using uv
```bash
uv tool install git+https://github.com/levish0/commitgen.git
```

### From source
```bash
git clone https://github.com/levish0/commitgen.git
cd commitgen
uv sync
```

## Setup

1. Get a Gemini API key from [Google AI Studio](https://aistudio.google.com/)

2. Create a `.env` file in your project directory:
```bash
echo "GEMINI_API_KEY=your_api_key_here" > .env
```

## Usage

```bash
# Stage your changes
git add .

# Generate commit message
commitgen
```

### Options

```bash
commitgen --help

Options:
  -n, --context-depth INTEGER  Number of recent commits to use as context (default: 5)
  --help                       Show this message and exit.
```

## Example Output

```
==================================================
SUMMARY: feat(auth): add email validation for login

DESCRIPTION:
- Add regex-based email format validation
- Display user-friendly error messages
- Prevents invalid emails from reaching the API
==================================================
```

## License

MIT
