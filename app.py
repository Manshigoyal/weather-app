from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "60bf2a73608246c09ecfdebb3bd5f064"

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None

    if request.method == "POST":
        city = request.form["city"]

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(url)
        data = response.json()

        if data["cod"] == 200:
            weather = {
    "city": city,
    "temp": data["main"]["temp"],
    "desc": data["weather"][0]["description"],
    "humidity": data["main"]["humidity"],
    "icon": f"http://openweathermap.org/img/wn/{data['weather'][0]['icon']}@2x.png",
    "main": data["weather"][0]["main"] 
}
        else:
            weather = {"error": "City not found"}

    return render_template("index.html", weather=weather)

if __name__ == "__main__":
    app.run()

