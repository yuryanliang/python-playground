import requests


def do_session_get():
    session = requests.session()
    return session.get('foo')
