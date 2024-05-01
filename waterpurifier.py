import requests
import time

def check_water_quality(api_key, channel_id):
    thingspeak_url = f"https://api.thingspeak.com/channels/{channel_id}/fields/4/last.json?api_key={api_key}"

    try:
        response = requests.get(thingspeak_url)
        if response.status_code == 200:
            data = response.json()
            water_cleanliness_status = data["field4"]

            if water_cleanliness_status == 1:
                print("Water is drinkable.")
            else:
                print("Water is not drinkable. Initiating filtration process.")
                filter_water()
        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error retrieving data from ThingSpeak: {e}")

def filter_water():
    # Simulate a water filtration process
    print("Filtering water...")
    # You would typically implement a real water filtration process here

if __name__ == "__main__":
    # Replace 'YOUR_API_KEY' and 'YOUR_CHANNEL_ID' with your ThingSpeak API key and channel ID
    api_key = 'H97R1W77Y2W0H595'
    channel_id = '2377009'

    while True:
        check_water_quality(api_key, channel_id)
        time.sleep(20)  # Check water quality every 10 seconds
