from page_object.auth_page import AuthPage
from page_object.admin_page import AdminPage
from page_object.products_page import ProductPage
from test_data.user import _user
from test_data.user import _user2
from test_data.product_data import add_product
from page_object.register_page import RegisterPage
from page_object.currency_page import CurrencyPage
import allure


@allure.title('Авторизация в админку')
def test_login_to_admin(browser):
    auth_page = AuthPage(browser)
    auth_page.open(path=AuthPage._path)
    auth_page.login_to_account(username=_user["name"], password=_user["password"])


@allure.title('Открытие карточки продукта')
def test_open_product_cart(browser):
    auth_page = AuthPage(browser)
    admin_page = AdminPage(browser)
    auth_page.open(path=AuthPage._path)
    auth_page.login_to_account(username=_user["name"], password=_user["password"])
    admin_page.switch_to_product_page()


@allure.title('Добавление нового товара')
def test_add_new_product(browser):
    auth_page = AuthPage(browser)
    admin_page = AdminPage(browser)
    product_page = ProductPage(browser)
    auth_page.open(path=AuthPage._path)
    auth_page.login_to_account(username=_user["name"], password=_user["password"])
    admin_page.switch_to_product_page()
    product_page.adding_new_item(product_name=add_product()['product_name'],
                                 meta_tag_title=add_product()['meta_tag_title'],
                                 description=add_product()['description'],
                                 model=add_product()['model'])


@allure.title('Удаление товара')
def test_remove_added_item(browser):
    auth_page = AuthPage(browser)
    admin_page = AdminPage(browser)
    auth_page.open(path=AuthPage._path)
    auth_page.login_to_account(username=_user["name"], password=_user["password"])
    admin_page.switch_to_product_page_catalog()
    admin_page.find_and_remove_product()
    admin_page.alert_accept()


@allure.title('Регистрация нового пользователя')
def test_register_new_acc(browser):
    register_page = RegisterPage(browser)
    register_page.register_new_account(
        first_name=_user2['first_name'],
        last_name=_user2['last_name'],
        email=_user2['email'],
        telephone=_user2['telephone'],
        password=_user2['password'],
        confirm_pass=_user2['confirm_pass']
    )


@allure.title('Авторизация в личный кабинет')
def test_log_in_account(browser):
    register_page = RegisterPage(browser)
    register_page.account_to_account(email=_user2['email'], password=_user2['password'])


@allure.title('Выход из личного кабинета')
def test_logout_from_acc(browser):
    register_page = RegisterPage(browser)
    register_page.account_to_account(email=_user2['email'], password=_user2['password'])
    register_page.logout_from_account()


@allure.title('Изменение валюты')
def test_switch_currency(browser):
    currency_page = CurrencyPage(browser)
    currency_page.switch_to_pound()
    currency_page.switch_to_dollar()
    currency_page.switch_to_euro()
