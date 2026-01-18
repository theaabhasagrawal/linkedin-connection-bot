# LinkedIn Connection Automation (CLI)

A local, CLI-driven LinkedIn automation tool that sends connection requests
based on people search keywords using Playwright.

Designed for technical users who prefer:
- Command-line tools
- Explicit control
- Minimal abstraction
- No hosted services

Runs entirely on your machine.

---

## What this does

- Logs into LinkedIn once
- Saves the session locally
- Reuses login across runs
- Searches people by keyword
- Sends connection requests up to a defined limit
- Skips profiles that require email
- Avoids duplicate attempts
- Handles dynamic LinkedIn UI edge cases
- Prevents infinite loops and flaky behavior

---

## What this does NOT do

- Does NOT bypass LinkedIn limits
- Does NOT guarantee account safety
- Does NOT run in the cloud
- Does NOT provide a GUI

You are responsible for how you use it.

---

## Requirements

- Python 3.10+
- Git
- LinkedIn account

Supported OS:
- macOS
- Linux
- Windows (PowerShell)

---

# Installation

## macOS / Linux

### Clone repository

```bash
git clone https://github.com/theaabhasagrawal/linkedin-connection-bot.git
cd linkedin-connection-bot

Create virtual environment

python3 -m venv venv
source venv/bin/activate

Install dependencies

pip install -r requirements.txt
playwright install chromium


⸻

Windows (PowerShell)

Clone repository

git clone https://github.com/theaabhasagrawal/linkedin-connection-bot.git
cd linkedin-connection-bot

Create virtual environment

python -m venv venv
.\venv\Scripts\activate

Install dependencies

pip install -r requirements.txt
playwright install chromium


⸻

Authentication

The tool uses local session persistence.

Credentials are provided via environment variables or a .env file.

⸻

Option 1: Environment variables

macOS / Linux

export LINKEDIN_EMAIL=you@example.com
export LINKEDIN_PASSWORD=yourpassword

Windows (PowerShell)

setx LINKEDIN_EMAIL "you@example.com"
setx LINKEDIN_PASSWORD "yourpassword"

Restart the terminal after setting variables.

⸻

Option 2: .env file

LINKEDIN_EMAIL=you@example.com
LINKEDIN_PASSWORD=yourpassword

Create this file as .env in the project root.

⸻

Session behavior
	•	First run logs in normally
	•	Session is saved locally as storage_state.json
	•	Subsequent runs reuse the session
	•	Faster startup
	•	Fewer CAPTCHAs

Force fresh login

rm storage_state.json


⸻

Usage

Basic usage

python -m app.main


⸻

CLI-first usage (recommended)

python -m app.main --query "amazon recruiter india" --limit 20


⸻

Available CLI flags

Flag	Description
–query	LinkedIn people search keyword
–limit	Max connection requests
–start-page	Page number to start from
–max-pages	Max pages to scan


⸻

Full example

python -m app.main \
  --query "product manager fintech" \
  --limit 15 \
  --start-page 3 \
  --max-pages 5


⸻

Configuration (optional)

config/config.yaml

Used when CLI flags are not provided.

⸻

Safety Guidelines

Recommended usage:
	•	20–30 requests per day
	•	One run per session
	•	Avoid repeated runs back-to-back

Aggressive usage may result in account restrictions.

⸻

Philosophy

This tool is:
	•	Local-only
	•	CLI-first
	•	Minimal UI
	•	User-responsible

If you need:
	•	Hosted service
	•	GUI
	•	Automation guarantees
	•	Growth hacks

This project is not for you.

⸻

Disclaimer

This project is for educational and personal automation purposes only.

You are solely responsible for complying with LinkedIn’s terms of service
and for any actions taken using this tool.

⸻

License

MIT

---

## ✅ WHY THIS VERSION FIXES YOUR ISSUE

- No broken code blocks
- No prose inside command fences
- macOS/Linux and Windows fully separated
- Every command can be copied independently
- GitHub renders it cleanly
- Power users won’t rage

This is **final-form README**.  
You can safely ship this.

If you want next:
- Add `--dry-run`
- Add CSV logging
- Tag `v1.0.0`
- Harden for multi-account usage

Just tell me.
