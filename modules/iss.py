import urllib2
import json

MODULE_NAME = "isstracker"
MODULE_AUTHOR = "Tomas Caram <tcaramm@gmail.com>"
MODULE_VERSION = 0.1

def _call_api():
    req = urllib2.Request("http://api.open-notify.org/iss-now.json")
    response = urllib2.urlopen(req)
    obj = json.loads(response.read())
    return obj

def get_iss_lat():
    """
    @Label(get_iss_lat)
    @Description(Get International Space Station's latitude position)
    @Parameters()
    @Color(#00008b)
    @Return(float)
    """

    res = _call_api()
    return float(res['iss_position']['latitude'])

def get_iss_long():
    """
    @Label(get_iss_long)
    @Description(Get International Space Station's longitude position)
    @Parameters()
    @Color(#00008b)
    @Return(float)
    """
    res = _call_api()
    return float(res['iss_position']['longitude'])