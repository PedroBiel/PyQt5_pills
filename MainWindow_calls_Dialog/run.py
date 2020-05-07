# -*- coding: utf-8 -*-
"""
PyQt5 pills
Mainwindow calls Dialog

Created on 04.05.2020

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = structural.eng.biel@gmail.com
"""

import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

from dialog import Dialog


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        """Run the MainWindow and calls the Dialog."""

        QMainWindow.__init__(self, parent)
        uic.loadUi('view/mainwindow.ui', self)
        
        # App objects.
        self.d_data = {}
        
        # PyQt5 objects.
        self.btn_call_dialog = self.pushButtonCallDialog
        self.btn_refresh = self.pushButtonRefresh
        self.input1 = self.labelInput1
        self.input2 = self.labelInput2
        
        # Instances of the classes.
        self.dialog = Dialog(self)
        
        # Events.
        self.btn_call_dialog.clicked.connect(self.call_dialog)
        self.btn_refresh.clicked.connect(self.get_dialog_inputs)
    
    def call_dialog(self):
        """Call the Dialog."""
        
        self.dialog.show()
        self.d_data = self.dialog.d_dialog_data()
        # self.get_dialog_inputs()
        
    def get_dialog_inputs(self):
        """Display the inputs of the Dialog in the MainWindow."""
        
        dlg = self.dialog
        dlg_data = dlg.d_dialog_data()
        self.input1.setText(dlg_data['input1'])
        self.input2.setText(dlg_data['input2'])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())
