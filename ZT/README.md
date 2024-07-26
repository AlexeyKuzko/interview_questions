## Автотестовый фреймворк ZT

### Реализованные сценарии

Созданы тесты, покрывающие 5 высокоприоритетных проверок для функциональности "Авторизация" [Яндекс Паспорта](https://passport.yandex.ru).

Allure-отчеты в директории `allure-results`; процент тестового покрытия в отчете `htmlcov/index.html`.

Полный чеклист опубликован на **[Google Docs](https://docs.google.com/document/d/11Z_BlI4JSaEnTVgdG9ePdqNOt4Y9M8c55sFXn1QuZ-U/edit)**.

### Структура проекта

- `Sources` – Test Sources Root
  - `base_page.py` - базовая страница "Авторизация"
- `/tests` - пакет, содержащий все тесты
  - `ui_test.py` - модуль, содержащий тесты для UI
  - `api_test.py` - модуль, содержащий тесты для API
- `/utils` - пакет, содержащий вспомогательные модули
  - `api_client.py` - модуль, содержащий методы для взаимодействия с API
  - `browser.py` - модуль, с методами для взаимодействия с браузерами
- `/run_tests.py` - модуль, выполняющий запуск автотестов
- `/сonftest.py` - модуль, содержащий фикстуры, используемые в тестах
- `/data.py` - модуль, содержащий вспомогательные данные, используемые в тестах
- `/pages` - пакет, содержащий POM-страницы

### Запуск автотестов

1. **Установка браузеров**

- [Google Chrome](https://www.google.com/chrome/)
- [Mozilla Firefox](https://www.mozilla.org/firefox/)

2. **Установка зависимостей**

    ```bash
    pip3 install -r requirements.txt
    ```

3. **Запуск автотестов и создание Allure-отчета**

    ```bash
    python3 Sources/run_tests.py && allure serve allure_results
    ```
