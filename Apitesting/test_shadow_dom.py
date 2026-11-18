from playwright.sync_api import Page, expect


def test_example(page: Page):
    page.set_content("""
        <book-app>
            <template shadowrootmode="open">
                <input type="search" aria-label="Search Books" placeholder="Search Books">
            </template>
        </book-app>
    """)

    search_box = page.get_by_role("searchbox", name="Search Books")
    expect(search_box).to_be_visible()
    search_box.fill("welcome")
    expect(search_box).to_have_value("welcome")
