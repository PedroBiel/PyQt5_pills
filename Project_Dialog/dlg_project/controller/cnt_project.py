# -*- coding: utf-8 -*-
"""
Controller Project

Created on 12.05.2020

__author__ = Pedro Biel
__version__ = 0.0.0
__email__ = pbiel@taimweser.com
"""


from dlg_project.data.initial_data import ProjectInitialData


class CntProject:
    
    def __init__(self, dialog):
        """Controler of the dialog Project."""
        
        self.d = dialog

    def project_initial_data(self):
        """Initial data of the project."""
        
        initial_data = ProjectInitialData.INITIAL_DATA
        
        return initial_data
        
    def project_data(self):
        """Dictionary with the data of the project."""
        
        project = self.d.lnt_project.text()
        name = self.d.lnt_name.text()
        company = self.d.lnt_company.text()
        structure = self.d.lnt_structure.text()
        author = self.d.lnt_author.text()
        comments = self.d.lnt_comments.text()
        
        self.d.d_project['project'] = project
        self.d.d_project['name'] = name
        self.d.d_project['company'] = company
        self.d.d_project['structure'] = structure
        self.d.d_project['author'] = author
        self.d.d_project['comments'] = comments
        
        return self.d.d_project
