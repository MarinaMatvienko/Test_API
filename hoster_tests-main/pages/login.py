""" Элементы страницы логирования """

import os
from pages.base_page import WebPage
from pages.elements import WebElement


class Login(WebPage):
    """Класс представляющий страницу логирования"""

    def __init__(self, web_driver, url=""):
        if not url:
            url = (
                    os.getenv("LOGIN")
                    or "https://hoster.by/"
            )

        super().__init__(web_driver, url)

    section_main_unit = WebElement(id="banner-main4")
    home_login_button = WebElement(xpath="/html/body/header/div[2]/div/div[4]/div[1]")
    close_log_form = WebElement(xpath='//*[@id="loginModal"]/div[1]/div[1]')
    input_log_email = WebElement(
        xpath='//*[@id="loginModal"]/div[1]/div[2]/div[2]/div/form/div[1]/input'
    )
    input_pass = WebElement(id="auth")
    name_user = WebElement(xpath="/html/body/header/div[2]/div/div[4]/div[1]/div/span[1]")
    forgot_your_password_link = WebElement(xpath="Sign Up")
    form_sign_in_btn = WebElement(id="auth-btn")
    registr_link = WebElement(id="registrUser")
    show_pass_btn = WebElement(css_selector=".hby-form .hby-form-item.has-icon .icon")
    invalid_data_msg = WebElement(
        xpath=".hby-section-form .hby-form-item .hby-error-text"
    )
    error_email = WebElement(css_selector='.hby-section-form .hby-form-item .hby-error-text')
    error_pass = WebElement(css_selector=
                            '#loginModal > div.hby-modal-body >'
                            ' div.hby-modal-wrapper > div.hby-section-form >'
                            ' div > form > div.hby-form-item.has-icon.auth-password > div')
