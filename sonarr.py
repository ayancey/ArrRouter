import requests
from pathlib import Path
import os


if os.name == "nt":
    path_mapping = {
        "***REMOVED***": "***REMOVED***"
    }
else:
    path_mapping = {
        "***REMOVED***": "***REMOVED***"
    }

# properly deal with path mapping, boring ahh

s = requests.session()

s.headers.update({
    "X-Api-Key": "***REMOVED***"
})


def get_tv_shows():
    return s.get("http://***REMOVED***:42002/api/v3/series").json()


def get_episodes(sid):
    return s.get(f"http://***REMOVED***:42002/api/v3/episodefile?seriesId={sid}").json()


def get_seasons(sid):
    return s.get(f"http://***REMOVED***:42002/api/v3/series/{sid}").json()["seasons"]
