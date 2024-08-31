# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'comp.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QMainWindow, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1024, 600)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(200, 80, 468, 402))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.widget)
        self.label.setStyleSheet("background-color: blue; color: white")
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.file_selec = QPushButton(self.widget)
        self.file_selec.setObjectName(u"file_selec")

        self.verticalLayout.addWidget(self.file_selec)

        self.format_combo = QComboBox(self.widget)
        self.format_combo.setObjectName(u"format_combo")

        self.verticalLayout.addWidget(self.format_combo)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.compress = QPushButton(self.widget)
        self.compress.setObjectName(u"compress")

        self.horizontalLayout.addWidget(self.compress)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.file_selec2 = QPushButton(self.widget)
        self.file_selec2.setObjectName(u"file_selec2")

        self.verticalLayout_2.addWidget(self.file_selec2)

        self.decompress = QPushButton(self.widget)
        self.decompress.setObjectName(u"decompress")

        self.verticalLayout_2.addWidget(self.decompress)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Select a File or Folder to compress", None))
        self.file_selec.setText(QCoreApplication.translate("Form", u"Select File or Folder", None))
        self.compress.setText(QCoreApplication.translate("Form", u"Compress", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Select a file  to decompress", None))
        self.file_selec2.setText(QCoreApplication.translate("Form", u"Select compressed file", None))
        self.decompress.setText(QCoreApplication.translate("Form", u"Decompress", None))
    # retranslateUi

