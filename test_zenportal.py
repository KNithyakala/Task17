import pytest

from Task17.POM.dashboard import Dashboard
from Task17.POM.login_ import Zenlogin
from Task17.conftest import login_details


def test_fields_validation(page,login_details):
    login_page= Zenlogin(page)

    field_validation = login_page.validate_fields()

    assert field_validation, "Elements are not displayed as expected."

    login_page.login(login_details["valid_username"],login_details["invalid_password"])

    error=login_page.get_error_message()

    assert error is not None, "Error message is not displayed."

def test_successfullogin_submitbutton_logout(page,login_details):
    login_page = Zenlogin(page)
    dashboard_page = Dashboard(page)

    # Login
    login_page.login(login_details["valid_username"],login_details["valid_password"])

    assert "Welcome," in dashboard_page.get_welcome_message()

    #Logout
    logout = dashboard_page.click_logout()

    # Logout
    assert logout, "Logout button is not working"

def test_unsuccessful_login(page,login_details):
    login_page = Zenlogin(page)

    login_page.login(login_details["invalid_username"],login_details["invalid_password"])

    error = login_page.get_error_message()

    assert error is not None, "Error message is not displayed"


    assert "Invalid" or "Incorrect" in error
