Тестовое задание
Тестировщик / Web QA (с AI + MCP автоматизацией).
Выполнил: Шалимов Александр Александрович

Структура репозитория:
|
-.github\workflows (настройки взаимодействия с GitHub)
-.venv (виртуальной окружение Python)
-.vscode (настройки запуска VS Code)
- e2e (для автотестов Playwright)
- elements (классы для фреймворка Page Element)
- factories (классы для фреймворка Page Factory)
- fixtures (delivery.db)
- node modules (для Node.js)
- pages (классы для фреймворка Page Object)
- sql (quereies.sql, решение третьей задачи из тестового задания)
- tests (тесты UI)
    test_delivery_days.py (тест с обращением к БД)
    test_delivery_schedule (тесты интерфеса)

Порядок запускатестов:
Вкладка Actions -> Выбираем самый последний workflow -> Нажимаем на Re-run jobs -> Нажимаем на Re-run all jobs
