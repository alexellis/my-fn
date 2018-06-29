import sys
import json
import random

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
            if r["event"]["type"] == "member_joined_channel":
                if "user" in r["event"]:
                    user_name = r["event"]["user"]
                    who = "<@" + user_name + ">"
                    emoticon_list = [":openfaas:", ":whale:", ":thumbsup:", ":wave:", ":sunglasses:", ":ok_hand:", ":chart_with_upwards_trend:", ":sunrise:", ":smiley:", ":smiley_cat:", ":parrot:", ":rocket:", ":100:", ":muscle:", ":signal_strength:", ":man-cartwheeling:"]

                    emoticons = build_emoticons(emoticon_list)

                    msg = {"text": "Let's all welcome {} to the community! {} ".format(who, emoticons.strip())}

                    out_req = requests.post(webhook_url, json=msg)
                    # print(str(out_req.status_code), out_req.text)

def build_emoticons(emoticon_list):
    emoticons = ""
    sample = random.sample(emoticon_list, 5)
    for em in sample:
        emoticons = emoticons + em + " "

    return emoticons