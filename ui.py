import webbrowser

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QTextCodec

from converter import xlsxToXml, xmlToQtTs


class Ui(QWidget):

    def __init__(self):
        super().__init__()
        QTextCodec.setCodecForLocale(QTextCodec.codecForName("Windows-1251"))

        self.filePath = None

        self.initUi()

    def initUi(self):
        self.verticalLayout = QVBoxLayout(self)
        self.gridLayout = QGridLayout(self)
        appLogo = QPixmap('icon.png').scaled(64, 64)
        gitHubLogo = QPixmap('github-logo.png').scaled(64, 64)
        labelWithLogo = QLabel(self)
        labelWithLogo.setPixmap(appLogo)

        labelWithName = QLabel(self)
        labelWithName.setText("QtTranslate-Helper")
        labelWithName.setStyleSheet("QLabel { color : grey; font-size: 36px}")

        btnWithGitHubLogo = QPushButton(self)
        labelWithGitHubRef = QLabel(self)
        labelWithGitHubRef.setOpenExternalLinks(True)
        labelWithGitHubRef.setText("<a href=\"https://github.com/haskiindahouse\">GitHub</a>")
        labelWithGitHubRef.setStyleSheet("QLabel { color : black; font: bold; font-size: 36px}")

        btnWithGitHubLogo.setIcon(QIcon(gitHubLogo))
        btnWithGitHubLogo.setIconSize(gitHubLogo.rect().size())
        btnWithGitHubLogo.clicked.connect(self.openHref)


        btnBrowse = QPushButton(self)
        btnBrowse.setStyleSheet("QPushButton {border: 1px  solid dark-blue; font-size: 24px}")
        btnBrowse.setFixedSize(200, 50)
        btnBrowse.setText("Browse")
        btnBrowse.clicked.connect(self.openFile)

        self.pathToFile = QTextEdit(self)
        self.pathToFile.setReadOnly(True)
        self.pathToFile.setText("Path to file")
        self.pathToFile.setFixedSize(400, 50)
        self.pathToFile.setStyleSheet("QTextEdit {font: bold; font-size: 18px; color: grey;}")

        btnConvertToXml = QPushButton(self)
        btnConvertToXml.setStyleSheet("QPushButton {border: 1px  solid dark-blue; font-size: 24px}")
        btnConvertToXml.setFixedSize(200, 50)
        btnConvertToXml.setText("Convert to .XML")
        btnConvertToXml.clicked.connect(self.convertFromXlsxToXml)

        btnConvertToQTs = QPushButton(self)
        btnConvertToQTs.setStyleSheet("QPushButton {border: 1px  solid dark-blue; font-size: 24px}")
        btnConvertToQTs.setFixedSize(200, 50)
        btnConvertToQTs.setText("Convert to .TS")
        btnConvertToQTs.clicked.connect(self.convertFromXmlToQTs)

        self.customLog = QPlainTextEdit(self)
        self.customLog.setStyleSheet("""
             QPlainTextEdit
             {
             background-color: #b1b1b1;
             color: #202020;
             border: 1px solid #031582;
             selection-background-color: #505050;
             selection-color: #ACDED5;
             }
             QMenu
             {
             background: #F2F2F2;
             color: #0E185F;
             border: 1px solid #000;
             selection-background-color: #ACDED5;
            
             } 
                 """)

        self.customLog.setReadOnly(True)
        self.customLog.blockCountChanged.connect(self.logAutoClear)

        self.gridLayout.addWidget(labelWithLogo, 0, 0, Qt.AlignLeft)
        self.gridLayout.addWidget(labelWithName, 0, 1, Qt.AlignLeft)
        self.gridLayout.addWidget(btnWithGitHubLogo, 0, 2, Qt.AlignRight)
        self.gridLayout.addWidget(labelWithGitHubRef, 0, 3, Qt.AlignRight)
        self.gridLayout.addWidget(btnBrowse, 1, 0, Qt.AlignLeft)
        self.gridLayout.addWidget(self.pathToFile, 1, 1, Qt.AlignLeft)
        self.gridLayout.addWidget(btnConvertToXml, 2, 0, Qt.AlignLeft)
        self.gridLayout.addWidget(btnConvertToQTs, 2, 1, Qt.AlignLeft)
        self.gridLayout.setColumnStretch(1, 1)

        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout.addWidget(self.customLog)
        self.move(300, 300)
        self.setWindowTitle('QtTranslate-Helper')
        self.setWindowIcon(QIcon('icon.png'))

        self.resize(750, 750)
        self.show()

    def openHref(self):
        self.customLog.appendPlainText("Open ref to github profile...")
        webbrowser.open("https://github.com/haskiindahouse")

    def openFile(self):
        self.customLog.appendPlainText("Start open the file...")

        self.filePath, _ = QFileDialog.getOpenFileName(self,
                                                   'Open file with transcription',
                                                   './',
                                                   'Transcription (*.xlsx;*.xml)')
        if self.filePath is not None and self.filePath:
            self.pathToFile.setText(self.filePath)
            self.removeFileType()
            self.customLog.appendPlainText("File opened...")
        else:
            self.customLog.appendPlainText("File not opened...")

    def convertFromXlsxToXml(self):
        if self.filePath is not None and self.filePath:
            self.customLog.appendPlainText("Start converting to xml...")
            xlsxToXml(self.filePath)
            self.customLog.appendPlainText("To XMl converted successfully...")

        else:
            self.customLog.appendPlainText("File not opened...")

    def convertFromXmlToQTs(self):
        if self.filePath is not None and self.filePath:
            self.customLog.appendPlainText("Start converting to ts...")
            xmlToQtTs(self.filePath)
        else:
            self.customLog.appendPlainText("File not opened...")

    def logAutoClear(self):
        blockCount = self.customLog.blockCount()
        if blockCount > 10:
            self.customLog.clear()

    def removeFileType(self):
        self.filePath = self.filePath.replace('.xlsx', '')
        self.filePath = self.filePath.replace('.XLSX', '')
        self.filePath = self.filePath.replace('.xml', '')
