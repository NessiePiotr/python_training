
def test_del_first_address(app):
    app.session.login(username="admin", password="secret")
    app.address.delete_first_address()
    app.session.logout()