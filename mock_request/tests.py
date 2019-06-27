import unittest
import mock

from main import do_session_get


class TestDoSessionGet(unittest.TestCase):
    @mock.patch('main.requests.session')
    def test_should_mock_session_get(self, session_mock):
        session_mock.return_value = mock.MagicMock(get=mock.MagicMock(return_value='bar'))
        self.assertEqual(do_session_get(), 'bar')


if __name__ == '__main__':
    unittest.main()
