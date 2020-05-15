# -*- coding: utf-8 -*-
"""
PyQt5 pills
Show Dialog with QWebEngineView

Created on 14.05.2020

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = structural.eng.biel@gmail.com
"""

import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

from dlg_web.web import DlgWeb


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        """Run the MainWindow and calls the Dialog with QWebEngineView."""

        QMainWindow.__init__(self, parent)
        uic.loadUi('view/mainwindow.ui', self)
       
        # PyQt5 objects.
        self.axn_about = self.actionAbout
        
        # Instances of the classes.
        self.dlg_web = DlgWeb(self)
        
        # Events.
        self.axn_about.triggered.connect(self.call_dialog_web)       
    
    def call_dialog_web(self):
        """Call the Dialog Web."""

        self.dlg_web.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())
    