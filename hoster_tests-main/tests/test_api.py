""" Проверка кода стараниц методами GET POST """

import time
import requests
import allure
from url.url_page import Url

headers = {
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N)"
                  " AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/77.0.3865.120 Mobile Safari/537.36 ",
}


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на главную страницу")
def test_get_home_page():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_home, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
                response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"
    with allure.step(f"Посмотрим что получили {response}"):
        pass


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Помочь")
def test_get_marketplace_page():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_volunteering, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
                response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"
    with allure.step(f"Посмотрим что получили {response}"):
        pass


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Проекты")
def test_get_abuse_page():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_project, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
                response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"
    with allure.step(f"Посмотрим что получили {response}"):
        pass


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Партнеры")
def test_get_whois_page():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_partners, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
                response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Территория успеха")
def test_get_payments_page():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_shop, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
                response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Контакты")
def test_get_belgie_page():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_contacts, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
                response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Помощь центру")
def test_get_cases_page():
    """ Проверка кода ответа. """

    time.sleep(1)
    response = requests.get(Url.url_help, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
                response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Политика конфединциальности")
def test_get_partners_page():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_agreement, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
                response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Новости")
def test_get_clients_page():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_news, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
                response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу О центре")
def test_get_public_clients_page():
    """ Проверка кода ответа. """

    time.sleep(1)
    response = requests.get(Url.url_about, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
                response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Школа")
def test_get_help_page():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_school, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
                response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Специалисты")
def test_get_media_page():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_specialists, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
                response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"



@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Контакты")
def test_get_clients_contacts_page():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_contacts, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
                response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу ДОКУМЕНТЫ Положение о cookie-файлах")
def test_get_clients_documents_cookies_policy_page():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_clients_documents_cookies_policy, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
                response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"



