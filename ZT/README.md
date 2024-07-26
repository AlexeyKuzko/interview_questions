## Автотестовый фреймворк ZT

### Реализованные сценарии

Созданы тесты, покрывающие 5 высокоприоритетных проверок для функциональности "Авторизация" [Яндекс Паспорта](https://passport.yandex.ru).

Полный чеклист опубликован на **[Google Docs](https://docs.google.com/document/d/11Z_BlI4JSaEnTVgdG9ePdqNOt4Y9M8c55sFXn1QuZ-U/edit)**.

Процент покрытия 100% (отчет: `htmlcov/index.html`)

### Структура проекта

- `Sources` - Test Sources Root
- `/run_tests.py` - модуль, выполняющий запуск автотестов
- `/config`
  - `config.py`
- `/pages`
  - `login_page.py`
- `/tests`
  - `test_authorization.py`
   - `сonftest.py`
- `/utils`
  - `api_client.py`
  - `browser.py`
  - `data.py`
- `/results`
  - `test_results.txt`

### Запуск автотестов

1. **Установка браузеров**

- [Google Chrome](https://www.google.com/chrome/)
- [Mozilla Firefox](https://www.mozilla.org/firefox/)

2. **Установка зависимостей**

    ```bash
    pip install -r requirements.txt
    ```

3. **Запуск автотестов и создание Allure-отчета**

    ```bash
    pytest -v tests --alluredir allure_results && allure serve allure_results
    ```
