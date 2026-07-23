"""
Base Connector

This module defines the common interface for all domain connectors.
"""

from abc import ABC, abstractmethod

import pandas as pd


class BaseConnector(ABC):
    """
    Abstract base class for all domain connectors.

    Every domain connector must implement the extract() method
    and return a Pandas DataFrame.
    """

    @abstractmethod
    def extract(self) -> pd.DataFrame:
        """
        Extract data for a domain.

        Returns:
            pd.DataFrame:
                The extracted domain dataset.
        """
        raise NotImplementedError