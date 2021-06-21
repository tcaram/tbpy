import urllib
import json

MODULE_NAME = "weather"
MODULE_AUTHOR = "Tomas Caram <tcaramm@gmail.com>"
MODULE_VERSION = 0.1


def __call_api(lat, lon):
    API_KEY = "d62fa22e64580ff65cc374ca8e791be3"
    lang = "es"

    url = (
        "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&lang=%s&units=metric&exclude=hourly,daily,minutely&appid=%s"
        % (lat, lon, lang, API_KEY)
    )

    request = urllib.urlopen(url)
    data = json.load(request)
    return data


def get_temperature(lat, lon):
    """
    @Label(get_temperature)
    @Description(Get temperature in a given location)
    @Parameters(float lat, float lon)
    @Example(-34.921, -56.159)
    @Color(#ff0000)
    @Return(float)
    """
    res = __call_api(lat, lon)
    return res["current"]["temp"]


def get_weather(lat, lon):
    """
    @Label(get_weather)
    @Description(Get weather in a given location)
    @Parameters(float lat, float lon)
    @Example(-34.921, -56.159)
    @Color(#ff0000)
    @Return(string)
    """
    res = __call_api(lat, lon)
    cweather = res["current"]["weather"][0]
    return cweather["main"] + ", " + cweather["description"]
