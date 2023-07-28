import requests
from pathlib import Path
import os


if os.name == "nt":
    path_mapping = {
        "***REMOVED***": "***REMOVED***"
    }
else:
    path_mapping = {
        # "***REMOVED***": "***REMOVED***",
        # "***REMOVED***": "***REMOVED******REMOVED***",
        # "***REMOVED***": "***REMOVED******REMOVED***"
    }

# properly deal with path mapping, boring ahh

s = requests.session()

s.headers.update({
    "Authorization": "Bearer ***REMOVED***"
})


def get_movies():
    return s.get(f"http://***REMOVED***:7878/api/v3/movie").json()


def return_path_fixed(mid):
    r = s.get(f"http://***REMOVED***:7878/api/v3/movie/{mid}")
    mapped_path = r.json()["movieFile"]["path"]

    for path in path_mapping:
        mapped_path = mapped_path.replace(path, path_mapping[path])

    return mapped_path
