import requests


API_KEY = 'C5RKxgzaXMi3lXAVw4etGMswPAqH93XP'


# Получает ключ локации в AccuWeather API по широте и долготе.
def get_location_key_by_lat_lon(lat, lon):
    ret = requests.get('http://dataservice.accuweather.com/locations/v1/cities/geoposition/search', 
                       params={
                           'apikey': API_KEY,
                           'q': f'{lat},{lon}'
                       })
    if ret.status_code != 200:
        print(ret.status_code, ret.content)
        return

    return ret.json()['Key']

# Получает текущую погоду по ключу локации в AccuWeather API.
def get_current_conditions_by_location_key(location_key):
    ret = requests.get(f'http://dataservice.accuweather.com/currentconditions/v1/{location_key}',
                       params={
                            'apikey': API_KEY,
                            'details': 'true'
                       })
    if ret.status_code != 200:
        print(ret.status_code, ret.content)
        return

    return ret.json()

# Получает погоду на весь день по ключу локации в AccuWeather API.
def get_daily_forecast_by_location_key(location_key):
    ret = requests.get(f'http://dataservice.accuweather.com/forecasts/v1/daily/1day/{location_key}',
                       params={
                           'apikey': API_KEY,
                           'details': 'true'
                       })
    if ret.status_code != 200:
        print(ret.status_code, ret.content)
        return

    return ret.json()
