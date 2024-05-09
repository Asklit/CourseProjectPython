import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog

from settings import SettingsWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.GoToSettings = None
        self.fileFlag = False
        self.fileNames = []
        uic.loadUi('uiMainFile.ui', self)  # Открытие файла ui

        self.LEErrorLine.hide()

        # Привязки функций к кнопкам
        self.btnChooseFile.clicked.connect(self.chooseFile)     # Кнопка выбора файла
        self.btnRun.clicked.connect(self.runCheckingCorrectness)    # Кнопка запуска проверки файла
        self.btnSettings.clicked.connect(self.setupSettings)    # Кнопка перехода к настройкам

    def chooseFile(self):  # Выбор файла
        dialog = QFileDialog.getOpenFileNames(self, "Выбор файла", "", "*.docx")
        if dialog[0]:
            print(dialog[0])
            self.fileFlag = True
            self.LENameFile.setText(f"Выбрано файлов: {len(dialog[0])} ")
            self.fileNames = dialog[0]
            self.LEErrorLine.hide()

    def runCheckingCorrectness(self):  # Запуск проверки корректности
        if self.fileFlag:
            pass  # Основная часть проверки
        else:
            self.LEErrorLine.show()

    def setupSettings(self):  # Запуск проверки корректности
        self.GoToSettings = SettingsWindow(self)
        self.hide()
        self.GoToSettings.show()


def except_hook(cls, exception, traceback):  # Блок для получения сообщений об ошибках
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':  # Запуск программы
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
