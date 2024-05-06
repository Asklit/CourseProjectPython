import sys

from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QWidget, QApplication


class SettingsWindow(QWidget):
    def __init__(self, *args):
        super().__init__()
        uic.loadUi('SettingsUI.ui', self)  # Открытие файла ui
        self.main = args[0]
        self.btnGoBack.clicked.connect(self.goBack)     # Кнопка перехода обратно в основное меню
        self.btnDefaultSettings.clicked.connect(self.setDefaultSettings)     # Кнопка установки базовых настроек

    def goBack(self):  # Вернуться назад в основное окно
        self.hide()
        self.main.show()

    #  A: Работает только для блоков теста LineEdit, для других видов нужно доделывать
    def setDefaultSettings(self):  # Установка базовых настроек
        _translate = QtCore.QCoreApplication.translate
        self.LEFieldsBottom.setText(_translate("Settings", "3"))
        self.LEFieldsTop.setText(_translate("Settings", "2"))
        self.LEFieldsLeft.setText(_translate("Settings", "3"))
        self.LEFieldsRight.setText(_translate("Settings", "1.5"))
        # self.comboBox.setCurrentIndex(self.items.keys().index("Times New Roman"))
        self.LEFieldsRight_2.setText(_translate("Settings", "1"))
        self.LEFirstLvlSpacingAfter.setText(_translate("Settings", "12"))
        self.LEFirstLvlSize.setText(_translate("Settings", "16"))
        self.LEFirstLvlSpacingBefore.setText(_translate("Settings", "0"))
        self.LESecondLvlSpacingBefore.setText(_translate("Settings", "12"))
        self.LESecondLvlSize.setText(_translate("Settings", "14"))
        self.LESecondLvlSpacingAfter.setText(_translate("Settings", "6"))
        self.LEThirdLvlSpacingBefore.setText(_translate("Settings", "8"))
        self.LEThirdLvlSize.setText(_translate("Settings", "13"))
        self.LEThirdLvlSpacingAfter.setText(_translate("Settings", "4"))

        # Доделать
        self.CBLVL1NotSpacing.setText(_translate("Settings", "Не отрывать от след."))
        self.CBLVL1NewPage.setText(_translate("Settings", "С новой страницы"))
        self.CBLVL2NotSpacing.setText(_translate("Settings", "Не отрывать от след."))
        self.CBLVL2NewPage.setText(_translate("Settings", "С новой страницы"))
        self.CBLVL3NewPage.setText(_translate("Settings", "С новой страницы"))
        self.CBLVL3NotSpacing.setText(_translate("Settings", "Не отрывать от след."))
        self.checkBox_7.setText(_translate("Settings", "B"))

        self.LEMainTextSpacingBefore.setText(_translate("Settings", "0"))
        self.LEMainTextSpacingAfter.setText(_translate("Settings", "0"))
        self.LEMainTextSize.setText(_translate("Settings", "13"))
        self.LEMainTextSpacingBetween.setText(_translate("Settings", "1.5"))
        self.LEMainTextSpacingParagraph.setText(_translate("Settings", "1,25"))
        #  self.CBNumberedListType.setCurrentIndex(self.items.keys().index("1. 2. 3."))
        #  self.CBNumberedListEndLetter.setCurrentIndex(self.items.keys().index("."))

        # Доделать
        self.CBNumberedListCapitalize.setText(_translate("Settings", "Начало с заглавной буквы"))
        self.CBMarkedListType.setItemText(0, _translate("Settings", "-"))
        self.CBMarkedListType.setItemText(1, _translate("Settings", "*"))
        self.CBMarkedListType.setItemText(2, _translate("Settings", "◉"))
        self.CBMarkedListType.setItemText(3, _translate("Settings", "●"))

        self.labelSettings_92.setText(_translate("Settings", "Маркер"))
        self.labelSettings_94.setText(_translate("Settings", "Маркированный список"))
        self.labelSettings_93.setText(_translate("Settings", "Знак в конце"))
        self.CBMarkedListEndLetter.setItemText(0, _translate("Settings", "."))
        self.CBMarkedListEndLetter.setItemText(1, _translate("Settings", ":"))
        self.CBMarkedListEndLetter.setItemText(2, _translate("Settings", ","))
        self.CBMarkedListEndLetter.setItemText(3, _translate("Settings", "!"))
        self.CBMarkedListEndLetter.setItemText(4, _translate("Settings", "?"))
        self.CBMarkedListCapitalize.setText(_translate("Settings", "Начало с заглавной буквы"))

        self.LETableFontSize.setText(_translate("Settings", "12"))
        self.CBTableParagraphBeforeTable.setText(_translate("Settings", "Абзац перед таблицей"))
        self.CBTableFormatParagraph.setItemText(0, _translate("Settings", "Таблица <N> - <Название>."))
        self.CBTableFormatParagraph.setItemText(1, _translate("Settings", "<Название>."))
        self.LETableSpacingBefore.setText(_translate("Settings", "13"))
        self.LETableSpacingAfter.setText(_translate("Settings", "0"))
        self.LETabletSpacingBetween.setText(_translate("Settings", "1"))
        self.LETableSpacingParagraph.setText(_translate("Settings", "0"))
        self.LETableParagraphSpacingAfter.setText(_translate("Settings", "13"))
        self.CBTableHeadingTop.setText(_translate("Settings", "Сверху"))
        self.CBTableHeadingBottom.setText(_translate("Settings", "Сбоку"))

        self.LEPictureSpacingBefore.setText(_translate("Settings", "6"))
        self.LEPictureSpacingAfter.setText(_translate("Settings", "0"))
        self.LEPicturetSpacingParagraph.setText(_translate("Settings", "0"))
        self.LEPictureSpacingBetween.setText(_translate("Settings", "1"))
        self.CBPictureNotSpacing.setText(_translate("Settings", "Не отрывать от след."))
        self.CBPictureTitle.setText(_translate("Settings", "Подпись под рисунком"))
        self.CBPictureTitleFormat.setItemText(0, _translate("Settings", "Рисунок <N> - <Название>."))
        self.CBPictureTitleFormat.setItemText(1, _translate("Settings", "<Название>."))
        self.LEPictureTitleSpacingBefore.setText(_translate("Settings", "11"))
        self.LEPictureTitleSpacingBefore_2.setText(_translate("Settings", "0"))
        self.LEPictureTitleSpacingAfter.setText(_translate("Settings", "6"))
        self.LEPictureTitleSpacingAfter_2.setText(_translate("Settings", "1"))
        self.LEPictureTitleSpacingAfter_3.setText(_translate("Settings", "0"))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)