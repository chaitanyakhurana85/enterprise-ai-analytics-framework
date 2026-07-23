"""
Retail Connector

This module connects the retail domain configuration
to the appropriate data adapter.
"""

import pandas as pd

from framework.adapters.csv_adapter import CSVAdapter
from framework.connectors.base_connector import BaseConnector


class RetailConnector(BaseConnector):
    """
    Connector responsible for loading retail-domain data.

    The connector understands the retail data source configuration,
    while the adapter handles the technical details of reading the file.
    """

    def __init__(
        self,
        dataset_path: str,
        read_options: dict | None = None,
    ) -> None:
        self.dataset_path = dataset_path
        self.read_options = read_options or {}

    def extract(self) -> pd.DataFrame:
        """
        Load retail data through the configured adapter.

        Returns:
            pd.DataFrame:
                The extracted retail dataset.
        """

        adapter = CSVAdapter(
            file_path=self.dataset_path,
            read_options=self.read_options,
        )

        return adapter.read_data()