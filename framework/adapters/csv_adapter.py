"""
CSV Adapter

This module provides a reusable adapter for reading CSV files
into a Pandas DataFrame.
"""

from pathlib import Path

import pandas as pd

from framework.adapters.base_adapter import BaseAdapter


class CSVAdapter(BaseAdapter):
    """
    Adapter for reading CSV files.

    Parameters:
        file_path: Path to the CSV file.
        read_options: Optional keyword arguments passed to pandas.read_csv().
    """

    def __init__(
        self,
        file_path: str,
        read_options: dict | None = None,
    ) -> None:
        self.file_path = Path(file_path)
        self.read_options = read_options or {}

    def read_data(self) -> pd.DataFrame:
        """
        Read the configured CSV file and return a Pandas DataFrame.

        Raises:
            FileNotFoundError:
                If the configured CSV file does not exist.

            ValueError:
                If the CSV file is empty.

        Returns:
            pd.DataFrame:
                The loaded dataset.
        """

        if not self.file_path.exists():
            raise FileNotFoundError(
                f"CSV file was not found: {self.file_path}"
            )

        dataframe = pd.read_csv(
            self.file_path,
            **self.read_options,
        )

        if dataframe.empty:
            raise ValueError(
                f"CSV file contains no data: {self.file_path}"
            )

        return dataframe