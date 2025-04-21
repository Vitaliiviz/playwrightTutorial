class HomePage:

    def __init__(self, page):
        self.about_header = page.locator("text = We export")
        self.about_body = page.locator("text = We export new and used vehiles all over Europe.")