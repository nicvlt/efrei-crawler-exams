import pandas as pd

from .constants import ALL_CLASSES


def concat_dataframes(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    """Concatenate two dataframes

    Args:
        df1 (pd.DataFrame): first dataframe
        df2 (pd.DataFrame): second dataframe

    Returns:
        pd.DataFrame: concatenated dataframe
    """
    return pd.concat([df1, df2], axis=0)


def check_class(class_name: str) -> bool:
    """Check if the class exists

    Args:
        class_name (str): class name

    Returns:
        bool: True if the class exists, False otherwise
    """
    return class_name in ALL_CLASSES


def is_between(name: str, first_student: str, last_student: str) -> bool:
    """Check if the name is between the first and last student

    Args:
        name (str): Name to check
        first_student (str): First student's name in the interval
        last_student (str): Last student's name in the interval

    Returns:
        bool: True if the name is between the first and last student
    """
    name = name.lower()
    first_student = first_student.lower()
    last_student = last_student.lower()

    return (
        first_student <= name <= last_student or last_student <= name <= first_student
    )


def filter_row_by_name(df: pd.DataFrame, lastname: str) -> bool:
    """Filter rows by lastname

    Args:
        df (pd.DataFrame): dataframe
        lastname (str): lastname

    Returns:
        bool: True if the name is in the row
    """
    name_col: str = df["Salle "]
    name_col = name_col.split(":")

    # Handle special case: Tiers-temps
    if len(name_col) == 1:
        return True

    name_col = name_col[1].strip().split(" ")

    first_student = name_col[1]
    last_student = name_col[3]

    return is_between(lastname, first_student, last_student)
