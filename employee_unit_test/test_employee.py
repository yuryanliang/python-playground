from unittest import TestCase
from unittest.mock import patch, Mock

from employee_unit_test.employee import Employee


class TestEmployee(TestCase):
    def test_monthly_schedule(self):
        employee = Employee('Tom', 'Grady', 500)

        # with patch.object(requests.get)
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok= True
            mocked_get.return_value.text = 'Success'

            schedule = employee.monthly_schedule('Jan')
            mocked_get.assert_called_with('http://company.com/Grady/Jan')

            self.assertEqual(schedule, 'Success')


    def test_monthly_schedule_mock(self):
        employee= Employee('Tom', 'Grady', 500)
        mock_request_get=Mock()
        schedule =employee.monthly_schedule('Jan')
        print ()