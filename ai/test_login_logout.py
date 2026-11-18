from playwright.sync_api import Page, expect

from aitesting.demoblaze_page import DemoBlazePage


def test_login_and_logout(page: Page) -> None:
    demo_blaze = DemoBlazePage(page)
    demo_blaze.open()

    expect(demo_blaze.login_link).to_be_visible()
    demo_blaze.log_in("pavanol", "test@123")

    expect(demo_blaze.logout_link).to_be_visible()
    expect(demo_blaze.welcome_message).to_have_text("Welcome pavanol")

    demo_blaze.log_out()
    expect(demo_blaze.login_link).to_be_visible()
