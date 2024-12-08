import accuweather


# Класс, который хранит в себе информацию о погоде для определённого города и информацию о городе.
class CityWeather:
    # Инициализирует класс.
    def __init__(self, temperature, humidity, wind_speed, rain_probability,
                 lat=None, lon=None):
        self.temperature = temperature
        self.humidity = humidity
        self.wind_speed = wind_speed
        self.rain_probability = rain_probability
        
        self.lat = lat
        self.lon = lon
    
    
    # Возвращает CityWeather с помощью ключа локации в AccuWeather API, kwargs передаются в конструктор CityWeather.
    def get_by_location_key(location_key, **kwargs):
        current_conditions = accuweather.get_current_conditions_by_location_key(location_key)
        daily_forecast = accuweather.get_daily_forecast_by_location_key(location_key)
        if (current_conditions is None) or (daily_forecast is None):
            return
        
        return CityWeather(
            current_conditions[0]['Temperature']['Metric']['Value'],
            current_conditions[0]['RelativeHumidity'],
            current_conditions[0]['Wind']['Speed']['Metric']['Value'],
            daily_forecast['DailyForecasts'][0]['Day']['RainProbability'],
            **kwargs
        )
    
    # Возвращает CityWeather с помощью широту и долготы, kwargs передаются в конструктор CityWeather.
    def get_by_lat_lon(lat, lon, **kwargs):
        location_key = accuweather.get_location_key_by_lat_lon(lat, lon)
        if location_key is None:
            return
        
        return CityWeather.get_by_location_key(location_key, lat=lat, lon=lon, **kwargs)
    
    
    # Преобразует класс в строку, также вызывается при print.
    def __str__(self):
        if self.lat is not None and self.lon is not None:
            header = f'Ширина: {self.lat}, долгота: {self.lon}\n'
        else:
            header = ''
        
        return header + \
               f'Температура: {self.temperature}\n' \
               f'Влажность: {self.humidity}\n' \
               f'Скорость ветра: {self.wind_speed}\n' \
               f'Вероятность дождя: {self.rain_probability}\n'


if __name__ == '__main__':
    print(CityWeather.get_by_lat_lon(55.751244, 37.618423))
    print(CityWeather.get_by_lat_lon(52.2855, 104.2890))
