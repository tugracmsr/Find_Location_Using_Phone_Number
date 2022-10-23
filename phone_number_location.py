import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
import folium
import os


if os.path.exists("mylocation.html"):
  os.remove("mylocation.html")
try:
    number = input("Enter Phone Number:")

    location = geocoder.description_for_number(phonenumbers.parse(number),"en")
    print(location)

    print(carrier.name_for_number(phonenumbers.parse(number), "en"))

    key = '' #https://opencagedata.com/dashboard#geocoding, enter your API Key here.
    geocoder = OpenCageGeocode(key)
    query = str(location)
    results = geocoder.geocode(query)
    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']
    print(lat,lng)

    myMap = folium.Map(location=[lat , lng], zoom_start=9)
    folium.Marker([lat,lng],popup=location).add_to(myMap)
    myMap.save("mylocation.html")
    os.system("mylocation.html")
except:
    print("Missing or invalid number\nPlease enter your phone number with country code")
