from textual.app import App, ComposeResult
from textual.containers import Horizontal

from pqviewer.table_header import TableHeader
from pqviewer.table_schema import TableSchema
from pqviewer.table_content import TableContent


class PQViewer(App):

    CSS_PATH = "global.tcss"

    def __init__(self, parsed_file):
        self.parsed_file = parsed_file
        super().__init__()

    def compose(self) -> ComposeResult:
        yield TableHeader(self.parsed_file)
        with Horizontal():
            yield TableSchema(self.parsed_file)
            yield TableContent(self.parsed_file)
