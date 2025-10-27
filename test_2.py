from ftplib import print_line

import pytest


@pytest.fixture

def browser():
    print('explorer')

    yield browser

    print('quit browser')
    pass

@pytest.fixture
def login_page(browser):
    print('login')
    pass

@pytest.fixture
def user():
    return 'username', 'password'



def test_login(login_page, user):
    username, password = user
    print(username, '3')
    assert password == 'password'
    assert username == 'username'







