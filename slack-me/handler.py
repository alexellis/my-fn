import sys
import json

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """

    ret = { "text": "I got a message.. length: " + str(len(req)) }

    sys.stderr.write(req)

    return json.dumps(ret)
