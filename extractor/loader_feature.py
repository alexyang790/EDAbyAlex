import pandas as pd 
import numpy as np
import glob

class loader_feature:
    def load(self, sheet_name=None, file_type=None):
        try:

            # Reading Excel sheet name
            self.sheet_name = sheet_name or self.sheet_name # if sheet_name is None, use the sheet_name from the __init__ method
            if self.sheet_name is None:
                self.sheet_name = pd.ExcelFile(self.path).sheet_names
                # if execl file has only one sheet, load the sheet name
                if len(self.sheet_name) == 1:
                    self.sheet_name = self.sheet_name[0]
                else:
                    raise TypeError(f"\n\n\nData loaded as dictionary. There might be multiple sheets. Please specify the sheet name. \n Available sheet names: {self.sheet_name} \n")
            
            # Reading file type and loading the file
            self.file_type = file_type or self.file_type # if file_type is None, use the file_type from the __init__ method
            if self.file_type == ".xlsx":
                self.df = pd.read_excel(self.path, sheet_name = self.sheet_name)
            else:
                self.df = pd.read_csv(self.path)

            return self.df
            
        except Exception as e:
            raise

    def load_multiple_csv(self):
        try:
            file_list = [file for file in glob.glob(self.path + f"*{self.file_query}*.csv")]

            if not file_list:
                raise FileNotFoundError(f"No files found with the query: {self.file_query}")

            self.df = pd.concat([pd.read_csv(file) for file in file_list])
            return self.df
        
        except Exception as e:
            print(f"Error loading file: {e}. Please check the file path and query")

    def load_multiple_xlsx(self):
        try:
            file_list = [file for file in glob.glob(self.path + f"*{self.file_query}*.xlsx")]

            if not file_list:
                raise FileNotFoundError(f"No files found with the query: {self.file_query}")

            self.df = pd.concat([pd.read_excel(file) for file in file_list])
            return self.df
        
        except Exception as e:
            print(f"Error loading file: {e}. Please check the file path and query")