"""Main"""
import os
import sys
from collections import OrderedDict


def run() -> None:
    """Run main logic"""
    simplified_paths: dict[str, bool] = OrderedDict()
    if path := os.getenv("PATH"):
        for element in path.split(":"):
            if element in simplified_paths:
                continue
            simplified_paths[element] = True
    sys.stdout.write(":".join(simplified_paths.keys()))
