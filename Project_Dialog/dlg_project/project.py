# -*- coding: utf-8 -*-
"""
Dialog Project

Created on 12.05.2020

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""


from PyQt5 import uic
from PyQt5.QtWidgets import QDialog

from dlg_project.controller.cnt_project import CntProject


class DlgProject(QDialog):
    
    def __init__(self, parent=None):
        """Dialog Project."""
        
        QDialog.__init__(self, parent)
        uic.loadUi('dlg_project/view/dlg_project.ui', self)
        
        # Objects of the application.
        self.d_project = {}  # Dictionary with the data of the project.
        
        # Instances of classes.
        self.cnt_project = CntProject(self)
        
        # PyQt objects.
        self.lnt_project = self.lineEdit_project
        self.lnt_name = self.lineEdit_name
        self.lnt_company = self.lineEdit_company
        self.lnt_structure = self.lineEdit_structure
        self.lnt_author = self.lineEdit_author
        self.lnt_comments = self.lineEdit_comments
        self.btn_ok = self.pushButton_ok
        self.btn_cancel = self.pushButton_cancel
        
        # Add items to QLineEdit.
        self.d_project = self.cnt_project.project_initial_data()
        self.lnt_project.setText(self.d_project['project'])
        self.lnt_project.selectAll()
        self.lnt_name.setText(self.d_project['name'])
        self.lnt_company.setText(self.d_project['company'])
        self.lnt_structure.setText(self.d_project['structure'])
        self.lnt_author.setText(self.d_project['author'])
        self.lnt_comments.setText(self.d_project['comments'])
        
        # Events.
        self.btn_ok.clicked.connect(self.cnt_project.project_data)
        self.btn_ok.clicked.connect(self.reject)
        self.btn_ok.clicked.connect(self.project_dictionary)
        self.btn_cancel.clicked.connect(self.close)

    def project_dictionary(self):
        """Return the dictionary with the data."""

        return self.d_project
