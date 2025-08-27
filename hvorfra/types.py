from ast import AST
from pathlib import Path
from typing import NamedTuple

SELF = 0
PARENT = 1


class CodeLocation(NamedTuple):
    path: Path
    line: int
    column: int


type AstPath = tuple[AST, ...]
