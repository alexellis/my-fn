import sys
import json

import requests

def challenge(r):
    if r["type"] == "url_verification":
        res = {"challenge": r["challenge"]}
        return json.dumps(res)

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """

    sys.stderr.write(req)

    r = json.loads(req)

    if "challenge" in r:
        return challenge(r)

    with open("/var/openfaas/secrets/incoming-webhook-url") as webhook_url_text:
        webhook_url = webhook_url_text.read().strip()
        if "event" in r:
            if r["event"] == "member_joined_channel":
                if "user" in r["event"]:
                    user_name = r["event"]["user"]
                    msg = {"text": "Welcome to " + user_name + "! :openfaas:"}

                    out_req = requests.post(webhook_url, json=msg)
                    # print(str(out_req.status_code), out_req.text)
