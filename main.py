import os
import subprocess
import sys


from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT as WD_ALIGN_PARAGRAPH
from settings import SettingsWindow
import keyboard
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT as WD_ALIGN_VERTICAL
from docx.enum.section import WD_ORIENTATION
from docx import Document

from docxParser import set_settings, parse_document
# from uiMain import Ui_Checker


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
        self.explorer = None

        self.ui.LEResLine.hide()
        self.ui.btnOpenRes.hide()

        keyboard.add_hotkey("f1", self.openDocumentation)

        self.ui.LEErrorLine.hide()

        # Привязки функций к кнопкам
        self.ui.btnChooseFile.clicked.connect(self.chooseFile)     # Кнопка выбора файла
        self.ui.btnRun.clicked.connect(self.runCheckingCorrectness)    # Кнопка запуска проверки файла
        self.ui.btnSettings.clicked.connect(self.setupSettings)    # Кнопка перехода к настройкам
        self.ui.btnHelp.clicked.connect(self.openDocumentation)
        self.ui.btnOpenRes.clicked.connect(self.openExplorer)
        self.ui.btnClearFiles.clicked.connect(self.clearFiles)

    def openDocumentation(self):
        if self.proc is not None:
            self.proc.kill()

        if self.isActiveWindow():
            self.proc = subprocess.Popen("hh.exe -mapid" + "100" + " HelpMenu.chm")
        else:
            self.proc = subprocess.Popen("hh.exe -mapid" + "20" + str(self.SettingsWindow.ui.tabWidget.currentIndex() + 1) + " Help Menu.chm")

    def openExplorer(self):
        if self.explorer is not None:
            self.explorer.kill()

    def chooseFile(self):  # Выбор файла
        self.ui.LEResLine.hide()
        self.ui.btnOpenRes.hide()
        dialog = QFileDialog.getOpenFileNames(self, "Выбор файла", "", "*.docx")

        if dialog[0]:
            for filename in dialog[0]:
                file, extension = os.path.splitext(filename)
                if extension == ".docx" and filename not in self.fileNames:
                    self.fileFlag = True
                    self.fileNames.append(filename)
                    self.ui.LENameFile.setText(f"Выбрано файлов: {len(self.fileNames)} ")
                    self.ui.LEErrorLine.hide()

    def clearFiles(self):
        self.ui.LENameFile.setText(f"Файлы не выбраны")
        self.fileFlag = False
        self.fileNames = []

    def runCheckingCorrectness(self):  # Запуск проверки корректности
        if self.fileFlag:
            self.getSettings()
            self.ui.LEResLine.setText(f"Проверено файлов: 0")
            self.ui.LEResLine.show()
            for filename in self.fileNames:
                file, extension = os.path.splitext(filename)
                if extension == ".docx":
                    set_settings(self.text_checklist, self.heading1_checklist, self.heading2_checklist,
                                 self.heading3_checklist, self.table_title_checklist, self.table_heading_checklist,
                                 self.table_checklist, self.list_checklist, self.page_checklist, self.picture_checklist,
                                 self.title_picture_checklist)
                    parse_document(filename)
                self.ui.LEResLine.setText(f"Проверено файлов: {len(self.fileNames)}")
            self.ui.btnOpenRes.show()
            self.clearFiles()
        else:
            self.ui.LEErrorLine.show()  # Вывод сообщения об отсутствии выбранных файлов
            self.ui.LEResLine.hide()
            self.ui.btnOpenRes.hide()

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
            "font_size": float(self.SettingsWindow.ui.LEMainTextSize.text()),
            "font_bald": self.SettingsWindow.ui.CBMainTextBold.isChecked(),
            "font_italic": self.SettingsWindow.ui.CBMainTextItalic.isChecked(),
            "font_underline": self.SettingsWindow.ui.CBMainTextUnderline.isChecked(),
            "font_color": None,  # нет такого в UI
            "font_back_color": None,  # нет такого в UI
            "alignment": alignment,
            "keep_with_next": False,  # нет такого в UI, false по умолчанию для main текста
            "page_break_before": False,  # нет такого в UI, false по умолчанию для main текста
            "space_before": float(self.SettingsWindow.ui.LEMainTextSpacingBefore.text()),
            "space_after": float(self.SettingsWindow.ui.LEMainTextSpacingAfter.text()),
            "left_indent": 0,  # нет такого в UI
            "right_indent": 0,  # нет такого в UI
            "first_line_indent": float(self.SettingsWindow.ui.LEMainTextSpacingParagraph.text()),
            "line_spacing": float(self.SettingsWindow.ui.LEMainTextSpacingBetween.text()),
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
            "font_size": float(self.SettingsWindow.ui.LEFirstLvlSize.text()),
            "font_bald": self.SettingsWindow.ui.CBLVL1Bold.isChecked(),
            "font_italic": self.SettingsWindow.ui.CBLVL1Italic.isChecked(),
            "font_underline": self.SettingsWindow.ui.CBLVL1Underline.isChecked(),
            "font_color": None,  # нет такого в UI
            "font_back_color": None,  # нет такого в UI
            "alignment": alignment,
            "keep_with_next": self.SettingsWindow.ui.CBLVL1NotSpacing.isChecked(),
            "page_break_before": self.SettingsWindow.ui.CBLVL1NewPage.isChecked(),  # нет такого в UI, false по умолчанию для main текста
            "space_before": float(self.SettingsWindow.ui.LEFirstLvlSpacingBefore.text()),
            "space_after": float(self.SettingsWindow.ui.LEFirstLvlSpacingAfter.text()),
            "left_indent": 0,  # нет такого в UI
            "right_indent": 0,  # нет такого в UI
            "first_line_indent": 0,  # нет такого в UI
            "line_spacing": 1.0,  # нет такого в UI
            "is_list":  self.SettingsWindow.ui.CBLVL1CheckNumeration.isChecked()
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
            "font_size": float(self.SettingsWindow.ui.LESecondLvlSize.text()),
            "font_bald": self.SettingsWindow.ui.CBLVL2Bold.isChecked(),
            "font_italic": self.SettingsWindow.ui.CBLVL2Italic.isChecked(),
            "font_underline": self.SettingsWindow.ui.CBLVL2Underline.isChecked(),
            "font_color": None,  # нет такого в UI
            "font_back_color": None,  # нет такого в UI
            "alignment": alignment,
            "keep_with_next": self.SettingsWindow.ui.CBLVL2NotSpacing.isChecked(),
            "page_break_before": self.SettingsWindow.ui.CBLVL2NewPage.isChecked(),  # нет такого в UI, false по умолчанию для main текста
            "space_before": float(self.SettingsWindow.ui.LESecondLvlSpacingBefore.text()),
            "space_after": float(self.SettingsWindow.ui.LESecondLvlSpacingAfter.text()),
            "left_indent": 0,  # нет такого в UI
            "right_indent": 0,  # нет такого в UI
            "first_line_indent": 0,  # нет такого в UI
            "line_spacing": 1.0,  # нет такого в UI
            "is_list": self.SettingsWindow.ui.CBLVL2CheckNumeration.isChecked()
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
            "font_size": float(self.SettingsWindow.ui.LEThirdLvlSize.text()),
            "font_bald": self.SettingsWindow.ui.CBLVL3Bold.isChecked(),
            "font_italic": self.SettingsWindow.ui.CBLVL3Italic.isChecked(),
            "font_underline": self.SettingsWindow.ui.CBLVL3Underline.isChecked(),
            "font_color": None,  # нет такого в UI
            "font_back_color": None,  # нет такого в UI
            "alignment": alignment,
            "keep_with_next": self.SettingsWindow.ui.CBLVL3NotSpacing.isChecked(),
            "page_break_before": self.SettingsWindow.ui.CBLVL3NewPage.isChecked(),  # нет такого в UI, false по умолчанию для main текста
            "space_before": float(self.SettingsWindow.ui.LEThirdLvlSpacingBefore.text()),
            "space_after": float(self.SettingsWindow.ui.LEThirdLvlSpacingAfter.text()),
            "left_indent": 0,  # нет такого в UI
            "right_indent": 0,  # нет такого в UI
            "first_line_indent": 0,  # нет такого в UI
            "line_spacing": 1.0,  # нет такого в UI
            "is_list": self.SettingsWindow.ui.CBLVL3CheckNumeration.isChecked()
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

        orientation = WD_ORIENTATION.PORTRAIT
        if self.SettingsWindow.ui.LandscapeOrientation.isChecked():
            orientation = WD_ORIENTATION.LANDSCAPE

        self.page_checklist = {
            "top_margin": float(self.SettingsWindow.ui.LEFieldsTop.text()),  # Поля страницы (верхнее)
            "bottom_margin": float(self.SettingsWindow.ui.LEFieldsBottom.text()),  # Поля страницы (нижнее)
            "left_margin": float(self.SettingsWindow.ui.LEFieldsLeft.text()),  # Поля страницы (левое)
            "right_margin": float(self.SettingsWindow.ui.LEFieldsRight.text()),  # Поля страницы (правое)
            "NumberingPosition": numbering_position,  # Позиция нумерации (сверху, снизу, справа, слева)
            "NumberingStartFrom": self.SettingsWindow.ui.LENumerationStartFrom.text(),  # Число, с которого начинается нумерация
            "orientation": orientation
        }

    def getListSettings(self):
        self.list_checklist = {
            "NumberedListType": self.SettingsWindow.ui.CBNumberedListType.currentText(),  # Тип нумерации (1. 2. 3. / 1) 2) 3))
        }

    def getTableSettings(self):
        alignment = WD_ALIGN_PARAGRAPH.LEFT
        if self.SettingsWindow.ui.RBTableTextLeft.isChecked():
            alignment = WD_ALIGN_PARAGRAPH.LEFT
        elif self.SettingsWindow.ui.RBTableTextRight.isChecked():
            alignment = WD_ALIGN_PARAGRAPH.RIGHT
        elif self.SettingsWindow.ui.RBLVL3TextMiddle.isChecked():
            alignment = WD_ALIGN_PARAGRAPH.CENTER

        vertical_alignment = WD_ALIGN_PARAGRAPH.CENTER
        if self.SettingsWindow.ui.RBTableTextTop.isChecked():
            vertical_alignment = WD_ALIGN_VERTICAL.TOP
        elif self.SettingsWindow.ui.RBTableTextMiddle_2.isChecked():
            vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        elif self.SettingsWindow.ui.RBTableTextBottom.isChecked():
            vertical_alignment = WD_ALIGN_VERTICAL.BOTTOM

        heading_alignment = WD_ALIGN_PARAGRAPH.CENTER
        if self.SettingsWindow.ui.RBTableHeadingTextLeft.isChecked():
            heading_alignment = WD_ALIGN_PARAGRAPH.LEFT
        elif self.SettingsWindow.ui.RBTableHeadingTextRight.isChecked():
            heading_alignment = WD_ALIGN_PARAGRAPH.RIGHT
        elif self.SettingsWindow.ui.RBTableHeadingTextMiddle.isChecked():
            heading_alignment = WD_ALIGN_PARAGRAPH.CENTER

        self.table_checklist = {
            "font_name": self.SettingsWindow.ui.CBFontName.currentText(),  # Шрифт
            "font_size": float(self.SettingsWindow.ui.LETableFontSize.text()),  # Размер шрифта в таблице
            "paragraph_before_table": self.SettingsWindow.ui.CBTableParagraphBeforeTable.isChecked(),  # Параграф перед таблицей
            "space_before": float(self.SettingsWindow.ui.LETableSpacingBefore.text()),
            "space_after": float(self.SettingsWindow.ui.LETableSpacingAfter.text()),
            "left_indent": 0,  # нет такого в UI
            "right_indent": 0,  # нет такого в UI
            "first_line_indent": float(self.SettingsWindow.ui.LETableSpacingParagraph.text()),
            "line_spacing": float(self.SettingsWindow.ui.LETabletSpacingBetween.text()),
            "spacing_under_paragraph_after_table": float(self.SettingsWindow.ui.LETableParagraphSpacingAfter.text()),  # Интервал абзаца после таблицы
            "alignment": alignment,
            "vertical_alignment": vertical_alignment
        }

        self.table_title_checklist = {
            "format_regex": self.SettingsWindow.ui.CBTableFormatParagraph.currentText(), # Формат подписи под таблицей (Таблица <N> - <Название>)
        }

        self.table_heading_checklist = {
            "font_bald": self.SettingsWindow.ui.CBTableBold.isChecked(),  # Жирный шрифт заголовков
            "font_italic": self.SettingsWindow.ui.CBTableItalic.isChecked(),  # Курсив заголовков
            "font_underline": self.SettingsWindow.ui.CBTableUnderline.isChecked(),  # Подчеркивание заголовков
            "heading_left": self.SettingsWindow.ui.CBTableHeadingLeft.isChecked(),  # Необходимость заголовков слева
            "heading_top": self.SettingsWindow.ui.CBTableHeadingTop.isChecked(),  # Необходимость заголовков сверху
            "alignment": heading_alignment,
            "vertical_alignment": vertical_alignment
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
            "alignment": picture_alignment,  # Выравнивание картинки
            "keep_with_next": self.SettingsWindow.ui.CBPictureNotSpacing.isChecked(),  # Не отрывать рисунок от подписи
            "space_before": float(self.SettingsWindow.ui.LEPictureSpacingBefore.text()),
            "space_after": float(self.SettingsWindow.ui.LEPictureSpacingAfter.text()),
            "first_line_indent": float(self.SettingsWindow.ui.LEPicturetSpacingParagraph.text()),
            "line_spacing": float(self.SettingsWindow.ui.LEPictureSpacingBetween.text()),
        }

        self.title_picture_checklist = {
            "enable_pic_title": self.SettingsWindow.ui.CBPictureTitle.isChecked(),
            "font_name": self.SettingsWindow.ui.CBFontName.currentText(),  # Шрифт подписи под рисунком
            "font_size": float(self.SettingsWindow.ui.LEPictureFontSize.text()),  # Размер подписи под рисунком
            "font_bald": self.SettingsWindow.ui.CBPictureTitleBold.isChecked(),  # Выделение жирным шрифтом
            "font_italic": self.SettingsWindow.ui.CBPictureTitleItalic.isChecked(),  # Выделение курсовом
            "font_underline": self.SettingsWindow.ui.CBPictureTitleUnderline.isChecked(),  # Выделение подчеркиванием
            "space_before": float(self.SettingsWindow.ui.LEPictureTitleSpacingBefore.text()),  # интервал перед подписью
            "space_after": float(self.SettingsWindow.ui.LEPictureTitleSpacingAfter.text()),  # интервал после подписи
            "first_line_indent": float(self.SettingsWindow.ui.LEPictureTitleSpacingFirstLine.text()),  # Абзацный отступ
            "line_spacing": float(self.SettingsWindow.ui.LEPictureTitleSpacingBetween.text()),  # Междустрочный интервал
            "alignment": title_alignment,  # Выравнивание подписи
            "format_regex": self.SettingsWindow.ui.CBPictureTitleFormat.currentText()  # Формат подписи (Рисунок <N> - <Название>.)
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
