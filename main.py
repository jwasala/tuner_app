from models.stream import Stream, TuningStatus
from models.tunings import TUNINGS
import sys
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt, Signal)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                           QRadialGradient)
from PySide2.QtWidgets import *





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
                                        "	background: rgba(237, 37, 78, 0.3);\n"
                                        "	border: 1px solid rgba(237, 37, 78, 0.5);\n"
                                        "	border-radius: 16px;\n"
                                        "	font: 14px 'Montserrat';\n"
                                        "	font-weight: 450;\n"
                                        "	margin: 5px;\n"
                                        "	padding: 8px 5px;\n"
                                        "}\n"
                                        "#buttons_grid QPushButton:pressed {\n"
                                        "	background: rgba(237, 37, 78, 0.8);\n"
                                        "}")
        self.buttons = QVBoxLayout(self.buttons_grid)
        self.buttons.setObjectName(u"buttons")
        self.buttons_row1 = QHBoxLayout()
        self.buttons_row1.setObjectName(u"buttons_row1")

        self.guitar_st = QPushButton(self.buttons_grid)
        self.guitar_st.setObjectName(u"guitar_st")

        self.buttons_row1.addWidget(self.guitar_st)
        self.ukulele_soprano = QPushButton(self.buttons_grid)
        self.ukulele_soprano.setObjectName(u"ukulele_soprano")

        self.buttons_row1.addWidget(self.ukulele_soprano)

        self.guitar_half_down = QPushButton(self.buttons_grid)
        self.guitar_half_down.setObjectName(u"guitar_half_down")

        self.buttons_row1.addWidget(self.guitar_half_down)

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

        self.strings_grid = QWidget(self.centralwidget)
        self.strings_grid.setObjectName(u"strings_grid")
        self.strings_grid.setGeometry(QRect(50, 304, 601, 126))
        self.strings_grid.setStyleSheet(u"#strings_grid QPushButton {\n"
                                        "	background: rgba(98, 139, 72, 0.3);\n"
                                        "	border: 1px solid rgb(98, 139, 72);\n"
                                        "	border-radius: 17px;\n"
                                        "	font: 14px 'Montserrat';\n"
                                        "	font-weight: 450;\n"
                                        "	margin: 15px;\n"
                                        "	padding: 10px;\n"
                                        "}")

        self.strings = QHBoxLayout(self.strings_grid)
        self.strings.setObjectName(u"strings")
        self.strings.setContentsMargins(9, 9, 9, 9)
        self.string_1 = QPushButton(self.strings_grid)
        self.string_1.setObjectName(u"string_1")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.string_1.sizePolicy().hasHeightForWidth())
        self.string_1.setSizePolicy(sizePolicy)

        self.strings.addWidget(self.string_1)

        self.string_2 = QPushButton(self.strings_grid)
        self.string_2.setObjectName(u"string_2")
        sizePolicy.setHeightForWidth(self.string_2.sizePolicy().hasHeightForWidth())
        self.string_2.setSizePolicy(sizePolicy)

        self.strings.addWidget(self.string_2)

        self.string_3 = QPushButton(self.strings_grid)
        self.string_3.setObjectName(u"string_3")
        sizePolicy.setHeightForWidth(self.string_3.sizePolicy().hasHeightForWidth())
        self.string_3.setSizePolicy(sizePolicy)

        self.strings.addWidget(self.string_3)

        self.string_4 = QPushButton(self.strings_grid)
        self.string_4.setObjectName(u"string_4")
        sizePolicy.setHeightForWidth(self.string_4.sizePolicy().hasHeightForWidth())
        self.string_4.setSizePolicy(sizePolicy)

        self.strings.addWidget(self.string_4)

        self.string_5 = QPushButton(self.strings_grid)
        self.string_5.setObjectName(u"string_5")
        sizePolicy.setHeightForWidth(self.string_5.sizePolicy().hasHeightForWidth())
        self.string_5.setSizePolicy(sizePolicy)

        self.strings.addWidget(self.string_5)

        self.string_6 = QPushButton(self.strings_grid)
        self.string_6.setObjectName(u"string_6")
        sizePolicy.setHeightForWidth(self.string_6.sizePolicy().hasHeightForWidth())
        self.string_6.setSizePolicy(sizePolicy)

        self.strings.addWidget(self.string_6)

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
        self.string_1.setText(QCoreApplication.translate("MainWindow", u"E2", None))
        self.string_2.setText(QCoreApplication.translate("MainWindow", u"A2", None))
        self.string_3.setText(QCoreApplication.translate("MainWindow", u"D3", None))
        self.string_4.setText(QCoreApplication.translate("MainWindow", u"G3", None))
        self.string_5.setText(QCoreApplication.translate("MainWindow", u"B3", None))
        self.string_6.setText(QCoreApplication.translate("MainWindow", u"E4", None))


def main():
    app = QApplication()
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

        if len(ts.strings) == 4:
            win.string_1.hide()
            win.string_6.hide()

            i = 2
            for (pitch, freq) in ts.strings:
                getattr(win, f'string_{i}').setText(str(pitch))
                getattr(win, f'string_{i}').setStyleSheet(u"#string_" + str(i) + " {\n"
                                        "	background: qlineargradient(spread:pad, x1:0.5, y1:" + "%.2f" % (1 - freq) + ", x2:0.5, y2:1, stop:0 rgba(98, 139, 72, 0.3), stop:0.001 rgba(98, 139, 72, 1));\n"
                                        "}")
                i += 1

        if len(ts.strings) == 6:
            win.string_1.show()
            win.string_6.show()

            i = 1
            for (pitch, freq) in ts.strings:
                getattr(win, f'string_{i}').setText(str(pitch))
                getattr(win, f'string_{i}').setStyleSheet(u"#string_" + str(i) + " {\n"
                                        "	background: qlineargradient(spread:pad, x1:0.5, y1:" + "%.2f" % (1 - freq) + ", x2:0.5, y2:1, stop:0 rgba(98, 139, 72, 0.3), stop:0.001 rgba(98, 139, 72, 1));\n"
                                        "}")
                i += 1

    stream = Stream(update_view)
    stream.start()

    def on_guitar_st_click(but):
        return stream.update_instrument(TUNINGS['guitar standard'])

    def on_guitar_half_down_click(but):
        return stream.update_instrument(TUNINGS['guitar half-step down'])

    def on_mandolin_standard_click(but):
        return stream.update_instrument(TUNINGS['mandolin standard'])

    def on_ukulele_soprano_click(but):
        return stream.update_instrument(TUNINGS['soprano ukulele'])

    def on_ukulele_baritone_click(but):
        return stream.update_instrument(TUNINGS['baritone ukulele'])

    def on_bass_four_string(but):
        return stream.update_instrument(TUNINGS['4-string bass'])

    win.guitar_st.clicked.connect(on_guitar_st_click)
    win.guitar_half_down.clicked.connect(on_guitar_half_down_click)
    win.mandolin_standard.clicked.connect(on_mandolin_standard_click)
    win.ukulele_soprano.clicked.connect(on_ukulele_soprano_click)
    win.ukulele_baritone.clicked.connect(on_ukulele_baritone_click)
    win.bass_four_string.clicked.connect(on_bass_four_string)

    try:
        sys.exit(app.exec_())
    except:
        print('Exiting')


if __name__ == '__main__':
    sys._excepthook = sys.excepthook

    def my_exception_hook(exctype, value, traceback):
        # Print the error and traceback
        print(exctype, value, traceback)
        # Call the normal Exception hook after
        sys._excepthook(exctype, value, traceback)
        sys.exit(1)


    # Set the exception hook to our wrapping function
    sys.excepthook = my_exception_hook

    main()
