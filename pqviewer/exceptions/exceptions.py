from rich import print
from rich.panel import Panel


def pretty_print_error(error: Exception) -> None:
    return print(
        Panel.fit(
            str(error),
            title="PQViewer encountered an error.",
            title_align="left",
            border_style="red",
            highlight=True,
        )
    )
