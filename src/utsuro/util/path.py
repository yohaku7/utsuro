import os

_FILE_DIR = os.path.dirname(__file__)

TMP_PATH = os.path.join(_FILE_DIR, "..", "..", "..", "tmp")
DATA_PATH = os.path.join(_FILE_DIR, "..", "..", "..", "data")


def get_tmp(file_name: str) -> str:
    return os.path.join(TMP_PATH, file_name)


def get_data(file_name: str) -> str:
    return os.path.join(DATA_PATH, file_name)
