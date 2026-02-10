class BaseElement:

    def __init__(self, page, selector):
        self.page = page
        self.selector = selector

    def wait(self, timeout=60000):
        self.page.wait_for_selector(self.selector, timeout=timeout)

    def get_text(self):
        self.wait()
        return self.page.locator(self.selector).inner_text()

    def is_visible(self):
        self.wait()
        return self.page.locator(self.selector).is_visible()