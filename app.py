from flask import Flask
from flask import render_template
from flask import request
import requests
import model

# initialize flask
app = Flask(__name__)

# define routes
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

# method post allows this route to recieve data
@app.route("/results", methods = ["GET", "POST"])
def results():
  if request.method == 'GET':
    return "<h2>Please enter a city.</h2>"
  else:
    # pass the users city to the Geocode API to return the city's coordinates
    # API key 1d296f83378c674dd2db4eb7122c0364
    city = request.form["city"]
    
    coordinates = requests.get(f"https://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid=1d296f83378c674dd2db4eb7122c0364").json()

    lat = round(coordinates[0]["lat"], 2)
    lon = round(coordinates[0]["lon"], 2)

    # get weather for the next 5 days in 3 hour increments
    weather = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid=1d296f83378c674dd2db4eb7122c0364&units=imperial").json()

    # get weather data from .json for each day with every 8 3-hour increment
    temp_current = round(weather["list"][0]["main"]["temp"])
    feel_temp_current = round(weather["list"][0]["main"]["feels_like"])
    humidity_current = weather["list"][0]["main"]["humidity"]
    condition_current = weather["list"][0]["weather"][0]["description"]
    min_current = round(weather["list"][4]["main"]["temp_min"])
    max_current = round(weather["list"][0]["main"]["temp_max"])

    temp_next_day = round(weather["list"][8]["main"]["temp"])
    feel_temp_next_day = round(weather["list"][8]["main"]["feels_like"])
    humidity_next_day = weather["list"][8]["main"]["humidity"]
    condition_next_day = weather["list"][8]["weather"][0]["description"]
    min_next_day = round(weather["list"][12]["main"]["temp_min"])
    max_next_day = round(weather["list"][8]["main"]["temp_max"])

    temp_two_days = round(weather["list"][16]["main"]["temp"])
    feel_temp_two_days = round(weather["list"][16]["main"]["feels_like"])
    humidity_two_days = weather["list"][16]["main"]["humidity"]
    condition_two_days = weather["list"][16]["weather"][0]["description"]
    min_two_day = round(weather["list"][20]["main"]["temp_min"])
    max_two_day = round(weather["list"][16]["main"]["temp_max"])

    temp_three_days = round(weather["list"][24]["main"]["temp"])
    feel_temp_three_days = round(weather["list"][24]["main"]["feels_like"])
    humidity_three_days = weather["list"][24]["main"]["humidity"]
    condition_three_days = weather["list"][24]["weather"][0]["description"]
    min_three_day = round(weather["list"][28]["main"]["temp_min"])
    max_three_day = round(weather["list"][24]["main"]["temp_max"])

    storedUrl = model.getImage(temp_current)
    
    # pass variables to results html render template
    return render_template("results.html", 
                           city = city, 
                           lat = lat, 
                           lon = lon, 
                           temp_current = temp_current, 
                           temp_next_day = temp_next_day, 
                           temp_two_days = temp_two_days, 
                           temp_three_days = temp_three_days, 
                           feel_temp_current = feel_temp_current,
                           feel_temp_next_day = feel_temp_next_day,
                           feel_temp_two_days = feel_temp_two_days,
                           feel_temp_three_days = feel_temp_three_days,
                           humidity_current = humidity_current,
                           humidity_next_day = humidity_next_day,
                           humidity_two_days = humidity_two_days,
                           humidity_three_days = humidity_three_days,
                           condition_current  = condition_current,
                           condition_next_day = condition_next_day,
                           condition_two_days = condition_two_days,
                           condition_three_days = condition_three_days,
                           min_current = min_current,
                           max_current = max_current,
                           min_next_day = min_next_day,
                           max_next_day = max_next_day,
                           min_two_day = min_two_day,
                           max_two_day = max_two_day,
                           min_three_day = min_three_day,
                           max_three_day = max_three_day,
                           storedUrl = storedUrl
                          )

# debug mode enabled
app.run(host="0.0.0.0", port=81, debug=True)