from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "221100ab3d0093f7fe086467bfec77f7"
WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.route('/weather', methods=['GET'])
def get_weather():
    zip_code = request.args.get("zip")
    print(f"Request received for {zip_code}")
    if not zip_code:
      return jsonify({"error": "Missing zip code"}), 400
    try:
        response = requests.get(WEATHER_API_URL, params={
            "zip": zip_code,
            "appid": API_KEY,
            "units": "imperial"
        })

        data = response.json()

        weather_data = {
            "zip": zip_code,
            "city": data.get("name", "Unknown"),
            "temperature": f"{data.get('main', {}).get('temp', 'N/A')} F",
            "feels_like": f"{data.get('main', {}).get('feels_like', 'N/A')} F"
        }

        return jsonify(weather_data)

    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Failed to fetch weather data", "details": str(e)}), 500


if __name__ == '__main__':
    app.run()
