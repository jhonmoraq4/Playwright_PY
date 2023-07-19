class SearchPage:
    def __init__(self, page):
        self.page = page
        self.search_term_input = page.locator('input#sb_form_q')

    def navigate(self):
        self.page.goto("https://bing.com")

    def search(self, text):
        self.search_term_input.fill(text)
        self.search_term_input.press("Enter")