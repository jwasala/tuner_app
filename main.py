from models.stream import Stream, TuningStatus
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                           QRadialGradient)
from PySide2.QtWidgets import *
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 600)
        MainWindow.setMinimumSize(QSize(700, 600))
        MainWindow.setMaximumSize(QSize(700, 700))
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#centralwidget {\n"
                                         "	background: #011936;\n"
                                         "}\n"
                                         "\n"
                                         "* {\n"
                                         "	color: #ffffff;\n"
                                         "}")
        self.closest_pitch = QLabel(self.centralwidget)
        self.closest_pitch.setObjectName(u"closest_pitch")
        self.closest_pitch.setGeometry(QRect(50, 200, 601, 76))
        font = QFont()
        font.setFamily(u"Montserrat Black")
        font.setPointSize(48)
        self.closest_pitch.setFont(font)
        self.closest_pitch.setStyleSheet(u"#closest_pitch {\n"
                                         "	background: #ECBC4C;\n"
                                         "	font-family: 'Montserrat Black';\n"
                                         "}")
        self.closest_pitch.setAlignment(Qt.AlignCenter)
        self.freq = QLabel(self.centralwidget)
        self.freq.setObjectName(u"freq")
        self.freq.setGeometry(QRect(50, 50, 601, 126))
        font1 = QFont()
        font1.setFamily(u"Montserrat")
        font1.setBold(700)
        font1.setPointSize(90)
        self.freq.setFont(font1)
        self.freq.setStyleSheet(u"#freq {\n"
                                "	background: qlineargradient(spread:pad, x1:0.5, y1:0.45, x2:0.5, y2:1, stop:0 rgba(31, 31, 31, 0), stop:0.001 rgba(237, 37,78, 255))\n"
                                "}")
        self.freq.setAlignment(Qt.AlignCenter)
        self.buttons_grid = QWidget(self.centralwidget)
        self.buttons_grid.setObjectName(u"buttons_grid")
        self.buttons_grid.setGeometry(QRect(50, 425, 601, 126))
        self.buttons_grid.setStyleSheet(u"#buttons_grid QPushButton {\n"
                                        "	background: rgba(237, 37, 78, 1);\n"
                                        "	border: 0;\n"
                                        "	border-radius: 10px;\n"
                                        "	font: 15px 'Montserrat';\n"
                                        "	font-weight: 450;\n"
                                        "	margin: 5px;\n"
                                        "	padding: 3px 5px;\n"
                                        "}\n"
                                        "#buttons_grid QPushButton:pressed {\n"
                                        "	background: rgba(237, 37, 78, 0.8);\n"
                                        "}")
        self.buttons = QVBoxLayout(self.buttons_grid)
        self.buttons.setObjectName(u"buttons")
        self.buttons_row1 = QHBoxLayout()
        self.buttons_row1.setObjectName(u"buttons_row1")
        self.ukulele_soprano = QPushButton(self.buttons_grid)
        self.ukulele_soprano.setObjectName(u"ukulele_soprano")

        self.buttons_row1.addWidget(self.ukulele_soprano)

        self.guitar_half_down = QPushButton(self.buttons_grid)
        self.guitar_half_down.setObjectName(u"guitar_half_down")

        self.buttons_row1.addWidget(self.guitar_half_down)

        self.guitar_st = QPushButton(self.buttons_grid)
        self.guitar_st.setObjectName(u"guitar_st")

        self.buttons_row1.addWidget(self.guitar_st)

        self.buttons.addLayout(self.buttons_row1)

        self.buttons_row2 = QHBoxLayout()
        self.buttons_row2.setObjectName(u"buttons_row2")
        self.mandolin_standard = QPushButton(self.buttons_grid)
        self.mandolin_standard.setObjectName(u"mandolin_standard")

        self.buttons_row2.addWidget(self.mandolin_standard)

        self.bass_four_string = QPushButton(self.buttons_grid)
        self.bass_four_string.setObjectName(u"bass_four_string")

        self.buttons_row2.addWidget(self.bass_four_string)

        self.ukulele_baritone = QPushButton(self.buttons_grid)
        self.ukulele_baritone.setObjectName(u"ukulele_baritone")

        self.buttons_row2.addWidget(self.ukulele_baritone)

        self.buttons.addLayout(self.buttons_row2)

        self.over_tone = QFrame(self.centralwidget)
        self.over_tone.setObjectName(u"over_tone")
        self.over_tone.setGeometry(QRect(0, 0, 0, 0))
        self.over_tone.setAutoFillBackground(True)
        self.over_tone.setStyleSheet(u"#over_tone {\n"
                                     "	color: rgb(98, 139, 72);\n"
                                     "}")
        self.over_tone.setFrameShadow(QFrame.Plain)
        self.over_tone.setLineWidth(20)
        self.over_tone.setFrameShape(QFrame.HLine)
        self.under_tone = QFrame(self.centralwidget)
        self.under_tone.setObjectName(u"under_tone")
        self.under_tone.setGeometry(QRect(0, 0, 0, 0))
        self.under_tone.setAutoFillBackground(True)
        self.under_tone.setStyleSheet(u"#under_tone {\n"
                                      "	color: rgba(237, 37,78, 255);\n"
                                      "}")
        self.under_tone.setFrameShadow(QFrame.Plain)
        self.under_tone.setLineWidth(20)
        self.under_tone.setFrameShape(QFrame.HLine)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Tuner", None))
        self.closest_pitch.setText(QCoreApplication.translate("MainWindow", u"A4", None))
        self.freq.setText(QCoreApplication.translate("MainWindow", u"440.0 Hz", None))
        self.ukulele_soprano.setText(QCoreApplication.translate("MainWindow", u"Soprano ukulele", None))
        self.guitar_half_down.setText(QCoreApplication.translate("MainWindow", u"Guitar half-step down", None))
        self.guitar_st.setText(QCoreApplication.translate("MainWindow", u"Guitar standard", None))
        self.mandolin_standard.setText(QCoreApplication.translate("MainWindow", u"Mandolin standard", None))
        self.bass_four_string.setText(QCoreApplication.translate("MainWindow", u"4-string bass", None))
        self.ukulele_baritone.setText(QCoreApplication.translate("MainWindow", u"Baritone ukulele", None))


def main():
    app = QApplication(sys.argv)
    win = Ui_MainWindow()
    w = QMainWindow()
    win.setupUi(w)
    w.show()

    def update_view(ts: TuningStatus) -> None:
        print(ts.closest_pitch, ts.freq, 'Hz', f'({ts.freq_diff})', [(str(p), b) for (p, b) in ts.strings])
        win.freq.setText(str(int(ts.freq)) + ' Hz')
        win.closest_pitch.setText(str(ts.closest_pitch))

        if ts.freq_diff == 0:
            win.over_tone.resize(0, win.over_tone.height())
            win.under_tone.resize(0, win.under_tone.height())

        if ts.freq_diff > 0:
            win.over_tone.setGeometry(350, 276, int(301 * abs(ts.freq_diff_normalized)), 20)
            win.under_tone.resize(0, win.under_tone.height())

        if ts.freq_diff < 0:
            win.under_tone.setGeometry(50 + (301 - int(301 * abs(ts.freq_diff_normalized))), 276,
                                       int(301 * abs(ts.freq_diff_normalized)), 20)
            win.over_tone.resize(0, win.under_tone.height())

    stream = Stream(update_view)
    stream.start()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
