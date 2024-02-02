from typing import List

import pyarrow.parquet as pq


class FileParser:
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        self.table = pq.read_table(self.file_name)

    def schema(self) -> List[tuple]:
        """Transform table schema to list."""

        return [
            (name, str(self.table.schema.field(name).type))
            for name in self.table.column_names
        ]

    def to_table(self) -> List[tuple]:
        """Transform table content to list."""

        table_header = [tuple(self.table.column_names)]
        table_content = [tuple(row.values()) for row in self.table.to_pylist()]
        return table_header + table_content

    def __len__(self) -> int:
        return len(self.table)
