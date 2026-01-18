import os
from playwright.async_api import async_playwright
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("LINKEDIN_EMAIL")
PASSWORD = os.getenv("LINKEDIN_PASSWORD")

STORAGE_STATE_PATH = "storage_state.json"


async def login():
    p = await async_playwright().start()

    # ---------------------------
    # CASE 1: Session already exists → reuse it
    # ---------------------------
    if os.path.exists(STORAGE_STATE_PATH):
        print("🔁 Reusing existing LinkedIn session")

        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(
            storage_state=STORAGE_STATE_PATH,
            viewport=None
        )
        page = await context.new_page()

        await page.goto("https://www.linkedin.com/feed/")
        return p, browser, context, page

    # ---------------------------
    # CASE 2: No session → login once
    # ---------------------------
    if not EMAIL or not PASSWORD:
        raise ValueError("Missing LinkedIn credentials in environment variables")

    print("🔐 No session found. Logging in once…")

    browser = await p.chromium.launch(headless=False)
    context = await browser.new_context(viewport=None)
    page = await context.new_page()

    await page.goto("https://www.linkedin.com/login")
    await page.fill("#username", EMAIL)
    await page.fill("#password", PASSWORD)
    await page.click("button[aria-label='Sign in']")
    await page.wait_for_url("**/feed/**", timeout=20000)

    # ---------------------------
    # SAVE SESSION
    # ---------------------------
    await context.storage_state(path=STORAGE_STATE_PATH)
    print("💾 Session saved for future runs")

    return p, browser, context, page
