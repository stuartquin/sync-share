import os
import mimetypes

BASE = os.path.expanduser("~/Sync")
IMAGES = ["png", "jpg", "jpeg", "gif"]

LANGUAGES = {
    "php": "php",
    "py": "python",
    "go": "go",
    "c": "c",
    "java": "java",
    "md": "markdown",
    "markdown": "markdown",
    "sql": "sql",
    "css": "css",
    "sh": "bash",
    "xml": "markup",
    "html": "markup",
    "js": "javascript",
    "rb": "ruby"
}

def get_ext(path):
    split = os.path.splitext(path)
    return split[1].strip(".")


def is_image(file_name):
    split = os.path.splitext(file_name)
    return split[1].strip(".") in IMAGES

def file_info(path, file_name):
    """
    Takes a path and file and returns a dict complete with info
    """
    full_path = path + "/" + file_name
    return {
        "is_dir": not os.path.isfile(full_path),
        "is_image": is_image(file_name),
        "full_path": full_path,
        "name": file_name
    }

def valid_path(path):
    return path.startswith(BASE)

def get_language(path):
    ext = get_ext(path)
    if ext in LANGUAGES:
        return LANGUAGES[ext]

    type = mimetypes.guess_type(path)
    if type[0] and type[0].startswith("text"):
        return "txt"

def load(path):
    lang = get_language(path)
    if lang:
        with open(path, "r") as file:
            return {"content": file.read(), "lang": lang, "path": path}

def list(path):
    if not valid_path(path):
        return []
    return [file_info(path, f) for f in os.listdir(path)]
