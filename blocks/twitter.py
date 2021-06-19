from requests_oauthlib import OAuth1
import requests

MODULE_NAME = "twitter"
MODULE_AUTHOR = "Tomas Caram <tcaramm@gmail.com>"
MODULE_VERSION = 0.1


def _make_request(text):
    APP_KEY = "uJjauAXgUwWQ6YuqPAUNRr8g7"
    APP_SECRET = "hXBi8cBmzOfV0S9pNfF4gmkbtuxFbAPKsJYdijQkniQeh3TNxl"
    CONSUMER_SECRET = "496011507-A8L54fj1jqDRstGav4Ks1wHwFzqujny5ikiMFnTW"
    TOKEN_SECRET = "50sFxDFfpRvASa5oZRnvd4COEVSinh5c29y1PH8fLc3i0"

    auth = OAuth1(APP_KEY, APP_SECRET, CONSUMER_SECRET, TOKEN_SECRET)
    params = {"status": text}

    r = requests.post(
        "https://api.twitter.com/1.1/statuses/update.json", auth=auth, params=params
    )

    return r

def send_tweet(text):
    """
    @Label(send_tweet   )
    @Description(Sends tweet)
    @Parameters(string text)
    @Example(Hola mundo)
    @Color(#00acee)
    """

    r = _make_request(text)
    return r.status_code == 200