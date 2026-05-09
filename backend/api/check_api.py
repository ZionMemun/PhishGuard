# This file manually checks the email analysis API using sample .eml files.

from pathlib import Path

import requests


API_URL = "http://127.0.0.1:8000/analyze-email"


def analyze_email_file(email_file_path: Path) -> None:
    """
    Sends one raw MIME email file to the backend API and prints the response.
    """

    raw_email = email_file_path.read_text(
        encoding="utf-8",
        errors="ignore"
    )

    response = requests.post(
        API_URL,
        json={
            "raw_email": raw_email,
            "user_name": "Zion",
            "user_email": "zion.maimon@gmail.com",
        },
        timeout=30
    )

    response.raise_for_status()

    print("\n" + "=" * 70)
    print("EMAIL FILE:", email_file_path.name)
    print("=" * 70)

    print(response.json())


def check_api() -> None:
    """
    Sends multiple sample raw MIME emails to the backend API.
    """

    project_root = Path(__file__).resolve().parents[2]

    sample_email_files = [
        "reply_to_mismatch_example_email.eml",
        "url_example_email.eml",
        "attachment_example_email.eml",
        "dear_friend_example_email.eml",
    ]

    for email_file_name in sample_email_files:

        email_file_path = (
            project_root
            / "samples"
            / email_file_name
        )

        if not email_file_path.exists():

            print("\nMissing file:", email_file_path)
            print("Skipping...")
            continue

        analyze_email_file(
            email_file_path=email_file_path
        )


if __name__ == "__main__":
    check_api()