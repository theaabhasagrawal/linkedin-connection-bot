# LinkedIn Connection Automation (CLI)

A local, CLI-driven LinkedIn automation tool that sends connection requests based on people search keywords using Playwright.

Designed for technical users who prefer:
- Command-line tools
- Explicit control
- Minimal abstraction
- No hosted services

Runs entirely on your machine.

---

## Requirements

- Python 3.10+
- Git
- LinkedIn account

**Supported OS:**
- macOS
- Linux
- Windows (PowerShell)

---

## Installation

### macOS / Linux

```bash
# 1. Clone repository
git clone [https://github.com/theaabhasagrawal/linkedin-connection-bot.git](https://github.com/theaabhasagrawal/linkedin-connection-bot.git)
cd linkedin-connection-bot

# 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
playwright install chromium
```

### Windows (PowerShell)

```powershell
# 1. Clone repository
git clone [https://github.com/theaabhasagrawal/linkedin-connection-bot.git](https://github.com/theaabhasagrawal/linkedin-connection-bot.git)
cd linkedin-connection-bot

# 2. Create virtual environment
python -m venv venv
.\venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
playwright install chromium
```

---

## Authentication

The tool uses local session persistence. Credentials are provided via environment variables or a `.env` file.

### Option 1: Environment variables

**macOS / Linux**
```bash
export LINKEDIN_EMAIL=you@example.com
export LINKEDIN_PASSWORD=yourpassword
```

**Windows (PowerShell)**
```powershell
setx LINKEDIN_EMAIL "you@example.com"
setx LINKEDIN_PASSWORD "yourpassword"
# Note: Restart the terminal after using setx
```

### Option 2: .env file
Create a file named `.env` in the project root:
```ini
LINKEDIN_EMAIL=you@example.com
LINKEDIN_PASSWORD=yourpassword
```

---

## Usage

### Basic usage
```bash
python -m app.main
```

### CLI-first usage (Recommended)
```bash
python -m app.main --query "amazon recruiter india" --limit 20
```

### Available CLI flags

| Flag | Description |
| :--- | :--- |
| `--query` | LinkedIn people search keyword |
| `--limit` | Max connection requests to send |
| `--start-page` | Page number to start scanning from |
| `--max-pages` | Max pages to scan |

### Full example
```bash
python -m app.main \
  --query "product manager fintech" \
  --limit 15 \
  --start-page 3 \
  --max-pages 5
```

---

## Safety Guidelines

**Recommended usage:**
- 20–30 requests per day maximum.
- One run per session.
- Avoid repeated runs back-to-back.

*Aggressive usage may result in account restrictions.*

---

## Disclaimer

This project is for educational and personal automation purposes only.

You are solely responsible for complying with LinkedIn’s terms of service and for any actions taken using this tool.

---
