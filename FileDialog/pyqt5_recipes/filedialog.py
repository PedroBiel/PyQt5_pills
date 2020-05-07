# -*- coding: utf-8 -*-
"""
PyQt5 pills
QFileDialog

Created on 05.05.2020

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = structural.eng.biel@gmail.com
"""


from PyQt5.QtWidgets import QFileDialog


class FileDialog:
    
    def __init__(self, caption, directory='', filter=''):
        """
        The QFileDialog class enables a user to traverse the file system in
        order to select one or many files or a directory.
        """
        
        self.caption = caption
        self.dir = directory
        self.ftr = filter

    def get_existing_directory(self):
        """Return an existing directory selected by the user as string."""

        directory = QFileDialog.getExistingDirectory(
                caption=self.caption,
                directory=self.dir,
                options=QFileDialog.ShowDirsOnly
                )

        return directory
    
    def get_open_file_name(self):
        """
        Return from existing file selected by the user the directory and the
        file name as one string.
        """

        dir_file_name = QFileDialog.getOpenFileName(
                caption=self.caption,
                directory=self.dir,
                filter=self.ftr
                )

        return dir_file_name[0]

    def get_save_file_name(self):
        """
        Return the directory and the file name selected by the user as one
        string.
        """

        dir_file_name = QFileDialog.getSaveFileName(
                caption=self.caption,
                directory=self.dir,
                filter=self.ftr
                )

        return dir_file_name[0]
