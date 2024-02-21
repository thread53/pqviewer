import sys

import pytest

from pqviewer.cli import pqviewer


@pytest.fixture
def mock_format():
    sys.argv[1] = "tests/unit/assets/invalid.csv"

@pytest.fixture
def mock_path():
    sys.argv[1] = "tests/unit/assets/invalid1.csv"

@pytest.mark.usefixtures("mock_format")
def test_invalid_format():
    with pytest.raises(SystemExit): #TODO use custom exceptions and update tests
        pqviewer()

@pytest.mark.usefixtures("mock_path")
def test_non_existing():
    with pytest.raises(SystemExit):
        pqviewer()