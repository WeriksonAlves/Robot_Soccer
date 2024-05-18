import cv2

class Camera:
    def __init__(self, camera_id=0):
        self.camera_id = camera_id
        self.cap = cv2.VideoCapture(self.camera_id)
        
    def capture_image(self):
        ret, frame = self.cap.read()
        if not ret:
            raise Exception("Failed to capture image from camera")
        return frame
