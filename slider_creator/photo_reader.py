from exif import Image
import folium
from folium.plugins import MarkerCluster
from folium.plugins import MarkerCluster
import pandas as pd


outputfile = 'photo_reader_output/test.txt'
folder_path = 'photos'
img_filename = 'CI-mg108283-before.jpg'
img_path = f'{folder_path}/{img_filename}'
popup_data = 'mg108283'

def dms_to_dd(d, m, s):
    dd = d + float(m)/60 + float(s)/3600
    return dd

with open(img_path, 'rb') as img_file:
    img = Image(img_file)

list = sorted(img.list_all())
#liststring = '/n'.join(map(str,list))


#with open(outputfile, 'w' ) as f: 
 #   f.write(liststring)
print(list)
xcoord = img.get("gps_latitude")
xcoordref = img.get("gps_latitude_ref")
ycoord = img.get("gps_longitude")
ycoordref = img.get("gps_longitude_ref")
datetime = img.get("datetime")

print(xcoord)

ddx = dms_to_dd(xcoord[0], xcoord[1], xcoord[2])
ddy = dms_to_dd(ycoord[0], ycoord[1], ycoord[2])

print(ycoordref)

if xcoordref == "S":
    x = "-"+ str(ddx[0])
    x = float(x)
else:
    x = ddx

if ycoordref == "W":
    y = "-"+ str(ddy)
    y = float(y)
   
else:
    y = ddy


print(x,xcoordref, " , " ,y, ycoordref, datetime)

photo_coords = [x, y]
print(photo_coords)

map = folium.Map(
    location = photo_coords, 
    zoom_start=15,
    tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
    attr='Esri')

folium.Marker(
    photo_coords, 
    popup = popup_data, 
    tooltip='click').add_to(map)


map.save('photo_reader_output/map_test.html')
map