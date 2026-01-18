from urllib.parse import quote
from app.li_selectors import *

async def run_connect_flow(page, config):
    query = config["search"]["query"]
    start_page = config["search"]["start_page"]
    max_pages = config["search"]["max_pages"]
    max_requests = config["limits"]["max_requests"]
    delay = config["limits"]["delay_between_actions_ms"]

    sent = 0
    skipped_profiles = set()

    def build_url(page_num):
        encoded = quote(query)
        return (
            "https://www.linkedin.com/search/results/people/"
            f"?keywords={encoded}&origin=SWITCH_SEARCH_VERTICAL"
            f"&page={page_num}&spellCorrectionEnabled=true"
        )

    for page_num in range(start_page, start_page + max_pages):
        if sent >= max_requests:
            break

        await page.goto(build_url(page_num))
        await page.wait_for_timeout(4000)

        while sent < max_requests:
            buttons = page.locator(CONNECT_SELECTOR)
            total = await buttons.count()
            if total == 0:
                break

            button = None
            href = None
            for i in range(total):
                candidate = buttons.nth(i)
                h = await candidate.get_attribute("href")
                if h and h not in skipped_profiles:
                    button = candidate
                    href = h
                    break

            if not button:
                break

            try:
                await button.scroll_into_view_if_needed()
                await page.wait_for_timeout(1000)
                await button.click()
                await page.wait_for_timeout(2000)

                send_btn = page.locator(SEND_WITHOUT_NOTE_SELECTOR)
                email_input = page.locator(EMAIL_INPUT_SELECTOR)
                dismiss_btn = page.locator(DISMISS_SELECTOR)

                if await send_btn.count() > 0 and await send_btn.is_enabled():
                    await send_btn.click()
                    sent += 1
                    print(f"✅ Sent {sent}/{max_requests}")
                else:
                    skipped_profiles.add(href)
                    await dismiss_btn.click()

                await page.wait_for_timeout(delay)

            except Exception:
                skipped_profiles.add(href)
                await page.keyboard.press("Escape")
                await page.wait_for_timeout(delay)

    print("🎯 Finished. Sent:", sent)
