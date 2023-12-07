from typing import List


def input_file_readlines(path: str) -> List[str]:
    return open(path, "r").read().splitlines()
