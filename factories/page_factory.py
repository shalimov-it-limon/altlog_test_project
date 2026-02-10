from pages.delivery_schedule_page import DeliverySchedulePage


class PageFactory:

    @staticmethod
    def delivery_schedule(page):
        return DeliverySchedulePage(page)