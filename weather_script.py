import requests
import matplotlib.pyplot as plt

API_KEY = "cda11f8ec1c791c83e97f573029a51be"

def get_weather_data(city_name):
    endpoint = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(endpoint, params=params)
        if response.status_code == 200:
            weather = response.json()
            return {
                "city": city_name,
                "temperature": weather["main"]["temp"],
                "humidity": weather["main"]["humidity"],
                "pressure": weather["main"]["pressure"],
                "description": weather["weather"][0]["description"]
            }
        else:
            print(f"⚠ Couldn't retrieve data for '{city_name}'. Error code:", response.status_code)
            return None
    except Exception as e:
        print("❌ Error fetching weather data:", e)
        return None

def show_weather_report(data):
    print("\n=== Weather Report ===")
    print(f"City       : {data['city']}")
    print(f"Temperature: {data['temperature']} °C")
    print(f"Humidity   : {data['humidity']}%")
    print(f"Pressure   : {data['pressure']} hPa")
    print(f"Condition  : {data['description'].capitalize()}")

def plot_weather(data):
    categories = ["Temperature", "Humidity", "Pressure"]
    values = [data["temperature"], data["humidity"], data["pressure"]]
    colors = ["#FFA07A", "#87CEFA", "#90EE90"]

    plt.figure(figsize=(7, 4.5))
    plt.bar(categories, values, color=colors)
    plt.title(f"Weather Overview: {data['city']}")
    plt.ylabel("Values")
    plt.grid(axis="y", linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    city_input = input("Enter a city to get its weather report: ").strip()
    weather_data = get_weather_data(city_input)

    if weather_data:
        show_weather_report(weather_data)
        plot_weather(weather_data)
