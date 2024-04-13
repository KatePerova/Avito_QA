import pytest
from playwright.sync_api import sync_playwright
import constants

# Функция запуска браузера
@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        yield browser
        browser.close()

# Функция модификации ответа бэкенда 
def modify_response(page, data):
    def modifier(route, request):
        modified_response = {"body": data}
        route.fulfill(body=modified_response['body'])

    page.route(constants.COUNTERS_INIT_ROUTE, modifier)

# Основная функция для выполнения тестов
def perform_test(browser, test_name, test_backend_response):
    # Открытие
    page = browser.new_page()

    # Замена данных, получаемых от бэкенда, на тестовые
    modify_response(page, test_backend_response)
    
    # Переход по ссылке, ожидание загрузки страницы и получения данных от бэкенда
    page.goto(constants.COUNTERS_URL, wait_until="load", timeout=constants.TIMEOUT_MS)
    page.wait_for_selector(constants.WATER_COUNTER_SELECTOR)
    page.wait_for_selector(constants.CO2_COUNTER_SELECTOR)
    page.wait_for_selector(constants.ENERGY_COUNTER_SELECTOR)
    
    # Выбор элемента со счётчиком воды
    page.evaluate(constants.SELECTOR_CONF, constants.WATER_COUNTER_SELECTOR)
    # Сохранение скриншота со счётчиком воды
    page.screenshot(path="output/"+test_name+" Счётчик воды"+".png", clip=constants.COUNTER_CLIP)

    # Выбор элемента со счётчиком CO2
    page.evaluate(constants.SELECTOR_CONF, constants.CO2_COUNTER_SELECTOR)
    # Сохранение скриншота со счётчиком CO2
    page.screenshot(path="output/"+test_name+" Счётчик CO2"+".png", clip=constants.COUNTER_CLIP)

    # Выбор элемента со счётчиком электроэнергии
    page.evaluate(constants.SELECTOR_CONF, constants.ENERGY_COUNTER_SELECTOR)
    # Сохранение скриншота со счётчиком электроэнергии
    page.screenshot(path="output/"+test_name+" Счётчик электроэнергии"+".png", clip=constants.COUNTER_CLIP)        

# Тест-кейс #1. Проверка отображения счётчиков с нулевыми значениями
def test_counters_with_zero_values(browser):
    perform_test(browser,
    "Тест-кейс #1. Проверка отображения счётчиков с нулевыми значениями.",
    '{"result":{"blocks":{"personalImpact":{"data":{"water":0,"co2":0,"energy":0}}}}}')

# Тест-кейс #2. Проверка отображения счётчиков с отрицательными значениями
def test_counters_with_negative_values(browser):
    perform_test(browser,
    "Тест-кейс #2. Проверка отображения счётчиков с отрицательными значениями.",
    '{"result":{"blocks":{"personalImpact":{"data":{"water":-1,"co2":-1,"energy":-1}}}}}')

# Тест-кейс #3: Проверка отображения счётчиков со значениями, лежащими в диапазоне от 1 до 999
def test_counters_with_values_in_1_999(browser):
    perform_test(browser,
    "Тест-кейс #3. Проверка отображения счётчиков со значениями, лежащими в диапазоне от 1 до 999.",
    '{"result":{"blocks":{"personalImpact":{"data":{"water":123,"co2":123,"energy":123}}}}}')

# Тест-кейс #4: Проверка отображения счётчиков со значениями, лежащими в диапазоне от 1000 до 999_999
def test_counters_with_values_in_1000_999999(browser):
    perform_test(browser,
    "Тест-кейс #4. Проверка отображения счётчиков со значениями, лежащими в диапазоне от 1000 до 999_999.",
    '{"result":{"blocks":{"personalImpact":{"data":{"water":3000,"co2":3123,"energy":13123}}}}}') 

# Тест-кейс #5: Проверка отображения счётчиков со значениями, большими или равными 1_000_000
def test_counters_with_values_more_than_999999(browser):
    perform_test(browser,
    "Тест-кейс #5. Проверка отображения счётчиков со значениями, большими или равными 1_000_000.",
    '{"result":{"blocks":{"personalImpact":{"data":{"water":1000000,"co2":1000000,"energy":1000000}}}}}') 