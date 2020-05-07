# -*- coding: utf-8 -*-
"""
PyQt5 pills
MessageBox

Created on 04.05.2020

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = structural.eng.biel@gmail.com
"""

import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

from pyqt5_recipes.messagebox import MessageBox

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        """Call a MessageBox."""

        QMainWindow.__init__(self, parent)
        uic.loadUi('view/mainwindow.ui', self)
        
        # PyQt5 objects.
        self.btn_question = self.pushButtonMsgBoxQuestion
        self.btn_information = self.pushButtonMsgBoxInformation
        self.btn_warning = self.pushButtonMsgBoxWarning
        self.btn_critical = self.pushButtonMsgBoxCritical
        self.btn_question_detail_text = self.pushButtonMsgBoxQuestionDetailedText
        self.btn_information_detail_text = self.pushButtonMsgBoxInformationDetailedText
        self.btn_warning_detail_text = self.pushButtonMsgBoxWarningDetailedText
        self.btn_critical_detail_text = self.pushButtonMsgBoxCriticalDetailedText
        
        # Events.
        self.btn_critical.clicked.connect(self.messagebox_critical)
        self.btn_information.clicked.connect(self.messagebox_information)
        self.btn_question.clicked.connect(self.messagebox_question)
        self.btn_warning.clicked.connect(self.messagebox_warning)
        self.btn_critical_detail_text.clicked.connect(self.messagebox_critical_detail_text)
        self.btn_information_detail_text.clicked.connect(self.messagebox_information_detail_text)
        self.btn_question_detail_text.clicked.connect(self.messagebox_question_detail_text)
        self.btn_warning_detail_text.clicked.connect(self.messagebox_warning_detail_text)
    
    def messagebox_critical(self):
        """
        Given the window title, text and informative text
        provide a modal dialog for reporting critical errors.
        """
        
        window_title = 'Window Title'
        text = 'This is critical.'
        info_text = 'This is the information for the critical issue.'
        self.messagebox = MessageBox(window_title, text, info_text)
        self.messagebox.critical()
    
    def messagebox_information(self):
        """
        Given the window title, text and informative text
        provide a modal dialog for reporting information about normal operations.
        """
        
        window_title = 'Window Title'
        text = 'This is a information.'
        info_text = 'This is the information for the information.'
        self.messagebox = MessageBox(window_title, text, info_text)
        self.messagebox.information()

    def messagebox_question(self):
        """
        Given the window title, text and informative text
        provide a modal dialog for rasking a question during normal operations.
        """
        
        window_title = 'Window Title'
        text = 'This is a question.'
        info_text = 'This is the information for the question.'
        self.messagebox = MessageBox(window_title, text, info_text)
        self.messagebox.question()
    
    def messagebox_warning(self):
        """
        Given the window title, text and informative text
        provide a modal dialog for reporting non-critical errors.
        """
        
        window_title = 'Window Title'
        text = 'This is a warning.'
        info_text = 'This is the information for the warning.'
        self.messagebox = MessageBox(window_title, text, info_text)
        self.messagebox.warning()
    
    def messagebox_critical_detail_text(self):
        """
        Given the window title, text, informative text and a detailed text
        provide a modal dialog for reporting critical errors.
        """
        
        window_title = 'Window Title'
        text = 'This is critical.'
        info_text = 'This is the information for the critical issue.'
        detail_text = 'Spam, eggs.'
        self.messagebox = MessageBox(window_title, text, info_text, detail_text)
        self.messagebox.critical_detailed_text()
    
    def messagebox_information_detail_text(self):
        """
        Given the window title, text, informative text and a detailed text
        provide a modal dialog for reporting information about normal operations.
        """
        
        window_title = 'Window Title'
        text = 'This is a information.'
        info_text = 'This is the information for the information.'
        detail_text = 'Spam, eggs.'
        self.messagebox = MessageBox(window_title, text, info_text, detail_text)
        self.messagebox.information_detailed_text()

    def messagebox_question_detail_text(self):
        """
        Given the window title, text, informative text and a detailed text
        provide a modal dialog for rasking a question during normal operations.
        """
        
        window_title = 'Window Title'
        text = 'This is a question.'
        info_text = 'This is the information for the question.'
        detail_text = 'Spam, eggs.'
        self.messagebox = MessageBox(window_title, text, info_text, detail_text)
        self.messagebox.question_detailed_text()
    
    def messagebox_warning_detail_text(self):
        """
        Given the window title, text, informative text and a detailed text
        provide a modal dialog for reporting non-critical errors.
        """
        
        window_title = 'Window Title'
        text = 'This is a warning.'
        info_text = 'This is the information for the warning.'
        detail_text = 'Spam, eggs.'
        self.messagebox = MessageBox(window_title, text, info_text, detail_text)
        self.messagebox.warning_detailed_text()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())
