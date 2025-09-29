# fake cgi module for Python 3.13+
import sys
import warnings
from typing import Any


warnings.warn(
    "Using fake 'cgi' module, "
    "because Python 3.13 removed it"
)


def parse_header(line: str) -> tuple[str, dict[Any, Any]]:
    return line, {}


sys.modules["cgi"] = sys.modules[__name__]
