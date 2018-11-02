for any given location.
import requests 

link = "http://api.openweathermap.org/data/2.5/forecast"
lat = float(input("Enter the latitude coordinates "))
lon = float(input("Enter the longitude coordinates "))            
additional_data = {
    "APPID" : "b049ad700500b231d3ccf3d662711691",
    "lat": lat,
    "lon" : lon
}

data = requests.get(link,params=additional_data).json()
print(data["city"]["name"])
print(data)
