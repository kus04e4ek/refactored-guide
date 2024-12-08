from flask import Flask, render_template, request

from city_weather import CityWeather


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('main.html')
    else:
        start = CityWeather.get_by_city_name(request.form['start_city_name'])
        end = CityWeather.get_by_city_name(request.form['end_city_name'])
        
        return render_template('answer.html', start=start, end=end,
                               result='Погода плохая'
                                      if start.check_bad_weather() or end.check_bad_weather()
                                      else 'Погода хорошая'
        )


if __name__ == '__main__':
    app.run(debug=True)
