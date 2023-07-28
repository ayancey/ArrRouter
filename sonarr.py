import requests
from pathlib import Path
import os


if os.name == "nt":
    path_mapping = {
        "***REMOVED***/TV Shows": "***REMOVED***"
    }
else:
    path_mapping = {
        # "***REMOVED***": "***REMOVED***",
        # "***REMOVED***": "***REMOVED***",
        # "***REMOVED***": "***REMOVED******REMOVED***"
    }

# properly deal with path mapping, boring ahh

s = requests.session()

s.headers.update({
    "X-Api-Key": "***REMOVED***"
})


def get_tv_shows():
    return s.get("http://***REMOVED***:42002/api/v3/series").json()


def get_episodes(sid):
    return s.get(f"http://***REMOVED***:42002/api/v3/episode?seriesId={sid}").json()


def get_seasons(sid):
    return s.get(f"http://***REMOVED***:42002/api/v3/series/{sid}").json()["seasons"]


def return_path_fixed(eid):
    r = s.get(f"http://***REMOVED***:42002/api/v3/episode/{eid}")
    mapped_path = r.json()["episodeFile"]["path"]

    for path in path_mapping:
        mapped_path = mapped_path.replace(path, path_mapping[path])

    return mapped_path
