from textual.app import Widget, ComposeResult
from textual.widgets import Label

from pqviewer.core.file_parser import FileParser


class TableHeader(Widget):

    def __init__(self, parsed_file: FileParser, id: str) -> None:
        self.file_name = parsed_file.file_name
        super().__init__(id=id)

    def compose(self) -> ComposeResult:
        yield Label(self.file_name, shrink=True)

    def on_mount(self) -> None:
        self.styles.height = "auto"
        self.border_title = "File"
        self.styles.color = "#777"
