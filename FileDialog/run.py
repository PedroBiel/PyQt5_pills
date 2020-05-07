# -*- coding: utf-8 -*-
"""
PyQt5 pills
QFileDialog

Created on 05.05.2020

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = structural.eng.biel@gmail.com
"""

import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

from pyqt5_recipes.filedialog import FileDialog

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        """Call a dialog that allow users to select files or directorie."""

        QMainWindow.__init__(self, parent)
        uic.loadUi('view/mainwindow.ui', self)
        
        # PyQt5 objects.
        self.btn_existing_dir = self.pushButtonExistingDirectory
        self.btn_open_file_name = self.pushButtonOpenFileName
        self.btn_save_file_name = self.pushButtonSaveFileName
        self.lbl = self.label
        
        # Events.
        self.btn_existing_dir.clicked.connect(self.existing_directory)
        self.btn_open_file_name.clicked.connect(self.open_file_name)
        self.btn_save_file_name.clicked.connect(self.save_file_name)
 
    def existing_directory(self):
        """Return an existing directory selected by the user as string."""

        caption = 'Caption'
        directory = 'C:/'
        file_dialog = FileDialog(caption, directory)
        dirctr = file_dialog.get_existing_directory()
        
        self.lbl.setText(dirctr)
 
    def open_file_name(self):
        """
        Return from existing file selected by the user the directory and the
        file name as one string.
        """

        caption = 'Caption'
        directory = 'C:/'
        filter = 'Text files (*.txt);; Images (*.png *.jpg)'
        file_dialog = FileDialog(caption, directory, filter)
        dir_file_name = file_dialog.get_open_file_name()
        
        self.lbl.setText(dir_file_name)
    
    def save_file_name(self):
        """
        Return the directory and the file name selected by the user as one
        string.
        """

        caption = 'Caption'
        directory = 'C:/'
        filter = 'Text files (*.txt);; Images (*.png *.jpg)'
        file_dialog = FileDialog(caption, directory, filter)
        dir_file_name = file_dialog.get_save_file_name()
        
        self.lbl.setText(dir_file_name)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())
