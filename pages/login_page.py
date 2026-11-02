from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.account_list =  page.locator("#nav-link-accountList")
        self.sign_in = page.get_by_label("Account settings and Lists").get_by_role("link", name="Sign in")
        self.sign_in_link = page.get_by_role("link", name="Sign in")
        self.email_input = page.get_by_role("textbox", name="Enter mobile number or email")
        self.password_input = page.get_by_role("textbox", name="Password")
        self.continue_button = page.get_by_role("button", name="Continue")
        self.sign_in_button = page.get_by_role("button", name="Sign in", exact=True)
        self.fg_auth_link = page.locator("#auth-fpp-link-bottom")
        self.fg_ap_email = page.locator("#ap_email")
        self.fg_continue_button = page.locator("#continue")
        self.am_signout = page.locator("#nav-item-signout")


    def sign_in_click(self):

        self.account_list.hover()
        self.sign_in_link.click()

    def nav_hover(self):
        self.account_list.hover()

    def sign_other_click(self):

        self.account_list.hover()
        self.sign_in.click()

    def enter_username(self, username):
        self.email_input.fill(username)

    def click_continue(self):
        self.continue_button.click()
    
    def enter_password(self, password):
        self.password_input.fill(password)

    def click_sign_in(self):
        self.sign_in_button.click()

    def fg_link(self):
        self.fg_auth_link.click()

    def fg_username(self,fgusername):
        self.fg_ap_email.click()
        self.fg_ap_email.fill(fgusername)

    def fg_button(self):
        self.fg_continue_button.click()

    def nav_signout(self):
        self.am_signout.wait_for(state="visible")
        self.am_signout.click()