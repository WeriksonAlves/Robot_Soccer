import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Robot Soccer Control')
        self.setGeometry(100, 100, 800, 600)
        
        self.tab_widget = QTabWidget()
        self.setCentralWidget(self.tab_widget)
        
        self.init_tabs()
        
    def init_tabs(self):
        from gui.tabs.data_acquisition_tab import DataAcquisitionTab
        from gui.tabs.control_tab import ControlTab

        self.tab_widget.addTab(DataAcquisitionTab(), "Data Acquisition")
        self.tab_widget.addTab(ControlTab(), "Control")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
