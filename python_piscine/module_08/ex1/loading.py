#!/usr/bin/env python3

# import pandas as pd
# import requests
# import matplotlib as mpl
from typing import Any, Optional

def ft_imports(pack_name: str) -> Optional[Any | None]:

    try:
        module = __import__(pack_name)
        print(type(module))
        print(f"[OK] {type(module)}")
        return module
    except ImportError:
        print(f"[ERROR] - '{pack_name}' Module not found!!")
        return None




if __name__ == "__main__":
    pack_names = ['pandas', 'requests', 'matplotlib']
    for pack in pack_names:
        ft_imports(pack)
