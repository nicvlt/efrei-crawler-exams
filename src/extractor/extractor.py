import pandas as pd
import os
from dotenv import load_dotenv

from ..navigator.navigator import Navigator
from .utils.functions import concat_dataframes, check_class, filter_row_by_name
from .utils.constants import ALL_CLASSES, USEFUL_COLUMNS

load_dotenv()


class Extractor:
    def __init__(self, lastname: str = None):
        """Extractor class constructor

        Args:
            lastname (str): student's lastname. Defaults to None.
        """

        self.lastname = lastname
        self.navigator = Navigator()

    def extract_info(self):
        """Extract student's information from the website"""

        if not os.listdir("tmp"):
            self.navigator.run(os.getenv("MOODLE_ID"), os.getenv("MOODLE_PASSWORD"))

        df = pd.DataFrame()
        with os.scandir("tmp") as files:
            for file in files:
                df = concat_dataframes(df, pd.read_excel(file.path))

        print("Classes available:", ALL_CLASSES)
        user_class: str = None
        while not check_class(user_class):
            user_class = input("Class: ")

        # TODO: Fix to containing (careful with L1 and L1INT)
        df = df[df["liste des pgm"] == user_class]
        df = df.loc[:, USEFUL_COLUMNS]

        # use filter_row_by_name to filter rows on dataframe
        if self.lastname:
            return df[
                df.apply(lambda row: filter_row_by_name(row, self.lastname), axis=1)
            ]

        return df
