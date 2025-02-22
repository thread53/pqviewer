from textual.app import Widget, ComposeResult
from textual.widgets import DataTable

from pqviewer.core.file_parser import FileParser


class TableSchema(Widget):

    def __init__(self, parsed_file: FileParser) -> None:
        self.parsed_file = parsed_file
        super().__init__()

    def compose(self) -> ComposeResult:
        yield DataTable(id="datatable_schema")

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns(*[("column", "type")][0])
        table.add_rows(self.parsed_file.schema())
