from pages.login_page import LoginPage

def test_login_valid_credentials(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("Admin", "admin123")

    # Assert that dashboard is loaded
    assert "dashboard" in driver.current_url.lower()
