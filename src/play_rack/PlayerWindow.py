

import sys

from PySide.QtGui import QMainWindow, QPushButton, QApplication, QFontDatabase, QFont

from .ui.PlayerWindow import Ui_PlayerWindow

class PlayerWindow(QMainWindow, Ui_PlayerWindow):

    def __init__(self, parent=None):
        super(PlayerWindow, self).__init__(parent)
        self.setupUi(self)

        self.font_db = QFontDatabase()

        font_id = self.font_db.addApplicationFont(":/fonts/assets/font/black_jack.ttf")
        if font_id != -1:
            self.black_jack = QFont(self.font_db.applicationFontFamilies(font_id)[0])
            self.black_jack.setPointSize(12)

            self.device_label.setFont(self.black_jack)

        font_id = self.font_db.addApplicationFont(":/fonts/assets/font/LiquidCrystal-Normal.ttf")
        if font_id != -1:
            self.lcd_font = QFont(self.font_db.applicationFontFamilies(font_id)[0])
            self.lcd_font.setPointSize(8)

            self.title.setFont(self.lcd_font)
            self.filename.setFont(self.lcd_font)
            self.time_pos.setFont(self.lcd_font)
            self.time_of.setFont(self.lcd_font)
            self.time_dur.setFont(self.lcd_font)






