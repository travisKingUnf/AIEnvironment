__author__ = 'travi_000'

print("High Level Wrapper Not Initialized")


class HighLevel(object):
    def __init__(self):
        # constructor object for all high level processes
        self.CameraManagement = CameraManagement()


class CameraManagement(object):
    def __init__(self):
        # constructor object for the management of the camera
        self.placeholder = False

