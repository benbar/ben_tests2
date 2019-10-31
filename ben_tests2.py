import datetime
import pytest
from time import sleep

from apps.hbonweb.pages.loginform_page import LoginForm, AdultKidsSelection
from apps.hbonweb.pages.home_page import Home, WhyHBO
from apps.hbonweb.flows.login_flow import login
from apps.hbonshared.resourcesmanager import ResourcesManager
from apps.hbonweb.pages.kids_page import Kids
from apps.hbonweb.pages.myaccount_page import MyAccount
from apps.hbonweb.pages.watchlist_page import Watchlist
from helpers.configmanager import ConfigManager

cm = ConfigManager()

@pytest.mark.env("prod", "preprod")
@pytest.mark.category("smoke", "deploy")
@pytest.mark.id("Cxxx")
def test_login_logout_success(driver, user):
    """C419: Be able to login with valid credentials

    https://hbo.testrail.com/index.php?/cases/view/419
    """
    # to force non-cached version // deploy
    dt = str(datetime.datetime.now()).replace(" ", "_")
    driver.helper.go_to_url(f"{cm.url}/{dt}")
    sleep(1)

    page = login(driver, user.email, user.password)
    page.click_on_kids_link()

    page = Kids(driver)
    page.click_on_got_it_alert_button()
    page.click_on_watchlist_link()

    page = Watchlist(driver)
    page.click_on_home_logged_in_link()

    page = Home(driver)
    page.click_on_my_account_link()

    page = MyAccount(driver)
    page.click_on_sign_out_link()

    page = WhyHBO(driver)
    assert page.is_sign_in_link_displayed()
    assert page.is_why_hbo_active_link_displayed()