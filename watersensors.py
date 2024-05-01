import time
import requests
import random

def generate_water_quality_data():
    # Simulate rainwater parameters
    rainwater_temperature = random.uniform(10, 20)
    rainwater_ph = random.uniform(6, 8)
    rainwater_dissolved_oxygen = random.uniform(5, 9)

    # Update parameters based on the average of rainwater
    temperature = rainwater_temperature
    ph = rainwater_ph
    dissolved_oxygen = rainwater_dissolved_oxygen

    return {
        "api_key": "S4XXUIDXL8B444K6",
        "field1": temperature,
        "field2": ph,
        "field3": dissolved_oxygen,
        "field4": 0  # Placeholder for water cleanliness status (0: Unclean, 1: Clean)
    }

def is_water_clean(data):
    # Adjust threshold values for drinkable water quality
    ph_threshold = 6.8
    dissolved_oxygen_threshold = 6.5

    return data["field2"] > ph_threshold and data["field3"] > dissolved_oxygen_threshold

def update_water_cleanliness_status(data):
    return 1 if is_water_clean(data) else 0

while True:
    data = generate_water_quality_data()
    data["field4"] = update_water_cleanliness_status(data)

    thingspeak_url = "https://api.thingspeak.com/update"

    try:
        response = requests.post(thingspeak_url, params=data)
        if response.status_code == 200:
            print(f"Data sent successfully: {data}")
            if is_water_clean(data):
                print("Clean water detected")
            else:
                print("Water quality unclean")
        else:
            print(f"Failed to send data. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error sending data to ThingSpeak: {e}")

    time.sleep(10)  # Sleep for 10 seconds between iterations
    