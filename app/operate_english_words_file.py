import os

import pandas as pd


class File:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_extension = self.get_file_extensions()
        self.file_type = File.check_file_type(self.file_extension)
        self.df = self.load_file()
        self.drop_nan()
        self.rm_whitespace()

    def get_file_extensions(self):
        """
        check file extension.
        return file extension.

        param
        --------------------
        None

        return
        --------------------
        extension: str
    """
        extension = os.path.splitext(self.file_path)[1]
        return extension

    @staticmethod
    def check_file_type(file_extension):
        """
        check file extension.
        if extension is nethier xlsx or csv, return 'not supported'.

        param
        --------------------
        file_extension: str

        return
        --------------------
        'csv' or 'xlsx' or 'not supported'
        """
        if file_extension == '.xlsx' or file_extension == '.xls':
            return 'excel'
        elif file_extension == '.csv':
            return 'csv'
        else:
            return 'not supported'

    def load_file(self):
        """
        load file, return df.

        param
        --------------------
        None

        return
        --------------------
        df: DataFrame
        """
        df = pd.read_csv(self.file_path)

        return df

    def drop_nan(self):
        """
        remove Not a number.

        param
        --------------------
        None

        return
        --------------------
        None
        """
        self.df = self.df.dropna()

    def rm_whitespace(self):
        """
        remove whitespace

        param
        --------------------
        None

        return
        --------------------
        None
        """
        self.df['English'] = self.df['English'].str.strip()
        self.df['Japanese'] = self.df['Japanese'].str.strip()


if __name__ == '__main__':
    pass
