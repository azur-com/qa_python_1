import pytest


@pytest.fixture
def browser_x():
    print('explorer')

    yield browser_x

    print('quit browser')
    pass

@pytest.fixture
def login_page(browser_x):
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
    print("{a}, {b}".format(a=password,b=username))
    print("email.my.com {} {}".format("groups", "users"))










