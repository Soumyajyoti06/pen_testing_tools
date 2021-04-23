# Import module
import pyfiglet
from geopy.geocoders import Nominatim

ascii_banner = pyfiglet.figlet_format("GEO LOCATION FINDER")
print(ascii_banner)

# Initialize Nominatim API
geolocator = Nominatim(user_agent="geoapiExercises")

# Assign Latitude & Longitude
Latitude = input("Enter the Latitude: ")
Longitude = input("Enter the Longitude: ")

# Dsiaplying Latitude and Longitude
print("Latitude: ", Latitude)
print("Longitude: ", Longitude)

# Get location with geocode
location = geolocator.geocode(Latitude+","+Longitude)

# Dsiplay location
print("\nLocation of the given Latitude and Longitude:")
print(location)
