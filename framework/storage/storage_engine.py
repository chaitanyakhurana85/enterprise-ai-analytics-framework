"""
Storage Engine

This module stores Pandas DataFrames in DuckDB.
"""

from pathlib import Path

import duckdb
import pandas as pd


class StorageEngine:
    """
    Handles persistence of DataFrames into DuckDB.
    """

    SUPPORTED_WRITE_MODES = {
        "replace",
        "append",
        "fail",
    }

    def __init__(self, database_path: str) -> None:
        self.database_path = Path(database_path)

    def store(
        self,
        dataframe: pd.DataFrame,
        table_name: str,
        write_mode: str = "replace",
    ) -> None:
        """
        Store a DataFrame in DuckDB.

        Parameters:
            dataframe:
                DataFrame to store.

            table_name:
                Destination DuckDB table.

            write_mode:
                Controls how existing tables are handled.

                Supported values:
                - replace
                - append
                - fail

        Raises:
            ValueError:
                If the DataFrame is empty or the write mode is unsupported.

            RuntimeError:
                If the table already exists when write_mode is "fail".
        """

        if dataframe.empty:
            raise ValueError(
                "Cannot store an empty DataFrame."
            )

        normalized_write_mode = write_mode.lower().strip()

        if normalized_write_mode not in self.SUPPORTED_WRITE_MODES:
            raise ValueError(
                "Unsupported write mode: "
                f"{write_mode}. Supported modes are: "
                f"{sorted(self.SUPPORTED_WRITE_MODES)}"
            )

        self.database_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        connection = duckdb.connect(
            str(self.database_path)
        )

        try:
            connection.register(
                "source_dataframe",
                dataframe,
            )

            table_exists = self._table_exists(
                connection=connection,
                table_name=table_name,
            )

            if normalized_write_mode == "replace":
                connection.execute(
                    f"""
                    CREATE OR REPLACE TABLE {table_name} AS
                    SELECT *
                    FROM source_dataframe
                    """
                )

            elif normalized_write_mode == "append":
                if table_exists:
                    connection.execute(
                        f"""
                        INSERT INTO {table_name}
                        SELECT *
                        FROM source_dataframe
                        """
                    )
                else:
                    connection.execute(
                        f"""
                        CREATE TABLE {table_name} AS
                        SELECT *
                        FROM source_dataframe
                        """
                    )

            elif normalized_write_mode == "fail":
                if table_exists:
                    raise RuntimeError(
                        f"DuckDB table already exists: {table_name}"
                    )

                connection.execute(
                    f"""
                    CREATE TABLE {table_name} AS
                    SELECT *
                    FROM source_dataframe
                    """
                )

        finally:
            connection.close()

        print(
            "Data stored successfully in DuckDB "
            f"table '{table_name}' using '{normalized_write_mode}' mode"
        )

    @staticmethod
    def _table_exists(
        connection: duckdb.DuckDBPyConnection,
        table_name: str,
    ) -> bool:
        """
        Check whether a table exists in DuckDB.
        """

        result = connection.execute(
            """
            SELECT COUNT(*)
            FROM information_schema.tables
            WHERE table_schema = 'main'
              AND table_name = ?
            """,
            [table_name],
        ).fetchone()

        return bool(result and result[0] > 0)