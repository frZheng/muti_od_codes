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
        # r"D:\subwayData\csjs_tools\map\zone_2077_zone-WGS1984_度-071ac2f9-80c3-4273-875e-a846675a5da8\zone_2077_zone-WGS1984_度.shp")
        # r"D:\subwayData\csjs_tools\map\sects\sects.shp")
        r"C:\Users\Administrator\Documents\ArcGIS\mySave\test2\polygon01.shp")



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
    # with open("data/sz_points_GCJ02_oldmap.csv", "w") as fout:
    # with open("data/sz_points_GCJ02_v4.csv", "w") as fout:
    with open("data/sz_points_GCJ02_test.csv", "w") as fout:
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
            # from geo_utile import wgs84togcj02
            # center = wgs84togcj02(float(centers[i][0]),float(centers[i][1])) # 按照argis生成的中心
            # center = [float(centers[i][0]),float(centers[i][1])]
            center = [0,0]
            msg += str(center[0]) + ","
            msg += str(center[1]) + ","

            for j in range(len(shapes[i].bbox)):
                msg += str(shapes[i].bbox[j]) + ","
            # 能按照顺序连接成框
            for j in range(len(shapes[i].points)):
                # [lng,lat] = wgs84togcj02(float(shapes[i].points[j][0]),float(shapes[i].points[j][1]))
                [lng, lat] = [float(shapes[i].points[j][0]), float(shapes[i].points[j][1])]
                msg += str(lng) + "," + str(lat) + ","
            msg = msg[:-1]  # 去掉最后一个逗号
            fout.write(msg + "\n")

# writeFile()

def writeShp():
    # # -*- coding: utf-8 -*-
    # import osr
    # import shapefile  # 使用pyshp
    # data_address = r"C:\Users\Administrator\Documents\ArcGIS\mySave\test2/polygon01.shp"  # 新建数据存放位置 file = shapefile.Writer(data_address)
    # file = shapefile.Writer(data_address)
    # # 创建两个字段
    # file.field('FIRST_FLD')
    # file.field('type', 'C', '40')  # 'SECOND_FLD'为字段名称，C代表数据类型为字符串，长度为 40
    # file.poly([[[117.210024, 40.082262], [117.105315, 40.074479], [117.105315, 40.074479], [117.102851, 40.073563],
    #             [116.720969, 39.599884]]])
    # file.record('First', 'polygon')
    # file.poly([[[110.210024, 40.082262], [110.105315, 40.004409], [110.105315, 40.004409], [110.102851, 40.003563],
    #             [112.020969, 40.599884]]])
    # file.record('Second', 'polygon')
    # file.poly([[[112.05, 38.056], [112.05, 40.056], [115.05, 40.056], [114.05, 37.056]]])
    # file.record('third', 'polygon')
    # # 关闭文件操作流
    # file.close()
    # # 定义投影
    # proj = osr.SpatialReference()
    # proj.ImportFromEPSG(4326)  # 4326-GCS_WGS_1984; 4490- GCS_China_Geodetic_Coordinate_System_2000
    # wkt = proj.ExportToWkt()
    # # 写入投影
    # f = open(data_address.replace(".shp", ".prj"), 'w')
    # f.write(wkt)
    # f.close()
    import os
    # 安装 geopandas https://blog.csdn.net/qq_44322368/article/details/122808209
    import geopandas
    # pip install geos
    # pip install shapely
    from shapely import geometry
    import matplotlib.pyplot as plt

    geometryData = []
    with open("data/sz_points_GCJ02_v4.csv", "r") as fin:
        lines = fin.readlines()
        for line in lines:
            if line[-1] == "\n":
                line = line[:-1]
            line_split = line.split(",")
            oneRegionData = []
            for i in range(7,len(line_split),2):
                lon = float(line_split[i])
                lat = float(line_split[i+1])
                oneRegionData.append([lon,lat])
            geometryData.append(geometry.Polygon(oneRegionData))

    cq = geopandas.GeoSeries(geometryData,
                             crs='EPSG:4326'
                             )

    # cq = geopandas.GeoSeries([geometry.Polygon([[14, 14], [13, 18], [20, 11], [18, 10]]),
    #                           geometry.Polygon([[0, 0], [10, 0], [10, 10], [0, 10]],
    #                                            [[[1, 3], [5, 3], [5, 1], [1, 1]],
    #                                             [[9, 9], [9, 8], [8, 8], [8, 9]]]),
    #                           geometry.Polygon([[11, 2], [11, 10], [12, 10], [12, 2]])
    #                           ],
    #                          # index = ['简单面','复杂面','c区'],
    #                          crs='EPSG:4326'
    #                          )

    # cq = geopandas.GeoSeries([geometry.Polygon([(14,14),(13,18),(20,11),(18,10)]),
    #                           geometry.Polygon([(0,0), (10, 0), (10, 10), (0, 10)],
    #                                            [((1, 3), (5, 3), (5, 1), (1, 1)),
    #                                             ((9, 9), (9, 8), (8, 8), (8, 9))]),
    #                           geometry.Polygon([(11, 2), (11, 10), (12, 10), (12, 2)])
    #                           ],
    #                          # index = ['简单面','复杂面','c区'],
    #                          crs='EPSG:4326'
    # )
    cq.to_file(r"C:\Users\Administrator\Documents\ArcGIS\mySave\test2/polygon01.shp",
               driver='ESRI Shapefile',
               encoding='utf-8')
    cq.plot()
    plt.show()

# writeShp()



def writeMarginFile():

    # 先用ARGIS手动绘制后再取最大面积的区域就是深圳的外围
    sf = shapefile.Reader(
        r"C:\Users\Administrator\Documents\ArcGIS\mySave\test\sz_margin.shp")

    shapes = sf.shapes()
    max_area_index = 0
    for i in range(0, len(shapes)):
    print(shapes)

    exit()
    # 格式 序号,lon1,lat1,,lon2,lat2,...,lonn,latn,
    with open("data/sz_margin_GCJ02_v1.csv", "w") as fout:
        for i in range(0, len(shapes)):
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

writeMarginFile()


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
