# -*- coding: utf-8 -*-
"""
PyQt5 pills
Mainwindow calls Dialog Project

Created on 12.05.2020

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = structural.eng.biel@gmail.com
"""

import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

from dlg_project.project import DlgProject


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        """Run the MainWindow and calls the Dialog Project."""

        QMainWindow.__init__(self, parent)
        uic.loadUi('view/mainwindow.ui', self)
        
        # App objects.
        self.d_data = {}  # Dictionary with the data of the project.
        
        # PyQt5 objects.
        self.axn_project = self.actionProject
        self.btn_show_project_data = self.pushButton_ShowProjectData
        self.txt_data = self.textEdit_data
        
        # Instances of the classes.
        self.dlg_project = DlgProject(self)
        
        # Events.
        self.axn_project.triggered.connect(self.call_dialog_project)
        self.btn_show_project_data.clicked.connect(self.get_dialog_project)
        
    
    def call_dialog_project(self):
        """Call the Dialog Project."""

        self.dlg_project.show()
        
    def get_dialog_project(self):
        """Display the inputs of the Dialog in the MainWindow."""

        dlg = self.dlg_project
        dlg_data = dlg.project_dictionary()
        self.txt_data.setText(str(dlg_data))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())
    