from pages.base_page import BasePage
from elements.base_element import BaseElement


class DeliverySchedulePage(BasePage):

    URL = "https://altlog.ru/grafik-dostavok-sbornyh-gruzov"

    title = "h1"
    cities_column = "table tbody tr td:first-child"
    cities = "div[class*='city'], div[class*='row']"

    def open_page(self):
        self.open(self.URL)
        self.wait_page_ready()

    def get_title(self):
        return BaseElement(self.page, self.title).get_text()

    #def is_table_visible(self):
    #   return BaseElement(self.page, self.table).is_visible()

    def get_all_cities(self):
        return self.page.locator(self.cities_column).all_inner_texts()
    
    def has_schedule_content(self):
        return self.page.locator(self.cities).count() > 0

    def is_correct_page(self):
        title = self.get_title().upper()
        return (
            "ДОСТАВКА" in title
            and "СБОРНЫХ" in title
            and "+2" in title
        )