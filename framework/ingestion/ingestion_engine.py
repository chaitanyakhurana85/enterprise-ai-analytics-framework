"""
Ingestion Engine

This module coordinates data extraction through a domain connector.
"""

import pandas as pd

from framework.connectors.base_connector import BaseConnector


class IngestionEngine:
    """
    Executes data ingestion using a configured domain connector.
    """

    def __init__(self, connector: BaseConnector) -> None:
        self.connector = connector

    def run(self) -> pd.DataFrame:
        """
        Execute the ingestion process.

        Returns:
            pd.DataFrame:
                The ingested dataset.
        """

        dataframe = self.connector.extract()

        print("Ingestion completed successfully")
        print(f"Rows ingested: {len(dataframe)}")
        print(f"Columns ingested: {len(dataframe.columns)}")

        return dataframe