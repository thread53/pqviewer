import sys
import os

from pqviewer.core.file_parser import FileParser
from pqviewer.app import PQViewer
from pqviewer.exceptions.exceptions import pretty_print_error


def pqviewer() -> None:
    """Main entry point"""

    if len(sys.argv) < 2:
        sys.exit(pretty_print_error("No file path provided."))
    file_path = sys.argv[1]
    if os.path.exists(file_path):
        try:
            parsed_file = FileParser(file_path)
        except Exception as e:
            sys.exit(pretty_print_error(e))
        app = PQViewer(parsed_file)
        app.run()
    else:
        sys.exit(
            pretty_print_error(f"The specified path does not exist.\n'{file_path}'")
        )
