from nose.tools import *
from app import app

app.config["TESTING"] = True
web = app.test_client()


def test_indext():
    rv = web.get('/lol', follow_redirects=True)
    assert_equal(rv.status_code, 404)

    rv = web.get('/', follow_redirects=True)
    assert_equal(rv.status_code, 200)
    assert_in(b"Fill this out.", rv.data)

    data = {'name': 'Lol', 'greet': 'bonjourno'}
    rv = web.post('/', follow_redirects=True, data=data)
    assert_in(b"Lol", rv.data)
    assert_in(b"bonjourno", rv.data)
