import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.tokopedia.com/")
    page.locator("div:nth-child(5) > .css-sncotz > div > .css-1u6yi94 > .css-1x9x50q > .css-twpy6c > .prd_container-card > .pcv3__container > .css-19oqosi > a").click()
    time.sleep(10)
    page.get_by_test_id("pdpBtnNormalPrimary").click()
    time.sleep(10)
    page.get_by_test_id("email-phone-input").click()
    page.get_by_test_id("email-phone-input").fill("benjamin.aulia88@gmail.com")
    page.get_by_test_id("email-phone-submit").click()
    time.sleep(10)
    page.get_by_test_id("forgot-password").click()
    page.get_by_label("unf-input").click()
    page.get_by_label("unf-input").fill("benjamin.aulia88@gmail.com")
    page.get_by_role("button", name="Lanjut").click()
    page.get_by_label("email").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
