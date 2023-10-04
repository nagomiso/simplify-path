"""Main"""
from collections import OrderedDict
import os

def run():
    """Run main logic"""
    simplified_paths: dict[str, bool] = OrderedDict()
    if path := os.getenv("PATH"):
        for element in path.split(":"):
            if element in simplified_paths:
                continue
            simplified_paths[element] = True
    print(":".join(simplified_paths.keys()))
