import pytest
from playwright.sync_api import Page, expect
from pages.pim.pim_page import PimPage

def test_employee(page:Page,login_with_admin):
    pim_page=PimPage(page)
    add_employee_pages=pim_page.visit_tab_add_employee()
    add_employee_pages.add_employee_names(first="Bilal",middle="Maher",last="sham")
    page.wait_for_timeout(5000)