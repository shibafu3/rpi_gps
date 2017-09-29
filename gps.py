#!/usr/bin/python3

import pyproj
from gps3 import gps3

ofs = open('coor.txt', 'a+')
EPSG4612 = pyproj.Proj("+init=EPSG:4612")
EPSG2451 = pyproj.Proj("+init=EPSG:2451")

gps_socket = gps3.GPSDSocket()
data_stream = gps3.DataStream()
gps_socket.connect()
gps_socket.watch()
for new_data in gps_socket:
    if new_data:
        data_stream.unpack(new_data)
        print('Altitude = ', data_stream.TPV['alt'])
        print('Latitude = ', data_stream.TPV['lat'])
        print('Longitude = ', data_stream.TPV['lon'])
        lat = data_stream.TPV['lat']
        lon = data_stream.TPV['lon']

        if lat != 'n/a' :
            y, x = pyproj.transform(EPSG4612, EPSG2451, lon,lat)
            ofs.write(str(lat) + ' ' + str(lon) + '\r\n')

            print('x = ', x)
            print('y = ', y)
