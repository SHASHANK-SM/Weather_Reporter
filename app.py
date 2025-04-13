
from flask import Flask, jsonify, request, render_template
import requests

app = Flask(__name__)

API_KEY = "215cb2134e6f2ebbab18662c8fe78512"  # Replace this with your actual API key

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get-weather')
def get_weather():
    city = request.args.get('city')
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data['cod'] == 200:
        return jsonify({
            'city': city,
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind': data['wind']['speed']
        })
    else:
        return jsonify({'error': 'City not found'})

if __name__ == '__main__':
    app.run(debug=True)
