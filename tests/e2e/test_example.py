import pytest
from playwright.sync_api import Page, expect
def test_valid_login_to_orangehrm(page: Page):
    login_page = LoginPage(page)
    login_page.login_with_valid_admin()

@pytest.mark.parametrize("username,password", 
                             [("admin","0000"),
                             ("aadmin","admin123"),
                             ("aadmin","1111")])


def test_login_invalid(page: Page,username,password):
    login_page = LoginPage(page)
    login_page.login_with_invalid_admin(username=username,password=password)
