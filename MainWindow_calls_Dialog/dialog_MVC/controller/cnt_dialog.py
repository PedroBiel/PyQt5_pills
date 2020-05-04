# -*- coding: utf-8 -*-
"""
PyQt5 pills
Mainwindow calls Dialog

Created on 04.05.2020

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = structural.eng.biel@gmail.com
"""


from dialog_MVC.data.initialdialog import InitialDataDialog


class CntDialog:
    
    def __init__(self, dialog):
        """Controler of the dialog data."""
        
        self.d = dialog
                
    def dialog_initial_data(self):
        initial_data = InitialDataDialog.DATA
        
        return initial_data
        
    def dialog_data(self):
        input1 = self.d.dlg_input1.text()
        input2 = self.d.dlg_input2.text()
        self.d.d_dlg_data['input1'] = input1
        self.d.d_dlg_data['input2'] = input2
        
        return self.d.d_dlg_data