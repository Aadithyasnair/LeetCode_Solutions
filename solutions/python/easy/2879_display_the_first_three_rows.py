"""
Problem ID : 2879
Title      : Display the First Three Rows
Language   : Pandas
Topics     : DataFrame
Solved Date: 2026-07-17
"""

import pandas as pd


def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)
