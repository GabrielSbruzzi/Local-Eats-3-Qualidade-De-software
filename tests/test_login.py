from login import login

def test_login_sucesso():
    assert login("admin", "123") == True

def test_login_falha():
    assert login("user", "errado") == False
