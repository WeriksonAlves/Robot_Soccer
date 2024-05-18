import cv2

class ImageProcessor:
    def extract_info(self, image):
        field_info = self.detect_field(image)
        robots_info = self.detect_robots(image)
        ball_info = self.detect_ball(image)
        return field_info, robots_info, ball_info
    
    def detect_field(self, image):
        # Logic to detect field
        pass
    
    def detect_robots(self, image):
        # Logic to detect robots
        pass
    
    def detect_ball(self, image):
        # Logic to detect ball
        pass
