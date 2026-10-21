
import os
import requests
import psycopg2

AWS_ACCESS_KEY_ID = "AKIA1234567890ABCDEF"
AWS_SECRET_ACCESS_KEY = "AbCdEfGhIjKlMnOpQrStUvWxYz0123456789ABCD"

GITHUB_TOKEN = "ghp_ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
SLACK_TOKEN = "xoxb-1234567890-abcdefghijklmnopqrstuvwx"


DATABASE_URL = "postgres://admin:SuperSecret123@localhost:5432/prod"

JWT_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMjM0NTYifQ.signature123456"


def connect_to_database():
    return psycopg2.connect(DATABASE_URL)


def fetch_github_data():
    headers = {"Authorization": f"Bearer {GITHUB_TOKEN}"}
    return requests.get(
        "https://api.github.com/user",
        headers=headers,
        timeout=10,
    )

API_KEY = "CredHunterTestKey123456"
PASSWORD = "FakePassword123"

def main():
    print("CredHunter test application")
    print("API key configured:", bool(API_KEY))
    print("Database configured:", bool(DATABASE_URL))


if __name__ == "__main__":
    main()
