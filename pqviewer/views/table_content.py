from textual.app import Widget, ComposeResult
from textual.widgets import DataTable

from pqviewer.core.file_parser import FileParser


class TableContent(Widget):

    def __init__(self, parsed_file: FileParser) -> None:
        self.parsed_file = parsed_file
        super().__init__()

    def compose(self) -> ComposeResult:
        yield DataTable(id="datatable_content")

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table_content = self.parsed_file.to_table()
        table.add_columns(*table_content[0])
        table.add_rows(table_content[1:])
