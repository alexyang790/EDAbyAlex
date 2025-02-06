import pandas as pd 
import numpy as np 

class unique_val_feature:
    def print_unique(self):
        for column, unique_value in self.unique.items():
            print(f"\nUnique values in {column}: \n {unique_value}\n\n")
        return

    def columns(self):
        print(self.df.columns) 
        return
    
    def unique_values(self, col_name = None):
        col_name = col_name
        if col_name is None:
            raise TypeError("Please specify the column name that you want to retrieve unique values from")  
        try:
            print (f"Unique values in {col_name} \n {self.unique[col_name]}")
            return
        except KeyError:
            print(f"Column '{col_name}' does not exist. Please provide a valid column name.")