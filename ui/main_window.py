""" main window class """
import os
from PyQt5.Qt import QMainWindow, QAction, QFileDialog, QErrorMessage, QImage
from ui.about_dialog import AboutDialog
from cv.image_processor import ImageProcessor


class MainWindow(QMainWindow):
    """main window"""

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.processor = ImageProcessor()

    def init_ui(self):
        """set size and initialize the interface """
        self.setMinimumSize(600, 600)
        self.setWindowTitle("Computer Vision Filter Paper Reader")
        self.init_menu()

    def init_menu(self):
        """initialzie menu"""
        loadAction = QAction("&Open", self)
        loadAction.triggered.connect(self.load_picture)

        aboutAction = QAction("&About", self)
        aboutAction.triggered.connect(self.show_about)

        menubar = self.menuBar()
        menubar.addAction(loadAction)
        menubar.addAction(aboutAction)

    def show_image(self, image):
        pass

    def show_about(self):
        """show about dialog"""
        aboutDialog = AboutDialog()
        aboutDialog.setModal(True)
        aboutDialog.exec_()

    def load_picture(self):
        """load file"""
        selected_file = QFileDialog().getOpenFileName(
            self,
            "Select Image File",
            os.getcwd(),
            "Image Files (*.png *.jpeg *.tif)"
        )[0]
        try:
            self.processor.load_file(selected_file)
        except IOError as identifier:
            QErrorMessage.showMessage("failed to load file " + selected_file)
