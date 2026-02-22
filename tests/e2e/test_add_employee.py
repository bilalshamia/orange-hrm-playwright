import random
from playwright.sync_api import Page, expect

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
