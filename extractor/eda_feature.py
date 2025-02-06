class eda_feature:
    def eda(self):
        if self.df is None:
            raise ValueError("Please call load() before running eda()")
            
        self.unique = {col: self.df[col].unique() for col in self.df.columns}
        self.missing = self.df.isnull().sum()
        
        output = [
            ("\n\nData preview", self.df.head(10)),
            ("Data description", self.df.describe()),
            ("Data info", self.df.info()),
            ("Data columns", self.df.columns),
            ("Unique values in each column", self.unique),
            ("Missing values", self.missing)
        ]
        
        for description, data in output:
            print(f"{description}:\n{data}\n\n\n")
        
        return