import pandas as pd
import os
from dotenv import load_dotenv

from ..navigator.navigator import Navigator
from .utils.functions import (
    concat_dataframes,
    check_class,
    filtering_row_by_year,
    filter_row_by_name,
)
from .utils.constants import ALL_YEARS, USEFUL_COLUMNS

load_dotenv()


class Extractor:
    def __init__(self, lastname: str = None):
        """Extractor class constructor

        Args:
            lastname (str, optional): student's lastname. Defaults to None.
        """

        self.lastname = lastname
        self.navigator = Navigator()

    def extract_info(self):
        """Extract student's information"""

        if not os.listdir("tmp"):
            self.navigator.run(os.getenv("MOODLE_ID"), os.getenv("MOODLE_PASSWORD"))

        df = pd.DataFrame()
        with os.scandir("tmp") as files:
            for file in files:
                df = concat_dataframes(df, pd.read_excel(file.path))

        print("\n\nYears available:", ALL_YEARS)
        user_year: str = None
        while not check_class(user_year):
            user_year = input("Enter your year: ")

        df = df[df.apply(lambda row: filtering_row_by_year(row, user_year), axis=1)]
        df = df.loc[:, USEFUL_COLUMNS]

        if self.lastname:
            return df[
                df.apply(lambda row: filter_row_by_name(row, self.lastname), axis=1)
            ]

        return df
