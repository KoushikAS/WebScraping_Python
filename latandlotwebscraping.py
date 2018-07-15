from geopy.geocoders import  Nominatim
import time
import json


geolocator=Nominatim()
list=["kudremukh","dubare","gokarn","mangalore","belgaum","k-gudi","bellary","udupi","jog-falls","raichur","hampi","bandipur","channarayapatna","siddapur","hassan","shravanabelagola","nagarhole","shimoga","manipal","bijapur","chikmagalur","chitradurga","tumkur","madikeri","uttara-kannada","halebid","dharwad","gulbarga","hubli","coorg","badami","bidar","ganeshgudi","bangalore","karwar","mysore","dharmasthala","bhagamandala","dandeli","bheemeshwari","nandi-hills","belur"]
data={}
count=0
print(geolocator.geocode("mysore",timeout=10).longitude)

try:
    for place in list:
        print(place)
        location=geolocator.geocode(place ,timeout=10)
        data[place]={}
        data[place]['lat']=location.latitude
        data[place]['lon'] = location.longitude
        count+=1

except:
    pass
print(count)
print(data['mysore'])

with open("lat_lon_place.json","w") as outfile:
    json.dump(data,outfile)
print("finish")