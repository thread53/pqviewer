from textual.app import ComposeResult
from textual.containers import Vertical
from textual.screen import ModalScreen
from textual.widgets import Static


class HelpScreen(ModalScreen):
    """Screen with PQViewer bindings."""

    keybinds = """Arrows: Move around the table\nPgUp:   Scroll up\nPgDn:   Scroll down\nTab:    Switch focus"""

    def compose(self) -> ComposeResult:
        with Vertical(id="help_panel"):
            yield Static(self.keybinds, id="help_content")
            yield Static("Press any key to return to table.", id="help_footer")

    def on_mount(self) -> None:
        help_panel = self.query_one("#help_panel")
        help_panel.border_title = "PQViewer key binds"

    def on_key(self) -> None:
        self.app.pop_screen()
