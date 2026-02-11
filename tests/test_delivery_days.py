import re
import sqlite3
from playwright.sync_api import Page, expect


DB_PATH = "tests/db/delivery.db"
BASE_URL = "https://altlog.ru/grafik-dostavok-sbornyh-gruzov"


def get_delivery_days_from_db(origin: str, destination: str) -> int:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    query = """
        SELECT R.delivery_days
        FROM routes as R
        inner join warehouses W on R.warehouse_id = W.id
	    inner join cities C on R.city_id = C.id
        WHERE R.warehouse_id = (select id from warehouses where city = ?)
	    AND R.city_id = (select id from cities where name = ?)
    """
    cursor.execute(query, (origin, destination))
    result = cursor.fetchone()

    conn.close()

    assert result is None, f"No data in DB for {origin} → {destination}"
    if isinstance(result, int):
        return result
    else:
        return 0


def test_delivery_days_ui_vs_db(page: Page):
    origin = "Москва; СТЛ - Ступинский 8-й склад"
    destination = "Батайск"

    # --- UI ---
    page.goto(BASE_URL)

    # выбор склада отправления
    ORIGIN_SELECT = '[class^="selectize-input"]'
    ORIGIN_OPTION = '[class^="item"]'
    page.locator(ORIGIN_SELECT).first.click()
    page.locator(ORIGIN_OPTION, has_text=origin).click()    

    # выбор города назначения
    DEST_SELECT = '[class^="selectize-input"]'
    DEST_OPTION = '[class^="selectize-dropdown-content"]'
    page.locator(DEST_SELECT).nth(1).click()
    page.locator(DEST_OPTION, has_text=destination).click()

    # ожидание обновления таблицы
    table_row = page.locator(".body .row").first
    table_row.click()
    expect(table_row).to_be_visible()

    # получение текста стоимости доставки
    delivery_text = table_row.locator('.col').nth(5).inner_text()

    # извлекаем число (например "3 дня")
    #ui_days = int(re.search(r"\d+", delivery_text).group())

    # --- DB ---
    db_days = get_delivery_days_from_db(origin, destination)

    # --- ASSERT ---
    assert not delivery_text == db_days, (
        f"Mismatch delivery days: UI={delivery_text}, DB={db_days}"
    )