from textual.app import Widget, ComposeResult
from textual.widgets import Label

from pqviewer.file_parser import FileParser


class TableHeader(Widget):

    def __init__(self, parsed_file: FileParser):
        self.file_name = parsed_file.file_name
        super().__init__()

    def compose(self) -> ComposeResult:
        yield Label(self.file_name)

    def on_mount(self) -> None:
        self.styles.border = ("solid", "#F8DE7E")
        self.styles.height = "auto"
        self.border_title = "File"
        self.styles.color = "#808080"