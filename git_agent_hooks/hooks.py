"""Pre-commit checks for agent code."""
import ast
import re
from typing import Tuple, List

CONFLICT_PATTERN = re.compile(r"^[<>=]{7}", re.MULTILINE)

def pre_commit_check(file_content: str, is_python: bool = True) -> Tuple[bool, List[str]]:
    errors = []
    if CONFLICT_PATTERN.search(file_content):
        errors.append("Unresolved merge conflict markers detected")

    if is_python:
        try:
            ast.parse(file_content)
        except SyntaxError as e:
            errors.append(f"Python syntax error: {e}")

    return (len(errors) == 0), errors
