""" entry point """
import logging
import sys

from ui.main_window import MainWindow
from PyQt5.Qt import QApplication

import config

logging.basicConfig(level=config.LOGGING_LEVEL)



app = QApplication(sys.argv)
window = MainWindow()
window.show()

sys.exit(app.exec_())
