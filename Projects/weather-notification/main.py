import requests
from win10toast import ToastNotifier
from plyer import notification


API_KEY = "0103509458a11b4954f5bc62903403cd"
CITY = "Belgrade"

def get_weather_data(key, city):
    API_URL = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric"
    weather_response = requests.get(API_URL)
    weather_data = weather_response.json()

    data_info = {}

    # min_temp = weather_data["main"]["temp_min"]
    # max_temp = weather_data["main"]["temp_max"]
    data_info["city"] = weather_data["name"]
    data_info["current_temp"] = weather_data["main"]["temp"]
    data_info["description"] = weather_data["weather"][1]["description"]
    data_info["humidity"]  = weather_data["main"]["humidity"]
    return data_info


def parse_weather_data(city,current_temp, description, humidity):
    message = f"Weather in {city}:\n"
    message += f"Temperature: {current_temp}°C\n"
    message += f"Condition: {description}\n"
    message += f"Humidity: {humidity}%"

    return  message


# def send_notification(message):
#     toaster = ToastNotifier()
#     toaster.show_toast("Weather notification",message, duration=10)

def send_notification(message):
    notification.notify(
        title="Weather Update",
        message=message,
        timeout=10
    )


def main():
    weather_data = get_weather_data(API_KEY,CITY)
    message = parse_weather_data(weather_data["city"],weather_data["current_temp"],weather_data["description"],weather_data["humidity"])
    send_notification(message)

main()


#wind10toast izbacuje neki error (tip podataka je u pitanju)