import unittest
from data_acquisition.camera import Camera

class TestCamera(unittest.TestCase):
    def test_capture_image(self):
        camera = Camera()
        image = camera.capture_image()
        self.assertIsNotNone(image)

if __name__ == '__main__':
    unittest.main()
