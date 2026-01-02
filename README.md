# Automated News Email Sender (Python)

This project fetches the latest news articles from an external API and automatically sends a summarized email using Gmail SMTP.

## Overview
The script retrieves news data in JSON format, extracts key article details, formats them into an email body, and sends the email securely using environment variables.

## Tech Stack
- Python
- Requests
- SMTP (Gmail)
- python-dotenv

## How It Works
- Loads API keys and credentials from environment variables
- Fetches news articles from a configured API endpoint
- Formats titles, descriptions, and links into an email
- Sends the email using a secure SMTP connection

## Files
- `main.py` – Fetches news data and prepares the email content
- `send_email.py` – Handles secure email delivery via SMTP

## Usage
1. Install dependencies:
2. Configure `.env` file with API and Gmail credentials
3. Run
 
## Learning Outcome
This project demonstrates real-world Python automation, API consumption, secure credential handling, and email automation.
