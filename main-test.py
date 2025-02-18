import requests


def request_weather():
    url = "http://127.0.0.1:5000/weather?zip=98121"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error - {response.status_code}-{response.text}")
        return None


weather_data = request_weather()
print(weather_data)
