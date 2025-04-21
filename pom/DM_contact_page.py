class ContactPage:
    def __init__(self, page):
        self.page = page


    def navigate(self):
        self.page.goto("https://dm-group.com.pl/contact/")

    def submit_form(self, name, email, subject, message):
        self.page.fill("[placeholder='Name']", name)
        self.page.fill("[placeholder='E-mail']", email)
        self.page.fill("[placeholder='Subject']", subject)
        self.page.fill("[placeholder='Message']", message)