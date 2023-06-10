import requests
from time import sleep
def get_ip_location(ip_address):
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)
    data = response.json()

    if data["status"] == "success":
        country = data["country"]
        city = data["city"]
        zip_code = data["zip"]
        lat = data["lat"]
        lon = data["lon"]

        print(f"IP Location Information:")
        print(f"IP Address: {ip_address}")
        sleep(0.5)
        print(f"Country: {country}")
        sleep(0.5)
        print(f"City: {city}")
        sleep(0.5)
        print(f"Zip Code: {zip_code}")
        sleep(0.5)
        print(f"Latitude: {lat}")
        sleep(0.5)
        print(f"Longitude: {lon}")
        sleep(0.5)
    else:
        print("Failed to retrieve IP location information.")

