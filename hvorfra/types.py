from pathlib import Path
from typing import NamedTuple

SELF = 0
PARENT = 1


class CodeLocation(NamedTuple):
    path: Path
    line: int
    column: int
