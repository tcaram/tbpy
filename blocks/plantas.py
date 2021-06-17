from gettext import gettext as _
import urllib
import json

MODULE_NAME = "weather"
MODULE_AUTHOR = "Tomas Caram <tcaramm@gmail.com>"
MODULE_PARAMS = [float, float]
MODULE_PARAMS_DEFAULT = [-34.921, -56.159]

def __call_api(lat, lon):
	API_KEY = "d62fa22e64580ff65cc374ca8e791be3"
	lang = "es"

	url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&lang=%s&units=metric&exclude=hourly,daily,minutely&appid=%s" % (lat, lon, lang, API_KEY)

	request = urllib.urlopen(url)
	data = json.load(request)
	return data;


def reconocer_planta(imagen):
	"""
		@Label(reconocer_planta)
		@Description(Reconocer planta con imagen)
		@Params(str imagen)
		@Example()
	"""
	return