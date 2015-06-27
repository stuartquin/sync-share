import os

BASE = os.path.expanduser("~/Sync")

def file_info(path, file_name):
    """
    Takes a path and file and returns a dict complete with info
    """
    full_path = path + "/" + file_name
    return {
        "is_dir": not os.path.isfile(full_path),
        "full_path": full_path,
        "name": file_name
    }

def valid_path(path):
    return path.startswith(BASE)

def load(path):
    with open(path, "r") as file:
        return file.read()

def list(path):
    if not valid_path(path):
        return []
    return [file_info(path, f) for f in os.listdir(path)]
