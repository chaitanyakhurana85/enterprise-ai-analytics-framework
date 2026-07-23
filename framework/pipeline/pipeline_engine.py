"""
Pipeline Engine

This module coordinates the execution of framework pipeline steps.
"""

from typing import Any, Dict

import pandas as pd

from domains.retail.connectors.retail_connector import RetailConnector
from framework.ingestion.ingestion_engine import IngestionEngine
from framework.storage.storage_engine import StorageEngine


class PipelineEngine:
    """
    Coordinates the execution of framework pipeline steps.
    """

    def __init__(
        self,
        active_domain: str,
        domain_settings: Dict[str, Any],
        database_path: str,
    ) -> None:
        self.active_domain = active_domain
        self.domain_settings = domain_settings
        self.database_path = database_path

    def execute(self) -> pd.DataFrame:
        """
        Execute the configured pipeline in sequence.

        Returns:
            pd.DataFrame:
                The ingested and stored dataset.
        """

        print("Starting pipeline execution...")
        print(f"Pipeline domain: {self.active_domain}")
        print("Step 1: Configuration loaded")

        connector = self._create_connector()

        print("Step 2: Connector created")

        ingestion_engine = IngestionEngine(
            connector=connector
        )

        dataframe = ingestion_engine.run()

        print("Step 3: Validation pending")
        print("Step 4: Transformation pending")

        table_name = self.domain_settings["database"]["table"]

        storage_engine = StorageEngine(
            database_path=self.database_path
        )

        storage_engine.store(
            dataframe=dataframe,
            table_name=table_name,
            write_mode="replace",
        )

        print("Step 5: Storage completed")
        print("Pipeline execution completed successfully")

        return dataframe

    def _create_connector(self) -> RetailConnector:
        """
        Create the connector for the active domain.

        Returns:
            RetailConnector:
                The configured retail connector.

        Raises:
            ValueError:
                If the active domain or dataset format is unsupported.
        """

        if self.active_domain == "retail":
            dataset_config = self.domain_settings["dataset"]

            dataset_path = dataset_config["path"]
            dataset_format = dataset_config["format"].lower()

            if dataset_format != "csv":
                raise ValueError(
                    f"Unsupported retail dataset format: {dataset_format}"
                )

            return RetailConnector(
                dataset_path=dataset_path
            )

        raise ValueError(
            f"Unsupported domain: {self.active_domain}"
        )