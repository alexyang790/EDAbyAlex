import os

class export_feature:
    def export(self, file_type = None, file_name = None):
        file_type = file_type or self.file_type # if file_type is None, use the file_type from the __init__ method
        file_name = file_name or os.path.splitext(os.path.basename(self.path))[0]        
        # Determine the file type and save the DataFrame as subsequent file type
        
        # Checking if self.df exists
        if self.df is None:
            raise ValueError("Please call load() before running export()")

        # Exporting the file
        if file_type == ".xlsx":
            self.df.to_excel(f"{file_name}.xlsx", index = False)
        else:
            self.df.to_csv(f"{file_name}.csv", index = False)
        return
