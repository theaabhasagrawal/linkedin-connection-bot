# LinkedIn Connection Automation (CLI)

A local, CLI-driven LinkedIn automation tool that sends connection requests
based on people search keywords using Playwright.

This tool is built for **technical users** who prefer command-line tools,
explicit control, and minimal abstraction.

- Runs locally
- No browser extensions
- No hosted service
- No remote credential storage

---

## What this does

- Logs into LinkedIn once
- Persists the session locally
- Reuses login across runs
- Searches people by keyword
- Sends connection requests up to a defined limit
- Skips profiles that require email
- Avoids duplicate attempts
- Handles dynamic LinkedIn UI edge cases

---

## What this does NOT do

- Does NOT bypass LinkedIn limits
- Does NOT guarantee account safety
- Does NOT run in the cloud
- Does NOT provide a GUI

You are responsible for how you use it.

---

## Requirements

- Python **3.10+**
- macOS or Linux
- Git
- A LinkedIn account

---

## Installation

```bash
git clone https://github.com/theaabhasagrawal/linkedin-connection-bot.git
cd linkedin-connection-bot


Create and activate a virtual environment:
python3 -m venv venv
source venv/bin/activate

Install dependencies:
pip install -r requirements.txt
playwright install chromium


Authentication
The tool uses local session persistence.
Credentials are provided via environment variables or a .env file.
Option 1: Environment variables
export LINKEDIN_EMAIL=you@example.com
export LINKEDIN_PASSWORD=yourpassword

Option 2: .env file
Create a .env file in the project root:
LINKEDIN_EMAIL=you@example.com
LINKEDIN_PASSWORD=yourpassword


Session behavior
	•	First run logs in normally
	•	Session is saved locally (storage_state.json)
	•	Subsequent runs reuse the session
	•	Fewer CAPTCHAs and faster startup

To force a fresh login:
rm storage_state.json


Usage
CLI-first usage (recommended)
python -m app.main \
  --query "amazon recruiter india" \
  --limit 20


All Flags:
python -m app.main \
  --query "product manager fintech" \
  --limit 15 \
  --start-page 3 \
  --max-pages 5


Safety Guidelines
LinkedIn enforces behavior-based limits.
Recommended usage:
	•	20–30 requests per day
	•	One run per session
	•	Avoid repeated runs back-to-back
Aggressive usage may result in temporary or permanent restrictions.


Philosophy
This tool is intentionally:
	•	Local-only
	•	CLI-first
	•	Minimal UI
	•	User-responsible
If you need:
	•	A hosted service
	•	A GUI
	•	Automation guarantees
	•	“Growth hacks”
This project is not for you.


Disclaimer

This project is for educational and personal automation purposes only.
You are solely responsible for complying with LinkedIn’s terms of service
and for any actions taken using this tool.


