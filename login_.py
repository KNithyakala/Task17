# Page Object Module - Login Page

class Zenlogin:
    def __init__(self,page):
        # Locator of elements
        self.page=page
        self.username_textbox= page.locator('//input[@id=":r0:"]')
        self.password_textbox= page.locator('//input[@id=":r1:"]')
        self.submit_button= page.locator('//button[text()="Sign in"]')
        self.error_message1 = page.locator('//p[@id=":r0:-helper-text"]')
        self.error_message2 = page.locator('//p[@id=":r1:-helper-text"]')

    def validate_fields(self):
        try:
            # Field validation
            self.username_textbox.is_visible()
            self.password_textbox.is_visible()
            self.submit_button.is_enabled()
            return True
        except TimeoutError:
            return False

    def login(self,username,password):
        # Entering values in username, password and clicking submit button
        self.username_textbox.fill(username)
        self.password_textbox.fill(password)
        self.submit_button.click()

    def get_error_message(self):
        # getting error message when entering incorrect or invalid email or password
        self.error_message2.wait_for(timeout=3000)
        if self.error_message2.is_visible():
            return self.error_message2.inner_text()
        elif self.error_message1.is_visible():
            return self.error_message1.inner_text()
        else:
            return None

