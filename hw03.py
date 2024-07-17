from colorama import Fore, Back, Style
from pathlib import Path
import sys

def write_paths(path, nesting_level=0):
    result = ""
    if path.is_file():
        result += Fore.GREEN + "\t" * nesting_level + path.name + "\n"
    else:
        result += Fore.BLUE + "\t" * nesting_level + path.name + "/" + "\n"
        for child in path.iterdir():
            result += write_paths(child, nesting_level=nesting_level + 1)

    return result


def hw03():
    _, path_arg = sys.argv

    path = Path(path_arg)

    if not path.exists():
        print("Path error")
        return

    result = write_paths(path)

    print(result)


hw03()
