import json
import urlparse

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """

    qs = urlparse.parse_qs(req)
    if "user_name" in qs:
        if not qs["user_name"][0] == "slackbot":
            ret = { "text": qs["user_name"][0] + " sent a message with a length of - " + str(len(req)) }
            return json.dumps(ret)

    return req

