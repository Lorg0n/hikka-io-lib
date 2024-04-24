import requests


HIKKA_URL_BASE = "https://api.hikka.io"


def request(url, method="GET", **kwargs):
    try:
        if method == "GET":
            r = requests.get(url, **kwargs)
        elif method == "POST":
            r = requests.post(url, **kwargs)
        else:
            raise ValueError(f"Invalid request method: {method}")
        r.raise_for_status()
        result_json = r.json()
        return result_json
    except requests.RequestException as e:
        raise Exception(f"Error executing the request: {e}")