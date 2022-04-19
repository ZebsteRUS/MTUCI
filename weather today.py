import requests

from weather import appid

try:
    res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                       params={'id': 524901, 'units': 'metric', 'lang': 'ru',
                               '1c918a32f2b9d695678d022868835456': appid})
    data = res.json()
    for i in data['list']:
        print(i['dt_txt'], '{0:+3.0f}'.format(i['main']['temp']), i['weather'][0]['description'])
except Exception as e:
    print("Exception (forecast):", e)
    pass
