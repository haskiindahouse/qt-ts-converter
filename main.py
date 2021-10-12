import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from ui import Ui


def initUi():
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.png"))

    ex = Ui()

    sys.exit(app.exec_())


if __name__ == '__main__':
    initUi()
