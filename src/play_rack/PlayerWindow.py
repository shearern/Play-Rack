

import sys

from PySide.QtGui import QMainWindow, QPushButton, QApplication

from .ui.PlayerWindow import Ui_PlayerWindow

class PlayerWindow(QMainWindow, Ui_PlayerWindow):

    def __init__(self, parent=None):
        super(PlayerWindow, self).__init__(parent)
        self.setupUi(self)