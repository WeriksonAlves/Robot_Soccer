from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from data_acquisition.camera import Camera
from data_acquisition.image_processing import ImageProcessor

class DataAcquisitionTab(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        
        self.camera_label = QLabel("Camera Feed")
        self.layout.addWidget(self.camera_label)
        
        self.capture_button = QPushButton("Capture Image")
        self.capture_button.clicked.connect(self.capture_image)
        self.layout.addWidget(self.capture_button)
        
        self.setLayout(self.layout)
        self.camera = Camera()
        self.image_processor = ImageProcessor()

    def capture_image(self):
        image = self.camera.capture_image()
        field_info, robots_info, ball_info = self.image_processor.extract_info(image)
        self.update_ui(field_info, robots_info, ball_info)
        
    def update_ui(self, field_info, robots_info, ball_info):
        # Update the UI with the extracted information
        pass
