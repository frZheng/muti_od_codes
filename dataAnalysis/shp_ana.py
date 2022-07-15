# pip install pyshp
# pip install osgeo
# conda install geopandas

import shapefile
import pandas as pd
#
# sf = shapefile.Reader(r"D:\subwayData\csjs_tools\map\sects\sects.shp")
sf = shapefile.Reader(r"D:\subwayData\csjs_tools\map\zone_2077_zone-WGS1984_度-071ac2f9-80c3-4273-875e-a846675a5da8\zone_2077_zone-WGS1984_度.shp")
# sf = shapefile.Reader(r"C:\Users\Administrator\Documents\ArcGIS\mySave\test.shp")

shapes = sf.shapes()
arr = []
print("len = ", len(shapes))
for i in range(0, len(shapes)):
    datas = shapes[i]
    arr.append(shapes[i].bbox)
    # print(i,len(datas.points))
grids = pd.DataFrame(arr, columns=['min_lon', 'min_lat', 'max_lon', 'max_lat'])
min_lon = grids['min_lon'].min()
min_lat = grids['min_lat'].min()
max_lon = grids['max_lon'].max()
max_lat = grids['max_lat'].max()

# print(grids)

# import geopandas #windows 无法使用
# # shps = geopandas.read_file(r"/tmp/zfr_files/muti_od/codes/dataAnalysis/map/sects/sects.shp")
# shps = geopandas.read_file(r"map/sects/sects.shp")
# # shps.plot()
# shps.savefig("test.pdf")
# a = "123"
# print(a.isdecimal())