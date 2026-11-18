from playwright.sync_api import Page, expect


class DemoBlazePage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.login_link = page.get_by_role("link", name="Log in", exact=True)
        self.login_modal = page.locator("#logInModal")
        self.username_input = page.locator("#loginusername")
        self.password_input = page.locator("#loginpassword")
        self.submit_login_button = self.login_modal.get_by_role(
            "button", name="Log in", exact=True
        )
        self.logout_link = page.get_by_role("link", name="Log out", exact=True)
        self.welcome_message = page.locator("#nameofuser")

    def open(self) -> None:
        self.page.goto("https://www.demoblaze.com/index.html")

    def log_in(self, username: str, password: str) -> None:
        self.login_link.click()
        expect(self.login_modal).to_be_visible()
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.submit_login_button.click()

    def log_out(self) -> None:
        self.logout_link.click()
