import sys
import os

from pqviewer.file_parser import FileParser
from pqviewer.app import PQViewer
from pqviewer.exceptions import pretty_print_error

def pqviewer():
    """ Main entry point"""

    file_name = sys.argv[1]
    if os.path.exists(file_name):
        try:
            parsed_file = FileParser(file_name)
        except Exception as e:
            sys.exit(pretty_print_error(e))
        
        app = PQViewer(parsed_file)
        app.run()
    else:
        sys.exit(pretty_print_error("Path does not exist"))
    

