"""Gemini API client for commit message generation."""

import os

from dotenv import load_dotenv
from google import genai

from .prompt import SYSTEM_PROMPT

load_dotenv()


def get_client() -> genai.Client:
    """Get Gemini API client."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY not found. "
            "Please set it in .env file or as environment variable."
        )
    return genai.Client(api_key=api_key)


def generate_commit_message(user_prompt: str) -> str:
    """Generate commit message using Gemini API."""
    client = get_client()

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[
            {"role": "user", "parts": [{"text": SYSTEM_PROMPT}]},
            {"role": "model", "parts": [{"text": "I understand. I will generate commit messages following the Conventional Commits format."}]},
            {"role": "user", "parts": [{"text": user_prompt}]},
        ],
    )

    return response.text.strip()