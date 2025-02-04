import pandas as pd 
import numpy as np

class data_eda:
    def __init__(self, path):
        """
        Initialize the data_eda class.

        Parameters
        ----------
        path : str
            The path to the Excel file to be analyzed.

        Attributes
        ----------
        path : str
            The path to the Excel file to be analyzed.
        df : DataFrame
            The loaded DataFrame from the Excel file.
        unique : dict
            A dictionary where the key is the column name and the value is a list of unique values in that column.
        """
        self.path = path
        self.df = None
        self.unique = None
    
    def load(self):
        """
        Load the Excel file into a DataFrame.

        Returns
        -------
        df : DataFrame
            The loaded DataFrame from the Excel file.

        Raises
        ------
        Exception
            If there is an error loading the file.
        """
        try:
            self.df = pd.read_excel(self.path)
            return self.df
        except Exception as e:
            print(f"Error loading file: {e}")
            raise
    
    def eda(self):
        """
        Perform exploratory data analysis on the loaded DataFrame.

        This function calculates unique values and missing values for each column in the DataFrame.
        It then prints out various descriptive statistics and information including a data preview,
        data description, data info, column names, unique values per column, and missing values count.

        Raises
        ------
        ValueError
            If the DataFrame has not been loaded, i.e., `load()` has not been called.
        """
        
        if self.df is None:
            raise ValueError("Please call load() before running eda()")
            
        self.unique = {col: self.df[col].unique() for col in self.df.columns}
        self.missing = self.df.isnull().sum()
        
        output = [
            ("Data preview", self.df.head(10)),
            ("Data description", self.df.describe()),
            ("Data info", self.df.info()),
            ("Data columns", self.df.columns),
            ("Unique values in each column", self.unique),
            ("Missing values", self.missing)
        ]
        
        for description, data in output:
            print(f"{description}:\n{data}\n\n\n")
        
        return
    
    def print_unique(self):
        """
        Prints out unique values for each column in the DataFrame.

        This function prints out the name of each column and the unique values in that column.
        It is a utility function for exploratory data analysis.

        Returns
        -------
        None
        """
        for column, unique_value in self.unique.items():
            print(f"Unique values in {column}: \n {unique_value}\n\n")
        return

    def columns(self):
        """
        Prints out all the columns in the DataFrame.

        This function is a utility function for exploratory data analysis.
        It prints out all the columns in the DataFrame.

        Returns
        -------
        None
        """
        print(self.df.columns) 
        return
    
    def unique_values(self, col_name):
        """
        Prints out unique values for the specified column in the DataFrame.

        This function prints out the name of the column and the unique values in that column.
        It is a utility function for exploratory data analysis.

        Parameters
        ----------
        col_name : str
            The column name to get the unique values for.

        Returns
        -------
        None
        """
        print (f"Unique values in {col_name} \n {self.unique[col_name]}")
        return

