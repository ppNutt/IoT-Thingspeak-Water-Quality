import random
import time
import requests

class RainwaterHarvestingSystem:
    def __init__(self, api_key, channel_id, tank_capacity):
        self.api_key = api_key
        self.channel_id = channel_id
        self.tank_capacity = tank_capacity
        self.rain_sensor_data = 0
        self.water_tank_level = 0

    def simulate_rainfall(self):
        # Simulate rainfall and update rain sensor data
        self.rain_sensor_data = random.uniform(0, 10)

    def collect_rainwater(self):
        # Simulate collecting rainwater and update water tank level
        self.water_tank_level += self.rain_sensor_data
        print(f"Rainwater collected: {self.rain_sensor_data} liters")
        print(f"Water tank level: {self.water_tank_level} liters")

        # Send data to ThingSpeak
        self.send_to_thingspeak()

        # Check if the water tank is full
        if self.water_tank_level >= self.tank_capacity:
            print("Water tank is full. Stopping the simulation.")
            return True

    def send_to_thingspeak(self):
        url = f"https://api.thingspeak.com/update?api_key={self.api_key}&field1={self.rain_sensor_data}&field2={self.water_tank_level}"

        try:
            response = requests.get(url)
            if response.status_code == 200:
                print("Data sent to ThingSpeak successfully.")
            else:
                print(f"Failed to send data to ThingSpeak. Status Code: {response.status_code}")
        except Exception as e:
            print(f"Error sending data to ThingSpeak: {e}")

def main():
    # Replace 'YOUR_API_KEY' and 'YOUR_CHANNEL_ID' with your ThingSpeak API key and channel ID
    api_key = '4I2BAXOVGHFI6US1'
    channel_id = '2379543'
    tank_capacity = 4580  

    rainwater_system = RainwaterHarvestingSystem(api_key, channel_id, tank_capacity)

    while True:
        rainwater_system.simulate_rainfall()
        if rainwater_system.collect_rainwater():
            break 
        time.sleep(10) 

if __name__ == "__main__":
    main()
