from playwright.sync_api import Page

class PIMPage:
    def __init__(self, page: Page):
        self.page = page
        self.pim_menu = page.get_by_role("link", name="PIM")
        self.add_button = page.get_by_role("button", name="Add")
        self.first_name = page.get_by_placeholder("First Name", exact=False)
        self.last_name = page.get_by_placeholder("Last Name", exact=False)
        self.save_button = page.get_by_role("button", name="Save")
        self.create_login_details_switch = page.locator("span").filter(has_text="Create Login Details")

    def add_employee(self, f_name, l_name, create_login=False):
        self.pim_menu.click()
        self.add_button.click()
        self.first_name.fill(f_name)
        self.last_name.fill(l_name)
        
        if create_login:
            self.create_login_details_switch.click()
            
        self.save_button.click()
