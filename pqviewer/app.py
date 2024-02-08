from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.binding import Binding

from pqviewer.table_header import TableHeader
from pqviewer.table_schema import TableSchema
from pqviewer.table_content import TableContent
from pqviewer.table_footer import TableFooter
from pqviewer.help_screen import HelpScreen


class PQViewer(App):

    CSS_PATH = "global.tcss"
    BINDINGS = [Binding("ctrl+c", "quit", "Quit"), Binding("h", "help_screen", "Help")]

    def __init__(self, parsed_file) -> None:
        self.parsed_file = parsed_file
        super().__init__()

    def compose(self) -> ComposeResult:
        yield TableHeader(self.parsed_file)
        with Horizontal():
            yield TableSchema(self.parsed_file)
            yield TableContent(self.parsed_file)
        yield TableFooter()

    def action_help_screen(self) -> None:
        """Action to display the help screen dialog."""
        self.push_screen(HelpScreen())
