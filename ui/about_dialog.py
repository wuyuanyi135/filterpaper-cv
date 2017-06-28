""" about dialog """
from PyQt5.Qt import QDialog, QTextEdit, QVBoxLayout
from config import VERSION

class AboutDialog(QDialog):
    """ about dialog """
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        """init ui"""
        edit = QTextEdit(self)
        edit.setReadOnly(True)
        edit.setText("""
Version: {version}
Author: Yuanyi Wu (ywu647@uwo.ca)
repository: 
        """.format(version=VERSION))
        layout = QVBoxLayout(self)
        layout.addWidget(edit)
        self.setLayout(layout)
        