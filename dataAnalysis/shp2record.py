# pip install pyshp
# pip install osgeo
# conda install geopandas

import shapefile
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import time
from geo_utile import center_geolocation
from geo_utile import getCenterOfGravityPoint

def writeFile():
    # sf = shapefile.Reader(r"D:\subwayData\csjs_tools\map\sects\sects.shp")
    sf = shapefile.Reader(
        r"D:\subwayData\csjs_tools\map\zone_2077_zone-WGS1984_度-071ac2f9-80c3-4273-875e-a846675a5da8\zone_2077_zone-WGS1984_度.shp")



    shapes = sf.shapes()
    arr = []
    print("len = ", len(shapes))
    centers = []
    with open("data/sz_points_Centers.csv", "r") as fin:
        lines = fin.readlines()
        for line in lines:
            line = line[:-1]
            centers.append(line.split(","))
    # 格式 序号,min_lon,min_lat,max_lon,max_lat,x,y,x,y
    with open("data/sz_points_GCJ02_v4.csv", "w") as fout:
        for i in range(0, len(shapes)):
            datas = shapes[i]
            arr.append(shapes[i].bbox)
            # print(i,len(datas.points))
            msg = ""
            msg += str(i) + ","

            points = []
            for j in range(len(shapes[i].points)):
                points.append([shapes[i].points[j][0],shapes[i].points[j][1]])
            # center = center_geolocation(points) # V1 的中心计算方式
            # center = getCenterOfGravityPoint(points) # V2 的计算方式
            from geo_utile import wgs84togcj02
            center = wgs84togcj02(float(centers[i][0]),float(centers[i][1])) # 按照argis生成的中心
            msg += str(center[0]) + ","
            msg += str(center[1]) + ","

            for j in range(len(shapes[i].bbox)):
                msg += str(shapes[i].bbox[j]) + ","
            # 能按照顺序连接成框
            for j in range(len(shapes[i].points)):
                [lng,lat] = wgs84togcj02(float(shapes[i].points[j][0]),float(shapes[i].points[j][1]))
                msg += str(lng) + "," + str(lat) + ","
            msg = msg[:-1]  # 去掉最后一个逗号
            fout.write(msg + "\n")

writeFile()

# def writeCenterFile():
#     sf = shapefile.Reader(r"C:\Users\Administrator\Documents\ArcGIS\mySave\test.shp")
#     shapes = sf.shapes()
#     with open("data/sz_points_Centers.csv", "w") as fout:
#         for i in range(0, len(shapes)):
#             msg = ""
#             msg += str(shapes[i].points[0][0])
#             msg += ","
#             msg += str(shapes[i].points[0][1])
#             fout.write(msg + "\n")
#
# writeCenterFile()

# def testFile():
#     with open("data/sz_points.csv", "r") as fin:
#         lines = fin.readlines()
#         # for i in range(len(lines)):
#         region = 1953
#         for i in range(region,region+1):
#             line = lines[i][:-1]
#             line_split = line.split(",")
#             x_arr = []
#             y_arr = []
#             # print(len(line_split))
#             y_arr_oneline = []
#             for j in range(7, len(line_split), 2):
#                 # print(j)
#                 y_arr.append(float(line_split[j]))
#                 x_arr.append(float(line_split[j + 1]))
#
#             fig = plt.figure()
#             window = fig.add_subplot(111)
#             l, = plt.plot([], [], 'r-')
#             data = np.array([y_arr,x_arr])
#             plt.xlim(min(y_arr) - (max(y_arr)-min(y_arr))/4, max(y_arr)+(max(y_arr)-min(y_arr))/4)
#             plt.ylim(min(x_arr)- (max(x_arr)-min(x_arr))/4, max(x_arr) + (max(x_arr)-min(x_arr))/4)
#
#             def update_line(num, data, line):
#                 print(num)
#                 line.set_data(data[..., :num])
#                 return line,
#
#
#             ani = animation.FuncAnimation(fig, update_line, len(y_arr), fargs=(data, l),
#                                           interval=100, blit=True,repeat=False)
#             plt.show()
#             # for i in range(10):
#             #     print(i)
#             #     time.sleep(1)
#             # plt.close()
#             # testFile()
# testFile()
