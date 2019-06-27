import os


class RemovalService:
    """
    A service for removing objects from the filesystem.
    """
    def __init__(self):
        pass

    def rm(self, filename):
        if os.path.isfile(filename):
            os.remove(filename)
            return

class UploadService:
    def __init__(self, removal_service):
        self.removal_service = removal_service

    def refresh(self):
        print('refresh')

    def upload_complete(self, filename):
        self.refresh()

        self.removal_service.rm(filename)
