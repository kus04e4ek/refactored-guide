import accuweather


# Класс, который хранит в себе информацию о погоде для определённого города и информацию о городе.
class CityWeather:
    # Инициализирует класс.
    def __init__(self, temperature, humidity, wind_speed, rain_probability,
                 lat=None, lon=None, city_name=None):
        self.temperature = temperature
        self.humidity = humidity
        self.wind_speed = wind_speed
        self.rain_probability = rain_probability
        
        self.lat = lat
        self.lon = lon
        self.city_name = city_name
    
    
    # Возвращает CityWeather с помощью ключа локации в AccuWeather API, kwargs передаются в конструктор CityWeather.
    def get_by_location_key(location_key, **kwargs):
        current_conditions = accuweather.get_current_conditions_by_location_key(location_key)
        daily_forecast = accuweather.get_daily_forecast_by_location_key(location_key)
        
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
        return CityWeather.get_by_location_key(location_key, lat=lat, lon=lon, **kwargs)
    
    # Возвращает CityWeather с помощью названия города, kwargs передаются в конструктор CityWeather.
    def get_by_city_name(city_name, **kwargs):
        location_key = accuweather.get_location_key_by_city_name(city_name)
        return CityWeather.get_by_location_key(location_key, city_name=city_name, **kwargs)


    # Возвращает True, если плохие погодные условия и False, если хорошие.
    def check_bad_weather(self):
        return self.temperature <= 0 or self.temperature >= 30 or \
               self.humidity <= 50 or self.humidity >= 80 or \
               self.wind_speed >= 50 or \
               self.rain_probability >= 50
    
    
    # Преобразует класс в строку, также вызывается при print.
    def __str__(self):
        header = ''
        if self.lat is not None and self.lon is not None:
            header += f'Ширина: {self.lat}, долгота: {self.lon}\n'
        if self.city_name is not None:
            header += f'Название города: {self.city_name}\n'
            
        tail = 'Погода плохая\n' if self.check_bad_weather() else 'Погода хорошая\n'
        
        return header + \
               f'Температура: {self.temperature}\n' \
               f'Влажность: {self.humidity}\n' \
               f'Скорость ветра: {self.wind_speed}\n' \
               f'Вероятность дождя: {self.rain_probability}\n' + \
               tail


if __name__ == '__main__':
    print(CityWeather.get_by_lat_lon(55.751244, 37.618423))
    print(CityWeather.get_by_lat_lon(52.2855, 104.2890))

    print(CityWeather(10, 60, 4, 0).check_bad_weather())
    print(CityWeather(-100, 60, 4, 0).check_bad_weather())
    print(CityWeather(100, 60, 4, 0).check_bad_weather())
    print(CityWeather(10, 0, 4, 0).check_bad_weather())
    print(CityWeather(10, 100, 4, 0).check_bad_weather())
    print(CityWeather(10, 60, 100, 0).check_bad_weather())
    print(CityWeather(10, 60, 4, 80).check_bad_weather())
