from unittest import TestCase, mock

from remove_service import RemovalService, UploadService



class TestUploadService(TestCase):

    @mock.patch.object(UploadService,'refresh')
    @mock.patch.object(RemovalService, 'rm')
    def test_upload_complete(self, mock_rm,mock_refresh):
        # build our dependencies
        removal_service = RemovalService()
        reference = UploadService(removal_service)

        # call upload_complete, which should, in turn, call `rm`:
        reference.upload_complete("my uploaded file")

        # check that it called the rm method of any RemovalService
        mock_rm.assert_called_with("my uploaded filee")
        mock_refresh.assert_called_once()
        # reference.refresh.assert_called_twice()


    def test_upload_complete_1(self):

        with mock.patch.object(RemovalService,'rm') as mock_rm:
            # build our dependencies
            removal_service = RemovalService()
            reference = UploadService(removal_service)

            # call upload_complete, which should, in turn, call `rm`:
            reference.upload_complete("my uploaded file")

            # check that it called the rm method of any RemovalService
            mock_rm.assert_called_with("my uploaded file")

    def test_upload_complete_2(self):
        # build our dependencies
        mock_removal_service = mock.create_autospec(RemovalService)

        reference = UploadService(mock_removal_service(1))

        # call upload_complete, which should, in turn, call `rm`:
        reference.upload_complete("my uploaded file")

        # test that it called the rm method
        mock_removal_service.rm.assert_called_with("my uploaded file")