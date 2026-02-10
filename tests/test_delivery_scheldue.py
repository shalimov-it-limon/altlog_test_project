from factories.page_factory import PageFactory


def test_page_open(page):
    delivery_page = PageFactory.delivery_schedule(page)
    delivery_page.open_page()
    assert "ДОСТАВКА СБОРНЫХ ГРУЗОВ В РЕЖИМЕ +2.. +6" in delivery_page.get_title()


def test_cities_list_not_empty(page):
    delivery_page = PageFactory.delivery_schedule(page)
    delivery_page.open_page()
    cities = delivery_page.get_all_cities()
    assert len(cities) > 0


def test_correct_page_opened(page):
    delivery = PageFactory.delivery_schedule(page)
    delivery.open_page()

    assert delivery.is_correct_page()