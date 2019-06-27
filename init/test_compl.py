from unittest import TestCase

from unittest import mock
from complex import Compl

class TestCompl(TestCase):
    def test_simple(self):
        with mock.patch.object(Compl, "__init__", lambda x, y, z: None):
            c = Compl(None, None)
            c.var1 = 0
            assert c.simple(1) is None
