from textual import on
from textual.app import ComposeResult
from textual.screen import ModalScreen
from textual.widgets import Select


class ThemeSelect(ModalScreen):
    """Screen with themes selector."""

    def compose(self) -> ComposeResult:
        yield Select.from_values(
            [
                "[#F8DE7E]vegas",
                "[#0BDA51]malachite",
                "[#B026FF]neon",
                "[#FF5733]crimson",
                "[#0000ff]blue",
            ],
            prompt="Select a theme",
            id="themes_content",
        )

    @on(Select.Changed)
    def select_changed(self, event: Select.Changed) -> None:
        selected_theme = event.value
        if selected_theme == Select.BLANK:
            return
        theme_name = str(event.value).split("]")[-1]
        self.dismiss(theme_name)
