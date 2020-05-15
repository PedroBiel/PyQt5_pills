# -*- coding: utf-8 -*-
"""
PyQt5 pills
Show Dialog with information of the version in QTextEdit

Created on 14.05.2020

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = structural.eng.biel@gmail.com
"""

import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

from dlg_version.version import DlgVersion


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        """
        Run the MainWindow and calls the Dialog with QTextEdit with some
        information.
        """

        QMainWindow.__init__(self, parent)
        uic.loadUi('view/mainwindow.ui', self)
    
        
        # PyQt5 objects.
        self.axn_version = self.actionVersion
        
        # Instances of the classes.
        self.dlg_version = DlgVersion(self)
        
        # Events.
        self.axn_version.triggered.connect(self.call_dialog_version)       
    
    def call_dialog_version(self):
        """Call the Dialog Version."""

        self.dlg_version.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())
    