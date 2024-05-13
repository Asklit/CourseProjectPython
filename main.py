import os
import subprocess
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from docx.enum.text import WD_ALIGN_PARAGRAPH
from settings import SettingsWindow
import keyboard


class QWiddet:
    pass


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.SettingsWindow = SettingsWindow(self)
        self.fileFlag = False
        self.fileNames = []  # Список путей до выбранных файлов
        uic.loadUi('uiMainFile.ui', self)  # Открытие файла ui

        # Параметры форматирования докумерта
        self.text_checklist = None
        self.heading1_checklist = None
        self.heading2_checklist = None
        self.heading3_checklist = None
        self.page_checklist = None
        self.list_checklist = None
        self.table_checklist = None
        self.picture_checklist = None

        keyboard.add_hotkey("f1", self.openDocumentation)

        self.LEErrorLine.hide()

        # Привязки функций к кнопкам
        self.btnChooseFile.clicked.connect(self.chooseFile)     # Кнопка выбора файла
        self.btnRun.clicked.connect(self.runCheckingCorrectness)    # Кнопка запуска проверки файла
        self.btnSettings.clicked.connect(self.setupSettings)    # Кнопка перехода к настройкам

    def openDocumentation(self):
        if self.isActiveWindow():
            self.proc = subprocess.Popen("hh.exe -mapid" + "00" "HelpMenu.chm")
        else:
            self.proc = subprocess.Popen("hh.exe -mapid" + "1" + str(self.SettingsWindow.tabWidget.currentIndex()) + "HelpMenu.chm")

    def chooseFile(self):  # Выбор файла
        dialog = QFileDialog.getOpenFileNames(self, "Выбор файла", "", "*.docx")
        if dialog[0]:
            self.fileFlag = True
            self.LENameFile.setText(f"Выбрано файлов: {len(dialog[0])} ")
            self.fileNames = dialog[0]
            self.LEErrorLine.hide()

    def runCheckingCorrectness(self):  # Запуск проверки корректности
        if self.fileFlag:
            self.getSettings()
            pass  # Основная часть проверки
        else:
            self.LEErrorLine.show()  # Вывод сообщения об отсутствии выбранных файлов

    def getSettings(self):
        self.getMainTextSettings()
        self.getHeading1Settings()
        self.getHeading2Settings()
        self.getHeading3Settings()
        self.getListSettings()
        self.getPageSettings()
        self.getPictureSettings()
        self.getTableSettings()
        print(self.text_checklist)
        print(self.heading1_checklist)
        print(self.heading2_checklist)
        print(self.heading3_checklist)
        print(self.table_checklist)
        print(self.list_checklist)
        print(self.page_checklist)
        print(self.picture_checklist)

    def getMainTextSettings(self):
        alignment = WD_ALIGN_PARAGRAPH.LEFT
        if self.SettingsWindow.RBMainTextLeft.isChecked():
            alignment = WD_ALIGN_PARAGRAPH.LEFT
        elif self.SettingsWindow.RBMainTextRight.isChecked():
            alignment = WD_ALIGN_PARAGRAPH.RIGHT
        elif self.SettingsWindow.RBMainTextMiddle.isChecked():
            alignment = WD_ALIGN_PARAGRAPH.CENTER
        elif self.SettingsWindow.RBMainTextLeft.isChecked():
            alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

        self.text_checklist = {
            "font_name": self.SettingsWindow.CBFontName.currentText(),
            "font_size": self.SettingsWindow.LEMainTextSize.text(),
            "font_bald": self.SettingsWindow.CBMainTextBold.isChecked(),
            "font_italic": self.SettingsWindow.CBMainTextItalic.isChecked(),
            "font_underline": self.SettingsWindow.CBMainTextUnderline.isChecked(),
            "font_color": None,  # нет такого в UI
            "font_back_color": None,  # нет такого в UI
            "alignment": alignment,
            "keep_with_next": False,  # нет такого в UI, false по умолчанию для main текста
            "page_break_before": False,  # нет такого в UI, false по умолчанию для main текста
            "space_before": self.SettingsWindow.LEMainTextSpacingBefore.text(),
            "space_after": self.SettingsWindow.LEMainTextSpacingAfter.text(),
            "left_indent": 0,  # нет такого в UI
            "right_indent": 0,  # нет такого в UI
            "first_line_indent": self.SettingsWindow.LEMainTextSpacingParagraph.text(),
            "line_spacing": self.SettingsWindow.LEMainTextSpacingBetween.text(),
        }

    def getHeading1Settings(self):
        alignment = WD_ALIGN_PARAGRAPH.CENTER
        if self.SettingsWindow.RBLVL1TextLeft.isChecked():
            alignment = WD_ALIGN_PARAGRAPH.LEFT
        elif self.SettingsWindow.RBLVL1TextRight.isChecked():
            alignment = WD_ALIGN_PARAGRAPH.RIGHT
        elif self.SettingsWindow.RBLVL1TextMiddle.isChecked():
            alignment = WD_ALIGN_PARAGRAPH.CENTER
        elif self.SettingsWindow.RBLVL1TextLeft.isChecked():
            alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

        self.heading1_checklist = {
            "font_name": self.SettingsWindow.CBFontName.currentText(),
            "font_size": self.SettingsWindow.LEFirstLvlSize.text(),
            "font_bald": self.SettingsWindow.CBLVL1Bold.isChecked(),
            "font_italic": self.SettingsWindow.CBLVL1Italic.isChecked(),
            "font_underline": self.SettingsWindow.CBLVL1Underline.isChecked(),
            "font_color": None,  # нет такого в UI
            "font_back_color": None,  # нет такого в UI
            "alignment": alignment,
            "keep_with_next": self.SettingsWindow.CBLVL1NotSpacing.isChecked(),
            "page_break_before": self.SettingsWindow.CBLVL1NewPage.isChecked(),  # нет такого в UI, false по умолчанию для main текста
            "space_before": self.SettingsWindow.LEFirstLvlSpacingBefore.text(),
            "space_after": self.SettingsWindow.LEFirstLvlSpacingAfter.text(),
            "left_indent": 0,  # нет такого в UI
            "right_indent": 0,  # нет такого в UI
            "first_line_indent": 0,  # нет такого в UI
            "line_spacing": 1.0,  # нет такого в UI
        }

    def getHeading2Settings(self):
        alignment = WD_ALIGN_PARAGRAPH.CENTER
        if self.SettingsWindow.RBLVL2TextLeft.isChecked():
            alignment = WD_ALIGN_PARAGRAPH.LEFT
        elif self.SettingsWindow.RBLVL2TextRight.isChecked():
            alignment = WD_ALIGN_PARAGRAPH.RIGHT
        elif self.SettingsWindow.RBLVL2TextMiddle.isChecked():
            alignment = WD_ALIGN_PARAGRAPH.CENTER
        elif self.SettingsWindow.RBLVL2TextLeft.isChecked():
            alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

        self.heading2_checklist = {
            "font_name": self.SettingsWindow.CBFontName.currentText(),
            "font_size": self.SettingsWindow.LESecondLvlSize.text(),
            "font_bald": self.SettingsWindow.CBLVL2Bold.isChecked(),
            "font_italic": self.SettingsWindow.CBLVL2Italic.isChecked(),
            "font_underline": self.SettingsWindow.CBLVL2Underline.isChecked(),
            "font_color": None,  # нет такого в UI
            "font_back_color": None,  # нет такого в UI
            "alignment": alignment,
            "keep_with_next": self.SettingsWindow.CBLVL2NotSpacing.isChecked(),
            "page_break_before": self.SettingsWindow.CBLVL2NewPage.isChecked(),  # нет такого в UI, false по умолчанию для main текста
            "space_before": self.SettingsWindow.LESecondLvlSpacingBefore.text(),
            "space_after": self.SettingsWindow.LESecondLvlSpacingAfter.text(),
            "left_indent": 0,  # нет такого в UI
            "right_indent": 0,  # нет такого в UI
            "first_line_indent": 0,  # нет такого в UI
            "line_spacing": 1.0,  # нет такого в UI
        }

    def getHeading3Settings(self):
        alignment = WD_ALIGN_PARAGRAPH.CENTER
        if self.SettingsWindow.RBLVL3TextLeft.isChecked():
            alignment = WD_ALIGN_PARAGRAPH.LEFT
        elif self.SettingsWindow.RBLVL3TextRight.isChecked():
            alignment = WD_ALIGN_PARAGRAPH.RIGHT
        elif self.SettingsWindow.RBLVL3TextMiddle.isChecked():
            alignment = WD_ALIGN_PARAGRAPH.CENTER
        elif self.SettingsWindow.RBLVL3TextLeft.isChecked():
            alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

        self.heading3_checklist = {
            "font_name": self.SettingsWindow.CBFontName.currentText(),
            "font_size": self.SettingsWindow.LEThirdLvlSize.text(),
            "font_bald": self.SettingsWindow.CBLVL3Bold.isChecked(),
            "font_italic": self.SettingsWindow.CBLVL3Italic.isChecked(),
            "font_underline": self.SettingsWindow.CBLVL3Underline.isChecked(),
            "font_color": None,  # нет такого в UI
            "font_back_color": None,  # нет такого в UI
            "alignment": alignment,
            "keep_with_next": self.SettingsWindow.CBLVL3NotSpacing.isChecked(),
            "page_break_before": self.SettingsWindow.CBLVL3NewPage.isChecked(),  # нет такого в UI, false по умолчанию для main текста
            "space_before": self.SettingsWindow.LEThirdLvlSpacingBefore.text(),
            "space_after": self.SettingsWindow.LEThirdLvlSpacingAfter.text(),
            "left_indent": 0,  # нет такого в UI
            "right_indent": 0,  # нет такого в UI
            "first_line_indent": 0,  # нет такого в UI
            "line_spacing": 1.0,  # нет такого в UI
        }

    def getPageSettings(self):
        numbering_position = "Bottom"
        if self.SettingsWindow.btnNumerationTop.isChecked():
            numbering_position = "Top"
        elif self.SettingsWindow.btnNumerationDown.isChecked():
            numbering_position = "Bottom"
        elif self.SettingsWindow.btnNumerationLeft.isChecked():
            numbering_position = "Left"
        elif self.SettingsWindow.btnNumerationRight.isChecked():
            numbering_position = "Right"

        self.page_checklist = {
            "FieldsTop": self.SettingsWindow.LEFieldsTop.text(),  # Поля страницы (верхнее)
            "FieldsBottom": self.SettingsWindow.LEFieldsBottom.text(),  # Поля страницы (нижнее)
            "FieldsLeft": self.SettingsWindow.LEFieldsLeft.text(),  # Поля страницы (левое)
            "FieldsRight": self.SettingsWindow.LEFieldsRight.text(),  # Поля страницы (правое)
            "NumberingPosition": numbering_position,  # Позиция нумерации (сверху, снизу, справа, слева)
            "NumberingStartFrom": self.SettingsWindow.LENumerationStartFrom.text()  # Число, с которого начинается нумерация
        }

    def getListSettings(self):
        self.list_checklist = {
            "NumberedListType": self.SettingsWindow.CBNumberedListType.currentText(),  # Тип нумерации (1. 2. 3. / 1) 2) 3))
        }

    def getTableSettings(self):
        alignment = WD_ALIGN_PARAGRAPH.LEFT
        if self.SettingsWindow.RBLVL3TextLeft.isChecked():
            alignment = WD_ALIGN_PARAGRAPH.LEFT
        elif self.SettingsWindow.RBLVL3TextRight.isChecked():
            alignment = WD_ALIGN_PARAGRAPH.RIGHT
        elif self.SettingsWindow.RBLVL3TextMiddle.isChecked():
            alignment = WD_ALIGN_PARAGRAPH.CENTER
        elif self.SettingsWindow.RBLVL3TextLeft.isChecked():
            alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

        self.table_checklist = {
            "font_name": self.SettingsWindow.CBFontName.currentText(),  # Шрифт
            "font_size": self.SettingsWindow.LETableFontSize.text(),  # Размер шрифта в таблице
            "heading_font_bald": self.SettingsWindow.CBTableBold.isChecked(),  # Жирный шрифт заголовков
            "heading_font_italic": self.SettingsWindow.CBTableItalic.isChecked(),  # Курсив заголовков
            "heading_font_underline": self.SettingsWindow.CBTableUnderline.isChecked(),  # Подчеркивание заголовков
            "heading_left": self.SettingsWindow.CBTableHeadingLeft.isChecked(),  # Необходимость заголовков слева
            "heading_top": self.SettingsWindow.CBTableHeadingTop.isChecked(),  # Необходимость заголовков сверху
            "heading_alignment": alignment,
            "paragraph_before_table": self.SettingsWindow.CBTableParagraphBeforeTable.isChecked(),  # Параграф перед таблицей
            "title_format": self.SettingsWindow.CBTableFormatParagraph.currentText(),  # Формат подписи под таблицей (Таблица <N> - <Название>)
            "space_before": self.SettingsWindow.LETableSpacingBefore.text(),
            "space_after": self.SettingsWindow.LETableSpacingAfter.text(),
            "left_indent": 0,  # нет такого в UI
            "right_indent": 0,  # нет такого в UI
            "first_line_indent": self.SettingsWindow.LETableSpacingParagraph.text(),
            "line_spacing": self.SettingsWindow.LETabletSpacingBetween.text(),
            "spacing_under_paragraph_after_table": self.SettingsWindow.LETableParagraphSpacingAfter.text()  # Интервал абзаца после таблицы
        }

    def getPictureSettings(self):
        title_alignment = WD_ALIGN_PARAGRAPH.LEFT
        if self.SettingsWindow.RBPictureTitleLeft.isChecked():
            title_alignment = WD_ALIGN_PARAGRAPH.LEFT
        elif self.SettingsWindow.RBPictureTitleRight.isChecked():
            title_alignment = WD_ALIGN_PARAGRAPH.RIGHT
        elif self.SettingsWindow.RBPictureTitleMiddle.isChecked():
            title_alignment = WD_ALIGN_PARAGRAPH.CENTER

        picture_alignment = WD_ALIGN_PARAGRAPH.CENTER
        if self.SettingsWindow.RBPictureLeft.isChecked():
            picture_alignment = WD_ALIGN_PARAGRAPH.LEFT
        elif self.SettingsWindow.RBPictureRight.isChecked():
            picture_alignment = WD_ALIGN_PARAGRAPH.RIGHT
        elif self.SettingsWindow.RBPictureMiddle.isChecked():
            picture_alignment = WD_ALIGN_PARAGRAPH.CENTER

        self.picture_checklist = {
            "title_font_name": self.SettingsWindow.CBFontName.currentText(),  # Шрифт подписи под рисунком
            "title_font_size": self.SettingsWindow.LEPictureFontSize.text(),  # Размер подписи под рисунком
            "title_font_bald": self.SettingsWindow.CBPictureTitleBold.isChecked(),  # Выделение жирным шрифтом
            "title_font_italic": self.SettingsWindow.CBPictureTitleItalic.isChecked(),  # Выделение курсовом
            "title_font_underline": self.SettingsWindow.CBPictureTitleUnderline.isChecked(),  # Выделение подчеркиванием
            "title_space_before": self.SettingsWindow.LEPictureTitleSpacingBefore.text(),  # интервал перед подписью
            "title_space_after": self.SettingsWindow.LEPictureTitleSpacingAfter.text(),  # интервал после подписи
            "title_first_line_indent": self.SettingsWindow.LEPictureTitleSpacingFirstLine.text(),  # Абзацный отступ
            "title_line_spacing": self.SettingsWindow.LEPictureTitleSpacingBetween.text(),  # Междустрочный интервал
            "title_alignment": title_alignment,  # Выравнивание подписи
            "title_format": self.SettingsWindow.CBPictureTitleFormat.currentText(),  # Формат подписи (Рисунок <N> - <Название>.)
            "picture_alignment": picture_alignment,  # Выравнивание картинки
            "keep_with_next": self.SettingsWindow.CBPictureNotSpacing.isChecked(),  # Не отрывать рисунок от подписи
            "picture_space_before": self.SettingsWindow.LEPictureSpacingBefore.text(),
            "picture_space_after": self.SettingsWindow.LEPictureSpacingAfter.text(),
            "picture_first_line_indent": self.SettingsWindow.LEPicturetSpacingParagraph.text(),
            "picture_line_spacing": self.SettingsWindow.LEPictureSpacingBetween.text(),
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
