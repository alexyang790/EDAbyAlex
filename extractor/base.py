import pandas as pd 
import numpy as np
import os 
import glob 
from .eda_feature import eda_feature
from .loader_feature import loader_feature
from .unique_val_feature import unique_val_feature
from .export_feature import export_feature

class extractor(eda_feature, loader_feature, unique_val_feature, export_feature):
    def __init__(self, path, file_type = None, sheet_name = None, file_query = None):
        
        self.path = path
        self.file_type = file_type
        self.sheet_name = sheet_name
        self.file_query = file_query
        self.df = None
        self.unique = None
    

