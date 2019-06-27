from unittest import TestCase
from . import main

class TestHello(TestCase):
    def test_hello(self):
        hello=main.Hello()
        self.assertEqual(hello.hello(), 'hello')

    def test_double(self):
        hello=main.Hello()
        self.assertEqual(hello.__double__(), 'hellohello')
    def test_get(self):
        hello=main.Hello()
        self.assertEqual(hello.__get__(), 'h')
