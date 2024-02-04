from textual.app import Widget, ComposeResult
from textual.widgets import DataTable

from pqviewer.file_parser import FileParser


class TableSchema(Widget):

    def __init__(self, parsed_file: FileParser) -> None:
        self.parsed_file = parsed_file
        super().__init__()

    def compose(self) -> ComposeResult:
        yield DataTable()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.styles.border = ("heavy", "#F8DE7E")
        table.border_title = "Schema"
        table.styles.scrollbar_color = "#F8DE7E"
        table.styles.scrollbar_color_active = "#F8DE7E"
        table.styles.scrollbar_color_hover = "#F8DE7E"
        table.add_columns(*[("column", "type")][0])
        table.add_rows(self.parsed_file.schema())
