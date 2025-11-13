from selene import browser, have

import pytest


@pytest.fixture
def test_success_login():
    browser.open_url('https://niffler.qa.guru')
    browser.element('[id="username"]').type('stas')
    browser.element('[id="password"]').type('12345')
    browser.element('[id="login-button"]').click()

    browser.element('[id="spendings"]').should(have.text('History of Spendings'))
    #browser.quit()

@pytest.fixture
def test_success_login_with_press_enter():
    browser.open_url('https://niffler.qa.guru')
    browser.element('[id="username"]').type('stas')
    browser.element('[id="password"]').type('12345').press_enter()

    browser.element('[id="spendings"]').should(have.text('History of Spendings'))
    #browser.quit()

def run_test():
    test_success_login()
    test_success_login_with_press_enter()


