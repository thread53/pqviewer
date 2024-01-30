from rich import print
from rich.panel import Panel


class PQViewerError(Exception):
    def __init__(self, msg, title):
        super().__init__(msg)
        self.msg = msg
        self.title = title


class PQViewerFileTypeError(PQViewerError):
    """Invalid file type."""

    pass


class PQViewerFilePathError(PQViewerError):
    """Invalid file path."""

    pass


def pretty_print_error(error: PQViewerError) -> None:
    return print(
        Panel.fit(
        str(error),
        title="PQViewer encountered an error.",
        title_align="left",
        border_style="red",
        highlight=True,
        )
    )
