from textual.app import Widget, ComposeResult
from textual.widgets import Footer


class TableFooter(Widget):

    def compose(self) -> ComposeResult:
        yield Footer()

    def on_mount(self) -> None:
        self.styles.height = "1"
