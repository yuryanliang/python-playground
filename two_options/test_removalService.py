from unittest import TestCase, mock
from unittest.mock import patch

from remove_service import RemovalService


class TestRemovalService(TestCase):

    @mock.patch('remove_service.os.path')
    @mock.patch('remove_service.os')
    def test_rm(self, mock_os, mock_path):
        # instantiate our service
        reference = RemovalService()

        # set up the mock
        mock_path.isfile.return_value = False

        reference.rm("any path")

        # test that the remove call was NOT called.
        self.assertFalse(mock_os.remove.called, "Failed to not remove the file if not present.")

        # make the file 'exist'
        mock_path.isfile.return_value = True

        reference.rm("any path")

        mock_os.remove.assert_called_with("any path")
