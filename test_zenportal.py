# Test Cases - Validation of Fields , Successful Login, Unsuccessful Login, Submit, Logout Functionality
from Task17.POM.dashboard import Dashboard
from Task17.POM.login_ import Zenlogin
from Task17.conftest import login_details

# Test case 1 - Validation of Fields - Username, Password and Submit button
def test_fields_validation(page,login_details):
    # Instance of Zenlogin page
    login_page= Zenlogin(page)

    #validating the fields
    field_validation = login_page.validate_fields()

    # Username, password and Submit button fields validation
    assert field_validation, "Elements are not displayed as expected."

    login_page.login(login_details["valid_username"],login_details["invalid_password"])

    #Error message validation
    error=login_page.get_error_message()

    assert error is not None, "Error message is not displayed."

# Test Case 2 - Validation of successful, Submit button and Logout Functionality
def test_successfullogin_submitbutton_logout(page,login_details):
    #Instance of Zenlogin and Dashboard page
    login_page = Zenlogin(page)
    dashboard_page = Dashboard(page)

    # Login
    login_page.login(login_details["valid_username"],login_details["valid_password"])

    #assertion
    assert "Welcome," in dashboard_page.get_welcome_message()

    #Logout
    logout = dashboard_page.click_logout()

    #assertion
    assert logout, "Logout button is not working"

# Testcase 3 - Unsuccessful Login
def test_unsuccessful_login(page,login_details):
    #Instance of Zenlogin Page
    login_page = Zenlogin(page)

    login_page.login(login_details["invalid_username"],login_details["invalid_password"])

    #Getting error message from page
    error = login_page.get_error_message()

    # assertions
    assert error is not None, "Error message is not displayed"

    assert "Invalid" or "Incorrect" in error