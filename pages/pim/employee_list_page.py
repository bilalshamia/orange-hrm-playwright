from playwright.sync_api import Page , expect
class EmployeeListPage:
    def __init__(self,page :Page):
        self.page=page
        self.id_input=self.page.locator(".oxd-input-group").filter(has_text="Employee Id").locator("input")
        self.name_input = self.page.locator(".oxd-input-group").filter(has_text="Employee Name").locator("input")
        self.search_button=self.page.get_by_role("button",name="Search")
        self.rest_button=self.page.get_by_role("button",name="Reset")
        self.table_row=self.page.locator(".oxd-table-card")
        self.no_record_ms = self.page.locator("span.oxd-text--span").get_by_text("No Records Found")


    def search_by_id(self,emp_id):
            self.id_input.fill(emp_id)
            self.search_button.click()
            self.page.wait_for_load_state("networkidle")

    def search_by_name(self,emp_name):
            self.name_input.fill(emp_name)
            self.page.locator(".oxd-autocomplete-dropdown").wait_for(state="visible")
            self.page.keyboard.press("ArrowDown")
            self.page.keyboard.press("Enter")
            self.search_button.click()

    def verify_employee_exists(self,expected_name):
            self.table_row.first.wait_for(state="visible")    
            expect(self.table_row.first).to_contain_text(expected_name)


    def verify_no_records(self):
            expect(self.no_record_ms.first).to_be_visible()  

    def reset_search(self):
            self.rest_button.click()
