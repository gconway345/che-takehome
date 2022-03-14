from pyowm import OWM
import sys
import os

sl_locations = [
    "Atlanta,US",
    "London,UK",
    "New York,US",
    "Guadalajara,MX",
    "Indianapolis,US",
    "San Francisco,US",
]


def main():
    # standup connection to OWM
    owm = OWM(apikey_get())
    mgr = owm.weather_manager()
    for location in sl_locations:
        print(location)
        observation = mgr.weather_at_place(location)
        w = observation.weather
        print(f"Current weather is: {w.detailed_status}")
        wind = w.wind()["speed"]
        print(f"Wind speed is {wind} MPH")
        print(f"Humidity is {w.humidity}%")
        temp = w.temperature("fahrenheit")["temp"]
        print(f"Temperature is {temp} F")
        print("-------------")


def apikey_get():
    # if system arguments provided, use that as the API key.
    if len(sys.argv) >= 2:
        apikey = sys.argv[1]
    else:
        # Assume the api key is in the ENV if not argument
        apikey = os.getenv("API_KEY")
    try:
        # test to see if the key is present, if not then not provided at all and end program
        len(apikey) > 1
    except:
        sys.exit("No API key provided, please add to ENV or provide as an argument")
    return apikey


if __name__ == "__main__":
    main()
