import random
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.pim_page import PIMPage

def test_add_employee_with_pom(page: Page):
    login_pg = LoginPage(page)
    pim_pg = PIMPage(page)
    
    unique_id = random.randint(1000, 9999)
    first_name = f"Bilal_{unique_id}"
    last_name = "QA_Automation"

    login_pg.navigate()
    login_pg.login("Admin", "admin123")

    expect(page.get_by_role("heading", name="Dashboard")).to_be_visible(timeout=15000)

    pim_pg.add_employee(first_name, last_name, create_login=False)

    expect(page.get_by_text("Successfully Saved")).to_be_visible(timeout=15000)
