"""Generate a detailed coverage JSON from a coverage data file.

The output JSON contains, for each file covered:
- path: absolute or relative file path
- source: the file source as a single string
- executed_lines: list of executed line numbers
- functions: list of { name, lineno, end_lineno, executed }

This helper reads coverage data using coverage.Coverage and writes a JSON
file suitable for analysis after Playwright tests run.
"""
import json
import ast
from typing import List, Dict
from coverage import Coverage


def _get_functions(source: str) -> List[Dict]:
    tree = ast.parse(source)
    funcs = []

    class FuncVisitor(ast.NodeVisitor):
        def visit_FunctionDef(self, node: ast.FunctionDef):
            # Python 3.8+ has end_lineno; if missing, we attempt to estimate
            funcs.append({
                "name": node.name,
                "lineno": node.lineno,
                "end_lineno": getattr(node, "end_lineno", node.lineno),
            })
            self.generic_visit(node)

        def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef):
            funcs.append({
                "name": node.name,
                "lineno": node.lineno,
                "end_lineno": getattr(node, "end_lineno", node.lineno),
            })
            self.generic_visit(node)

    FuncVisitor().visit(tree)
    return funcs


def generate_detailed_json(data_file: str = ".coverage", out_file: str = "coverage-playwright.json"):
    cov = Coverage(data_file=data_file)
    cov.load()
    data = cov.get_data()

    result = {}
    for filename in sorted(data.measured_files()):
        try:
            with open(filename, "r", encoding="utf8") as f:
                src = f.read()
        except Exception:
            continue
        executed = sorted(list(data.lines(filename) or []))
        funcs = _get_functions(src)
        # annotate whether function had any executed line
        for fn in funcs:
            fn_lines = set(range(fn["lineno"], fn["end_lineno"] + 1))
            fn["executed"] = len(fn_lines.intersection(set(executed))) > 0

        result[filename] = {
            "path": filename,
            "source": src,
            "executed_lines": executed,
            "functions": funcs,
        }

    with open(out_file, "w", encoding="utf8") as out:
        json.dump(result, out, indent=2)


if __name__ == "__main__":
    generate_detailed_json()
