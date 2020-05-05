# -*- coding: utf-8 -*-
"""
PyQt5 pills
Mainwindow calls Dialog

Created on 04.05.2020

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = structural.eng.biel@gmail.com
"""


from PyQt5 import uic
from PyQt5.QtWidgets import QDialog

from dialog_MVC.controller.cnt_dialog import CntDialog


class Dialog(QDialog):
    
    def __init__(self, parent=None):
        """Dialog of the application."""
        
        QDialog.__init__(self, parent)
        uic.loadUi('view/dialog.ui', self)
        
        # Objects of the application.
        self.d_dlg_data = {}
        
        # Instances of the classes.
        self.cnt_dialog = CntDialog(self)
        
        # PyQt5 objects
        self.dlg_input1 = self.lineEditInput1
        self.dlg_input2 = self.lineEditInput2
        self.btn_apply = self.pushButtonApply
        self.btn_cancel = self.pushButtonCancel
        
        # Add items to QLineEdit.
        self.d_dlg_data = self.cnt_dialog.dialog_initial_data()
        self.dlg_input1.setText(self.d_dlg_data['input1'])
        self.dlg_input1.selectAll()
        self.dlg_input2.setText(self.d_dlg_data['input2'])
        
        # Events.
        self.btn_apply.clicked.connect(self.cnt_dialog.dialog_data)
        self.btn_apply.clicked.connect(self.reject)
        self.btn_cancel.clicked.connect(self.close)
        
    def d_dialog_data(self):
        """Returns the dictionary with the data."""
        
        return self.d_dlg_data
