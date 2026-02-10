class BasePage:

    def __init__(self, page):
        self.page = page

    def open(self, url):
        self.page.goto(url, wait_until="domcontentloaded")

    def wait_page_ready(self):
        self.page.wait_for_selector("h1", timeout=60000)