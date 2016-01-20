#!/usr/bin/python

# Import PySide classes
import sys
from PySide.QtCore import *
from PySide.QtGui import *

from play_rack.PlayerWindow import PlayerWindow

if __name__ == '__main__':

    # Create a Qt application
    app = QApplication(sys.argv)

    window = PlayerWindow()
    window.show()

    # Enter Qt application main loop
    app.exec_()

    sys.exit()