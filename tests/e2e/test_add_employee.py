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

def test_add_new_employee(page: Page):
    num=random.randint(1,1000)
   
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", timeout=60000 )
    
    
    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    
    
    page.get_by_role("link", name="PIM").click(timeout=60000)
    page.get_by_role("button", name="Add").click()
    
   
    page.get_by_placeholder("First Name").fill(f"Bilal_{num}")
    page.get_by_placeholder("Last Name").fill("Tester")
    
   
    page.get_by_role("button", name="Save").click()
    

    expect(page.get_by_text("Successfully Saved")).to_be_visible(timeout=10000)
