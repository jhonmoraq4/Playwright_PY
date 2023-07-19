from playwright.sync_api import Page
import pytest

#url = 'https://www.saucedemo.com'
#@pytest.mark.skip_browser("chromium") # para skip un browser
#@pytest.mark.only_browser("chromium") # para ejecutar en un solo browser
def test_title(page: Page):
    page.goto("/")
    assert page.title() == "Swag Labs"

def test_Inventory_Site(page: Page):
    page.goto("/inventory.html")
    assert page.inner_text('h3') == "Epic sadface: You can only access '/inventory.html' when you are logged in."