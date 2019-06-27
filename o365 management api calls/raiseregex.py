import unittest

class MyError(Exception):
    def __init__(self,message,error_code):
        super(MyError, self).__init__(message)

        self._error_code = error_code

    @classmethod
    def from_response(cls):
        message='"404","ss"'
        error_code= '77'
        return cls(message,error_code)

def raiseError():
    raise MyError.from_response()

class TestStuff(unittest.TestCase):
    def testError(self):
        self.assertRaisesRegex(MyError, '"404","ss"',raiseError)

# unittest.main()


