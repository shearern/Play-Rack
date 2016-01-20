# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PlayerWindow.ui'
#
# Created: Tue Jan 19 19:57:33 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_PlayerWindow(object):
    def setupUi(self, PlayerWindow):
        PlayerWindow.setObjectName("PlayerWindow")
        PlayerWindow.resize(363, 306)
        self.centralwidget = QtGui.QWidget(PlayerWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.device_label = QtGui.QLabel(self.centralwidget)
        self.device_label.setObjectName("device_label")
        self.verticalLayout.addWidget(self.device_label)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.detail_box = QtGui.QLabel(self.centralwidget)
        self.detail_box.setObjectName("detail_box")
        self.horizontalLayout_2.addWidget(self.detail_box)
        self.eject_btn = QtGui.QPushButton(self.centralwidget)
        self.eject_btn.setObjectName("eject_btn")
        self.horizontalLayout_2.addWidget(self.eject_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fade_in_btn = QtGui.QPushButton(self.centralwidget)
        self.fade_in_btn.setObjectName("fade_in_btn")
        self.horizontalLayout.addWidget(self.fade_in_btn)
        self.stop_btn = QtGui.QPushButton(self.centralwidget)
        self.stop_btn.setObjectName("stop_btn")
        self.horizontalLayout.addWidget(self.stop_btn)
        self.play_btn = QtGui.QPushButton(self.centralwidget)
        self.play_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/open-iconic-master/png/media-play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play_btn.setIcon(icon)
        self.play_btn.setObjectName("play_btn")
        self.horizontalLayout.addWidget(self.play_btn)
        self.fade_out_btn = QtGui.QPushButton(self.centralwidget)
        self.fade_out_btn.setObjectName("fade_out_btn")
        self.horizontalLayout.addWidget(self.fade_out_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.pos_scroll = QtGui.QScrollBar(self.centralwidget)
        self.pos_scroll.setOrientation(QtCore.Qt.Horizontal)
        self.pos_scroll.setObjectName("pos_scroll")
        self.verticalLayout.addWidget(self.pos_scroll)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.vol_scroll = QtGui.QScrollBar(self.centralwidget)
        self.vol_scroll.setOrientation(QtCore.Qt.Vertical)
        self.vol_scroll.setObjectName("vol_scroll")
        self.horizontalLayout_3.addWidget(self.vol_scroll)
        PlayerWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(PlayerWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 363, 21))
        self.menubar.setObjectName("menubar")
        PlayerWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(PlayerWindow)
        self.statusbar.setObjectName("statusbar")
        PlayerWindow.setStatusBar(self.statusbar)

        self.retranslateUi(PlayerWindow)
        QtCore.QMetaObject.connectSlotsByName(PlayerWindow)

    def retranslateUi(self, PlayerWindow):
        PlayerWindow.setWindowTitle(QtGui.QApplication.translate("PlayerWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.device_label.setText(QtGui.QApplication.translate("PlayerWindow", "Device Label", None, QtGui.QApplication.UnicodeUTF8))
        self.detail_box.setText(QtGui.QApplication.translate("PlayerWindow", "Info Box", None, QtGui.QApplication.UnicodeUTF8))
        self.eject_btn.setText(QtGui.QApplication.translate("PlayerWindow", "Eject", None, QtGui.QApplication.UnicodeUTF8))
        self.fade_in_btn.setText(QtGui.QApplication.translate("PlayerWindow", "Fade In", None, QtGui.QApplication.UnicodeUTF8))
        self.stop_btn.setText(QtGui.QApplication.translate("PlayerWindow", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.fade_out_btn.setText(QtGui.QApplication.translate("PlayerWindow", "Fade Out", None, QtGui.QApplication.UnicodeUTF8))

import ui_resources_rc
