from playwright.sync_api import Page, expect


def test_search_for_tshirts(page: Page) -> None:
    page.goto("http://www.automationpractice.pl/index.php")
    page.locator("#search_query_top").fill("T-shirts")
    page.locator("#search_query_top").press("Enter")

    expect(
        page.get_by_text("Faded Short Sleeve T-shirts", exact=True)
    ).to_be_visible()
