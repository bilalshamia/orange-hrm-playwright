import pytest
from playwright.sync_api import Page,expect
from pages.pim.pim_page import PimPage

def test_search_employee_postive(page:Page,login_with_admin):
    pim_page=PimPage(page)
    search_page=pim_page.visit_tab_employee_list()
    search_page.search_by_id("10000")
    search_page.verify_employee_exists("Sayan")
    search_page.reset_search()
    search_page.search_by_name("Sayan")
    search_page.verify_employee_exists("Sayan")

@pytest.mark.parametrize("invalid_id,invalid_name",[
    ("99392","Billlala"),
    ("12323313","Mossahaa"),
    ("9990003","aogisiejs")])

def test_search_employe_negative(page:Page,login_with_admin,invalid_id,invalid_name): 
    pim_page=PimPage(page)
    search_page=pim_page.visit_tab_employee_list()
    search_page.search_by_id(invalid_id)
    search_page.verify_no_records()
    search_page.reset_search()
    search_page.search_by_name(invalid_name)
    search_page.verify_no_records()