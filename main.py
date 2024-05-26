import os
import subprocess
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from docx.enum.text import WD_ALIGN_PARAGRAPH
from settings import SettingsWindow
import keyboard

from uiMain import Ui_Checker


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.ui = Ui_Checker()
        # self.ui.setupUi(self)
        self.SettingsWindow = SettingsWindow(self)
        self.fileFlag = False
        self.fileNames = []  # Список путей до выбранных файлов
        self.ui = uic.loadUi('uiMainFile.ui', self)  # Открытие файла ui

        # Параметры форматирования докумерта
        self.text_checklist = None
        self.heading1_checklist = None
        self.heading2_checklist = None
        self.heading3_checklist = None
        self.page_checklist = None
        self.list_checklist = None
        self.table_checklist = None
        self.picture_checklist = None
        self.table_heading_checklist = None
        self.title_picture_checklist = None
        self.table_title_checklist = None

        self.proc = None

        keyboard.add_hotkey("f1", self.openDocumentation)

        self.ui.LEErrorLine.hide()

        # Привязки функций к кнопкам
        self.ui.btnChooseFile.clicked.connect(self.chooseFile)     # Кнопка выбора файла
        self.ui.btnRun.clicked.connect(self.runCheckingCorrectness)    # Кнопка запуска проверки файла
        self.ui.btnSettings.clicked.connect(self.setupSettings)    # Кнопка перехода к настройкам
        self.ui.btnHelp.clicked.connect(self.openDocumentation)

    def openDocumentation(self):
        if self.proc is not None:
            self.proc.kill()

        if self.isActiveWindow():
            self.proc = subprocess.Popen("hh.exe -mapid" + "100" + " HelpMenu.chm")
        else:
            self.proc = subprocess.Popen("hh.exe -mapid" + "20" + str(self.SettingsWindow.ui.tabWidget.currentIndex() + 1) + " HelpMenu.chm")

    def chooseFile(self):  # Выбор файла
        dialog = QFileDialog.getOpenFileNames(self, "Выбор файла", "", "*.docx")
        if dialog[0]:
            self.fileFlag = True
            self.ui.LENameFile.setText(f"Выбрано файлов: {len(dialog[0])} ")
            self.fileNames = dialog[0]
            self.ui.LEErrorLine.hide()

    def runCheckingCorrectness(self):  # Запуск проверки корректности
        if self.fileFlag:
            self.getSettings()
            print(self.text_checklist)
            print(self.heading1_checklist)
            print(self.heading2_checklist)
            print(self.heading3_checklist)
            print(self.table_checklist)
            print(self.list_checklist)
            print(self.page_checklist)
            print(self.picture_checklist)
        else:
            self.ui.LEErrorLine.show()  # Вывод сообщения об отсутствии выбранных файлов

    def getSettings(self):
        self.getMainTextSettings()
        self.getHeading1Settings()
        self.getHeading2Settings()
        self.getHeading3Settings()
        self.getListSettings()
        self.getPageSettings()
        self.getPictureSettings()
        self.getTableSettings()

    def getMainTextSettings(self):
        alignment = WD_ALIGN_PARAGRAPH.LEFT
        if self.SettingsWindow.ui.RBMainTextLeft.isChecked():
            alignment = WD_ALIGN_PARAGRAPH.LEFT
        elif self.SettingsWindow.ui.RBMainTextRight.isChecked():
            alignment = WD_ALIGN_PARAGRAPH.RIGHT
        elif self.SettingsWindow.ui.RBMainTextMiddle.isChecked():
            alignment = WD_ALIGN_PARAGRAPH.CENTER
        elif self.SettingsWindow.ui.RBMainTextLeft.isChecked():
            alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

        self.text_checklist = {
            "font_name": self.SettingsWindow.ui.CBFontName.currentText(),
            "font_size": self.SettingsWindow.ui.LEMainTextSize.text(),
            "font_bald": self.SettingsWindow.ui.CBMainTextBold.isChecked(),
            "font_italic": self.SettingsWindow.ui.CBMainTextItalic.isChecked(),
            "font_underline": self.SettingsWindow.ui.CBMainTextUnderline.isChecked(),
            "font_color": None,  # нет такого в UI
            "font_back_color": None,  # нет такого в UI
            "alignment": alignment,
            "keep_with_next": False,  # нет такого в UI, false по умолчанию для main текста
            "page_break_before": False,  # нет такого в UI, false по умолчанию для main текста
            "space_before": self.SettingsWindow.ui.LEMainTextSpacingBefore.text(),
            "space_after": self.SettingsWindow.ui.LEMainTextSpacingAfter.text(),
            "left_indent": 0,  # нет такого в UI
            "right_indent": 0,  # нет такого в UI
            "first_line_indent": self.SettingsWindow.ui.LEMainTextSpacingParagraph.text(),
            "line_spacing": self.SettingsWindow.ui.LEMainTextSpacingBetween.text(),
        }

    def getHeading1Settings(self):
        alignment = WD_ALIGN_PARAGRAPH.CENTER
        if self.SettingsWindow.ui.RBLVL1TextLeft.isChecked():
            alignment = WD_ALIGN_PARAGRAPH.LEFT
        elif self.SettingsWindow.ui.RBLVL1TextRight.isChecked():
            alignment = WD_ALIGN_PARAGRAPH.RIGHT
        elif self.SettingsWindow.ui.RBLVL1TextMiddle.isChecked():
            alignment = WD_ALIGN_PARAGRAPH.CENTER
        elif self.SettingsWindow.ui.RBLVL1TextLeft.isChecked():
            alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

        self.heading1_checklist = {
            "font_name": self.SettingsWindow.ui.CBFontName.currentText(),
            "font_size": self.SettingsWindow.ui.LEFirstLvlSize.text(),
            "font_bald": self.SettingsWindow.ui.CBLVL1Bold.isChecked(),
            "font_italic": self.SettingsWindow.ui.CBLVL1Italic.isChecked(),
            "font_underline": self.SettingsWindow.ui.CBLVL1Underline.isChecked(),
            "font_color": None,  # нет такого в UI
            "font_back_color": None,  # нет такого в UI
            "alignment": alignment,
            "keep_with_next": self.SettingsWindow.ui.CBLVL1NotSpacing.isChecked(),
            "page_break_before": self.SettingsWindow.ui.CBLVL1NewPage.isChecked(),  # нет такого в UI, false по умолчанию для main текста
            "space_before": self.SettingsWindow.ui.LEFirstLvlSpacingBefore.text(),
            "space_after": self.SettingsWindow.ui.LEFirstLvlSpacingAfter.text(),
            "left_indent": 0,  # нет такого в UI
            "right_indent": 0,  # нет такого в UI
            "first_line_indent": 0,  # нет такого в UI
            "line_spacing": 1.0,  # нет такого в UI
        }

    def getHeading2Settings(self):
        alignment = WD_ALIGN_PARAGRAPH.CENTER
        if self.SettingsWindow.ui.RBLVL2TextLeft.isChecked():
            alignment = WD_ALIGN_PARAGRAPH.LEFT
        elif self.SettingsWindow.ui.RBLVL2TextRight.isChecked():
            alignment = WD_ALIGN_PARAGRAPH.RIGHT
        elif self.SettingsWindow.ui.RBLVL2TextMiddle.isChecked():
            alignment = WD_ALIGN_PARAGRAPH.CENTER
        elif self.SettingsWindow.ui.RBLVL2TextLeft.isChecked():
            alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

        self.heading2_checklist = {
            "font_name": self.SettingsWindow.ui.CBFontName.currentText(),
            "font_size": self.SettingsWindow.ui.LESecondLvlSize.text(),
            "font_bald": self.SettingsWindow.ui.CBLVL2Bold.isChecked(),
            "font_italic": self.SettingsWindow.ui.CBLVL2Italic.isChecked(),
            "font_underline": self.SettingsWindow.ui.CBLVL2Underline.isChecked(),
            "font_color": None,  # нет такого в UI
            "font_back_color": None,  # нет такого в UI
            "alignment": alignment,
            "keep_with_next": self.SettingsWindow.ui.CBLVL2NotSpacing.isChecked(),
            "page_break_before": self.SettingsWindow.ui.CBLVL2NewPage.isChecked(),  # нет такого в UI, false по умолчанию для main текста
            "space_before": self.SettingsWindow.ui.LESecondLvlSpacingBefore.text(),
            "space_after": self.SettingsWindow.ui.LESecondLvlSpacingAfter.text(),
            "left_indent": 0,  # нет такого в UI
            "right_indent": 0,  # нет такого в UI
            "first_line_indent": 0,  # нет такого в UI
            "line_spacing": 1.0,  # нет такого в UI
        }

    def getHeading3Settings(self):
        alignment = WD_ALIGN_PARAGRAPH.CENTER
        if self.SettingsWindow.ui.RBLVL3TextLeft.isChecked():
            alignment = WD_ALIGN_PARAGRAPH.LEFT
        elif self.SettingsWindow.ui.RBLVL3TextRight.isChecked():
            alignment = WD_ALIGN_PARAGRAPH.RIGHT
        elif self.SettingsWindow.ui.RBLVL3TextMiddle.isChecked():
            alignment = WD_ALIGN_PARAGRAPH.CENTER
        elif self.SettingsWindow.ui.RBLVL3TextLeft.isChecked():
            alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

        self.heading3_checklist = {
            "font_name": self.SettingsWindow.ui.CBFontName.currentText(),
            "font_size": self.SettingsWindow.ui.LEThirdLvlSize.text(),
            "font_bald": self.SettingsWindow.ui.CBLVL3Bold.isChecked(),
            "font_italic": self.SettingsWindow.ui.CBLVL3Italic.isChecked(),
            "font_underline": self.SettingsWindow.ui.CBLVL3Underline.isChecked(),
            "font_color": None,  # нет такого в UI
            "font_back_color": None,  # нет такого в UI
            "alignment": alignment,
            "keep_with_next": self.SettingsWindow.ui.CBLVL3NotSpacing.isChecked(),
            "page_break_before": self.SettingsWindow.ui.CBLVL3NewPage.isChecked(),  # нет такого в UI, false по умолчанию для main текста
            "space_before": self.SettingsWindow.ui.LEThirdLvlSpacingBefore.text(),
            "space_after": self.SettingsWindow.ui.LEThirdLvlSpacingAfter.text(),
            "left_indent": 0,  # нет такого в UI
            "right_indent": 0,  # нет такого в UI
            "first_line_indent": 0,  # нет такого в UI
            "line_spacing": 1.0,  # нет такого в UI
        }

    def getPageSettings(self):
        numbering_position = "Bottom"
        if self.SettingsWindow.ui.btnNumerationTop.isChecked():
            numbering_position = "Top"
        elif self.SettingsWindow.ui.btnNumerationDown.isChecked():
            numbering_position = "Bottom"
        elif self.SettingsWindow.ui.btnNumerationLeft.isChecked():
            numbering_position = "Left"
        elif self.SettingsWindow.ui.btnNumerationRight.isChecked():
            numbering_position = "Right"

        self.page_checklist = {
            "FieldsTop": self.SettingsWindow.ui.LEFieldsTop.text(),  # Поля страницы (верхнее)
            "FieldsBottom": self.SettingsWindow.ui.LEFieldsBottom.text(),  # Поля страницы (нижнее)
            "FieldsLeft": self.SettingsWindow.ui.LEFieldsLeft.text(),  # Поля страницы (левое)
            "FieldsRight": self.SettingsWindow.ui.LEFieldsRight.text(),  # Поля страницы (правое)
            "NumberingPosition": numbering_position,  # Позиция нумерации (сверху, снизу, справа, слева)
            "NumberingStartFrom": self.SettingsWindow.ui.LENumerationStartFrom.text()  # Число, с которого начинается нумерация
        }

    def getListSettings(self):
        self.list_checklist = {
            "NumberedListType": self.SettingsWindow.ui.CBNumberedListType.currentText(),  # Тип нумерации (1. 2. 3. / 1) 2) 3))
        }

    def getTableSettings(self):
        alignment = WD_ALIGN_PARAGRAPH.LEFT
        if self.SettingsWindow.ui.RBLVL3TextLeft.isChecked():
            alignment = WD_ALIGN_PARAGRAPH.LEFT
        elif self.SettingsWindow.ui.RBLVL3TextRight.isChecked():
            alignment = WD_ALIGN_PARAGRAPH.RIGHT
        elif self.SettingsWindow.ui.RBLVL3TextMiddle.isChecked():
            alignment = WD_ALIGN_PARAGRAPH.CENTER
        elif self.SettingsWindow.ui.RBLVL3TextLeft.isChecked():
            alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

        self.table_checklist = {
            "font_name": self.SettingsWindow.ui.CBFontName.currentText(),  # Шрифт
            "font_size": self.SettingsWindow.ui.LETableFontSize.text(),  # Размер шрифта в таблице
            "paragraph_before_table": self.SettingsWindow.ui.CBTableParagraphBeforeTable.isChecked(),  # Параграф перед таблицей
            "space_before": self.SettingsWindow.ui.LETableSpacingBefore.text(),
            "space_after": self.SettingsWindow.ui.LETableSpacingAfter.text(),
            "left_indent": 0,  # нет такого в UI
            "right_indent": 0,  # нет такого в UI
            "first_line_indent": self.SettingsWindow.ui.LETableSpacingParagraph.text(),
            "line_spacing": self.SettingsWindow.ui.LETabletSpacingBetween.text(),
            "spacing_under_paragraph_after_table": self.SettingsWindow.ui.LETableParagraphSpacingAfter.text()  # Интервал абзаца после таблицы
        }

        self.table_title_checklist = {
            "title_format": self.SettingsWindow.ui.CBTableFormatParagraph.currentText(), # Формат подписи под таблицей (Таблица <N> - <Название>)
        }

        self.table_heading_checklist = {
            "heading_font_bald": self.SettingsWindow.ui.CBTableBold.isChecked(),  # Жирный шрифт заголовков
            "heading_font_italic": self.SettingsWindow.ui.CBTableItalic.isChecked(),  # Курсив заголовков
            "heading_font_underline": self.SettingsWindow.ui.CBTableUnderline.isChecked(),  # Подчеркивание заголовков
            "heading_left": self.SettingsWindow.ui.CBTableHeadingLeft.isChecked(),  # Необходимость заголовков слева
            "heading_top": self.SettingsWindow.ui.CBTableHeadingTop.isChecked(),  # Необходимость заголовков сверху
            "heading_alignment": alignment
            }

    def getPictureSettings(self):
        title_alignment = WD_ALIGN_PARAGRAPH.LEFT
        if self.SettingsWindow.ui.RBPictureTitleLeft.isChecked():
            title_alignment = WD_ALIGN_PARAGRAPH.LEFT
        elif self.SettingsWindow.ui.RBPictureTitleRight.isChecked():
            title_alignment = WD_ALIGN_PARAGRAPH.RIGHT
        elif self.SettingsWindow.ui.RBPictureTitleMiddle.isChecked():
            title_alignment = WD_ALIGN_PARAGRAPH.CENTER

        picture_alignment = WD_ALIGN_PARAGRAPH.CENTER
        if self.SettingsWindow.ui.RBPictureLeft.isChecked():
            picture_alignment = WD_ALIGN_PARAGRAPH.LEFT
        elif self.SettingsWindow.ui.RBPictureRight.isChecked():
            picture_alignment = WD_ALIGN_PARAGRAPH.RIGHT
        elif self.SettingsWindow.ui.RBPictureMiddle.isChecked():
            picture_alignment = WD_ALIGN_PARAGRAPH.CENTER

        self.picture_checklist = {
            "picture_alignment": picture_alignment,  # Выравнивание картинки
            "keep_with_next": self.SettingsWindow.ui.CBPictureNotSpacing.isChecked(),  # Не отрывать рисунок от подписи
            "picture_space_before": self.SettingsWindow.ui.LEPictureSpacingBefore.text(),
            "picture_space_after": self.SettingsWindow.ui.LEPictureSpacingAfter.text(),
            "picture_first_line_indent": self.SettingsWindow.ui.LEPicturetSpacingParagraph.text(),
            "picture_line_spacing": self.SettingsWindow.ui.LEPictureSpacingBetween.text(),
        }

        self.title_picture_checklist = {
            "title_font_name": self.SettingsWindow.ui.CBFontName.currentText(),  # Шрифт подписи под рисунком
            "title_font_size": self.SettingsWindow.ui.LEPictureFontSize.text(),  # Размер подписи под рисунком
            "title_font_bald": self.SettingsWindow.ui.CBPictureTitleBold.isChecked(),  # Выделение жирным шрифтом
            "title_font_italic": self.SettingsWindow.ui.CBPictureTitleItalic.isChecked(),  # Выделение курсовом
            "title_font_underline": self.SettingsWindow.ui.CBPictureTitleUnderline.isChecked(),  # Выделение подчеркиванием
            "title_space_before": self.SettingsWindow.ui.LEPictureTitleSpacingBefore.text(),  # интервал перед подписью
            "title_space_after": self.SettingsWindow.ui.LEPictureTitleSpacingAfter.text(),  # интервал после подписи
            "title_first_line_indent": self.SettingsWindow.ui.LEPictureTitleSpacingFirstLine.text(),  # Абзацный отступ
            "title_line_spacing": self.SettingsWindow.ui.LEPictureTitleSpacingBetween.text(),  # Междустрочный интервал
            "title_alignment": title_alignment,  # Выравнивание подписи
            "title_format": self.SettingsWindow.ui.CBPictureTitleFormat.currentText()  # Формат подписи (Рисунок <N> - <Название>.)
        }

    def setupSettings(self):  # Запуск окна настроек
        self.hide()
        self.SettingsWindow.show()


def except_hook(cls, exception, traceback):  # Блок для получения сообщений об ошибках
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':  # Запуск программы
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
