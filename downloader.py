import requests
from pathlib import Path
from urllib.parse import urlparse, unquote
from os.path import splitext, basename


def download_pic(url, path):
    response = requests.get(url)
    response.raise_for_status()
    Path(path).mkdir(exist_ok=True)
    parsed_url = urlparse(url)
    name = unquote(basename(parsed_url.path))
    with open(f"{path}/{name}", 'wb') as picture:
        picture.write(response.content)


def get_file_format(url):
    parsed_url = urlparse(url)
    name = unquote(basename(parsed_url.path))
    name_format_tuple = splitext(name)
    if name_format_tuple[1]:
        return name_format_tuple[1]
    return name_format_tuple[0]
