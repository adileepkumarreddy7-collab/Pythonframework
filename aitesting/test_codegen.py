
import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.demoblaze.com/")
    expect(page.get_by_role("link", name="Home (current)")).to_be_visible()
    page.get_by_role("link", name="Contact").click()
    expect(page.get_by_role("dialog", name="New message")).to_be_visible()
    page.locator("#recipient-email").click()
    page.get_by_role("dialog", name="New message").click()
    expect(page.get_by_role("img", name="Second slide")).to_be_visible()
    page.get_by_role("textbox", name="Message:").click()
    page.locator("#recipient-email").click()
    page.locator("#recipient-email").fill("adileep.8@gmail.com")
    page.locator("#recipient-email").press("Tab")
    page.get_by_role("textbox", name="Contact Email: Contact Name:").fill("8998883899")
    page.get_by_role("textbox", name="Contact Email: Contact Name:").press("Tab")
    page.get_by_role("textbox", name="Message:").fill("idhfksjhfkjret")
    expect(page.get_by_role("img", name="Third slide")).to_be_visible()
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Send message").click()
    expect(page.get_by_role("link", name="PRODUCT STORE")).to_be_visible()
    page.get_by_role("link", name="Cart").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
