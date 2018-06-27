import json
import sys


def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """

    sys.stderr.write(req)

    r = json.laods(req)

    if "challenge" in r:
        return challenge(r)

    

def callenge(r):
    if r["type"] == "url_verification":
        res = {"challenge": r["challenge"]}
        return json.dumps(res)

