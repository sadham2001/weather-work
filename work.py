import requests

API_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"


def get_weather_data():
    response = requests.get(API_URL)
    return response.json()


def get_temperature_by_date(data, target_date):
    for entry in data["list"]:
        if target_date in entry["dt_txt"]:
            return entry["main"]["temp"]
    return None


def get_wind_speed_by_date(data, target_date):
    for entry in data["list"]:
        if target_date in entry["dt_txt"]:
            return entry["wind"]["speed"]
    return None


def get_pressure_by_date(data, target_date):
    for entry in data["list"]:
        if target_date in entry["dt_txt"]:
            return entry["main"]["pressure"]
    return None


def main():
    data = get_weather_data()

    while True:
        print("\nMenu:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            target_date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
            temperature = get_temperature_by_date(data, target_date)
            if temperature is not None:
                print(f"Temperature on {target_date}: {temperature} K")
            else:
                print("Data not found for the given date.")

        elif choice == 2:
            target_date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
            wind_speed = get_wind_speed_by_date(data, target_date)
            if wind_speed is not None:
                print(f"Wind Speed on {target_date}: {wind_speed} m/s")
            else:
                print("Data not found for the given date.")

        elif choice == 3:
            target_date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
            pressure = get_pressure_by_date(data, target_date)
            if pressure is not None:
                print(f"Pressure on {target_date}: {pressure} hPa")
            else:
                print("Data not found for the given date.")

        elif choice == 0:
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
