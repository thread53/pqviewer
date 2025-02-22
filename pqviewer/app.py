from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.binding import Binding
from textual.reactive import var

from pqviewer.views.table_header import TableHeader
from pqviewer.views.table_schema import TableSchema
from pqviewer.views.table_content import TableContent
from pqviewer.views.table_footer import TableFooter
from pqviewer.views.help_screen import HelpScreen
from pqviewer.views.themes_screen import ThemeSelect


THEMES = {
    "vegas": "#F8DE7E",
    "malachite": "#0BDA51",
    "neon": "#B026FF",
    "crimson": "#FF5733",
    "blue": "#0000ff",
}


class PQViewer(App):

    CSS_PATH = "global.tcss"
    BINDINGS = [
        Binding("ctrl+c", "quit", "Quit"),
        Binding("t", "themes_screen", "Themes"),
        Binding("h", "help_screen", "Help")
    ]
    theme = var("vegas")

    def __init__(self, parsed_file) -> None:
        self.parsed_file = parsed_file
        super().__init__()

    def compose(self) -> ComposeResult:
        yield TableHeader(self.parsed_file, id="table_header")
        with Horizontal():
            yield TableSchema(self.parsed_file)
            yield TableContent(self.parsed_file)
        yield TableFooter()

    def watch_theme(self):
        color_hex = THEMES[self.theme]
        table_header = self.query_one("#table_header")
        table_header.styles.border = ("heavy", color_hex)

        datatable_schema = self.query_one("#datatable_schema")
        datatable_schema.styles.border = ("heavy", color_hex)
        datatable_schema.styles.scrollbar_color = color_hex
        datatable_schema.styles.scrollbar_color_active = color_hex
        datatable_schema.styles.scrollbar_color_hover = color_hex
        datatable_schema.border_title = "Schema"
        datatable_schema.border_subtitle = f"Total columns: {self.parsed_file.number_columns()}"

        datatable_content = self.query_one("#datatable_content")
        datatable_content.styles.border = ("heavy", color_hex)
        datatable_content.styles.scrollbar_color = color_hex
        datatable_content.styles.scrollbar_color_active = color_hex
        datatable_content.styles.scrollbar_color_hover = color_hex
        datatable_content.border_title = "Table"
        datatable_content.border_subtitle = f"Total rows: {self.parsed_file.number_rows()}"

    def action_help_screen(self) -> None:
        """Action to display the help screen dialog."""
        self.push_screen(HelpScreen())

    def action_themes_screen(self):
        self.push_screen(ThemeSelect(), callback=self.modal_callback_to_exit)

    def modal_callback_to_exit(self, selected_theme):
        self.theme = selected_theme
