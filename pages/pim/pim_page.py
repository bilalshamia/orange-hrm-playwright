from playwright.sync_api import Page , expect
from pages.pim.add_employee import AddEmployeePage
from pages.pim.employee_list_page import EmployeeListPage
class PimPage:
    def __init__(self,page : Page):
        self.page=page   
        self.page.get_by_role("link",name="PIM").click()
        Pim_title=self.page.get_by_role("heading", name="PIM")
        expect(Pim_title).to_be_visible()

    def visit_tab_add_employee(self):

            self.page.get_by_text("Add Employee").click()
            expect(self.page.get_by_role("heading",name="Add Employee")).to_be_visible()
            return AddEmployeePage(self.page)

    def visit_tab_employee_list(self):
        self.page.get_by_text("Employee List").click()
        expect(self.page.get_by_text("Employee List")).to_be_visible()
        return EmployeeListPage(self.page)