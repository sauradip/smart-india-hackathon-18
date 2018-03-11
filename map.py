import gmplot
from geopy.geocoders import Nominatim


# this code is used to locate the region in map and generate coordinates which will be used to find regional language 

geolocator = Nominatim()
location = geolocator.geocode("KanKani")

print((location.latitude, location.longitude))



pathlat = (location.latitude),(location.latitude)
pathlon = (location.longitude),(location.longitude)
#pathlat = (26.29),(26.29)
#pathlon = (73.02),(73.02)

gmap = gmplot.GoogleMapPlotter(pathlat[0],pathlon[0],18)

gmap.plot(pathlat,pathlon,'cornflowerblue', edge_width=10)

gmap.draw('map.html')
