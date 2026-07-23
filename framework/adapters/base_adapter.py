"""
Base Adapter

This module defines the common interface for all data adapters.

Every adapter in the framework (CSV, Excel, Snowflake,
BigQuery, REST API, etc.) must inherit from this class
and implement the read_data() method.
"""

from abc import ABC, abstractmethod


class BaseAdapter(ABC):
    """
    Abstract base class for all data adapters.
    """

    @abstractmethod
    def read_data(self):
        """
        Read data from a source and return a Pandas DataFrame.

        Returns:
            pandas.DataFrame
        """
        pass