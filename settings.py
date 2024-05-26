import sys

from PyQt5 import (uic, QtCore, QtWidgets)
from PyQt5.QtWidgets import QWidget, QApplication

# from uiSettings import Ui_Settings


# from SettingsUi import Ui_Settings


class SettingsWindow(QWidget):
    def __init__(self, *args):
        super(SettingsWindow, self).__init__()
        # self.ui = Ui_Settings()
        # self.ui.setupUi(self)
        self.ui = uic.loadUi('SettingsUI.ui', self)  # Открытие файла ui
        self.main = args[0]
        self.ui.btnGoBack.clicked.connect(self.goBack)  # Кнопка перехода обратно в основное меню
        self.ui.btnDefaultSettings.clicked.connect(self.setDefaultSettingsByScreen)  # Кнопка установки базовых настроек
        self.ui.btnHelp.clicked.connect(self.main.openDocumentation)
        self.ui.tabWidget.setCurrentIndex(0)
        self.setDefaultSettings()

    def goBack(self):  # Вернуться назад в основное окно
        self.hide()
        self.main.show()

    def setDefaultSettings(self):  # Установка базовых настроек
        self.setDefaultPage()
        self.setDefaultHeadings()
        self.setDefaultMainText()
        self.setDefaultList()
        self.setDefaultTable()
        self.setDefaultTPicture()

    def setDefaultSettingsByScreen(self):
        lst = [self.setDefaultPage,
               self.setDefaultHeadings,
               self.setDefaultMainText,
               self.setDefaultList,
               self.setDefaultTable,
               self.setDefaultTPicture]
        lst[self.tabWidget.currentIndex()]()

    def setDefaultPage(self):
        self.ui.LEFieldsBottom.setText("3")
        self.ui.LEFieldsTop.setText("2")
        self.ui.LEFieldsLeft.setText("3")
        self.ui.LEFieldsRight.setText("1.5")

        self.ui.CBFontName.setCurrentIndex(0)
        self.ui.btnNumerationDown.setChecked(True)
        self.ui.CBFontName.setCurrentIndex(0)
        self.ui.PortraitOrientation.setChecked(True)

    def setDefaultHeadings(self):
        self.ui.LEFirstLvlSpacingAfter.setText("12")
        self.ui.LEFirstLvlSize.setText("16")
        self.ui.LEFirstLvlSpacingBefore.setText("0")
        self.ui.LESecondLvlSpacingBefore.setText("12")
        self.ui.LESecondLvlSize.setText("14")
        self.ui.LESecondLvlSpacingAfter.setText("6")
        self.ui.LEThirdLvlSpacingBefore.setText("8")
        self.ui.LEThirdLvlSize.setText("13")
        self.ui.LEThirdLvlSpacingAfter.setText("4")

        self.ui.CBLVL1CheckNumeration.setChecked(True)
        self.ui.CBLVL2CheckNumeration.setChecked(True)
        self.ui.CBLVL3CheckNumeration.setChecked(True)

        self.ui.CBLVL1NotSpacing.setChecked(True)
        self.ui.CBLVL1NewPage.setChecked(True)
        self.ui.CBLVL2NotSpacing.setChecked(True)
        self.ui.CBLVL2NewPage.setChecked(False)
        self.ui.CBLVL3NewPage.setChecked(False)
        self.ui.CBLVL3NotSpacing.setChecked(True)
        self.ui.CBLVL1Bold.setChecked(True)
        self.ui.CBLVL1Italic.setChecked(False)
        self.ui.CBLVL1Underline.setChecked(False)
        self.ui.RBLVL1TextMiddle.setChecked(True)
        self.ui.CBLVL2Bold.setChecked(True)
        self.ui.CBLVL2Italic.setChecked(False)
        self.ui.CBLVL2Underline.setChecked(False)
        self.ui.RBLVL2TextMiddle.setChecked(True)
        self.ui.CBLVL3Bold.setChecked(True)
        self.ui.CBLVL3Italic.setChecked(False)
        self.ui.CBLVL3Underline.setChecked(False)
        self.ui.RBLVL3TextMiddle.setChecked(True)

    def setDefaultMainText(self):
        self.ui.LEMainTextSpacingBefore.setText("0")
        self.ui.LEMainTextSpacingAfter.setText("0")
        self.ui.LEMainTextSize.setText("13")
        self.ui.LEMainTextSpacingBetween.setText("1.5")
        self.ui.LEMainTextSpacingParagraph.setText("1.25")

        self.ui.CBMainTextBold.setChecked(False)
        self.ui.CBMainTextItalic.setChecked(False)
        self.ui.CBMainTextUnderline.setChecked(False)
        self.ui.RBMainTextWidth.setChecked(True)

    def setDefaultList(self):
        pass

    def setDefaultTable(self):
        self.ui.LETableFontSize.setText("12")
        self.ui.CBTableParagraphBeforeTable.setChecked(True)
        self.ui.CBTableFormatParagraph.setCurrentIndex(0)

        self.ui.LETableSpacingBefore.setText("13")
        self.ui.LETableSpacingAfter.setText("0")
        self.ui.LETabletSpacingBetween.setText("1")
        self.ui.LETableSpacingParagraph.setText("0")
        self.ui.LETableParagraphSpacingAfter.setText("13")

        self.ui.CBTableHeadingTop.setChecked(True)
        self.ui.CBTableHeadingLeft.setChecked(True)

        self.ui.CBTableBold.setChecked(True)
        self.ui.CBTableItalic.setChecked(False)
        self.ui.CBTableUnderline.setChecked(False)
        self.ui.RBTableTextMiddle_2.setChecked(True)
        self.ui.RBTableTextLeft.setChecked(True)
        self.ui.RBTableHeadingTextMiddle.setChecked(True)

    def setDefaultTPicture(self):
        self.ui.LEPictureSpacingBefore.setText("6")
        self.ui.LEPictureSpacingAfter.setText("0")
        self.ui.LEPicturetSpacingParagraph.setText("0")
        self.ui.LEPictureSpacingBetween.setText("1")

        self.ui.CBPictureNotSpacing.setChecked(True)
        self.ui.CBPictureTitle.setChecked(True)

        self.ui.CBPictureTitleFormat.setCurrentIndex(0)
        self.ui.LEPictureFontSize.setText("11")
        self.ui.LEPictureTitleSpacingBefore.setText("0")
        self.ui.LEPictureTitleSpacingAfter.setText("6")
        self.ui.LEPictureTitleSpacingBetween.setText("1")
        self.ui.LEPictureTitleSpacingFirstLine.setText("0")

        self.ui.RBPictureMiddle.setChecked(True)
        self.ui.RBPictureTitleMiddle.setChecked(True)
        self.ui.CBPictureTitleUnderline.setChecked(False)
        self.ui.CBPictureTitleItalic.setChecked(True)
        self.ui.CBPictureTitleBold.setChecked(True)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)
