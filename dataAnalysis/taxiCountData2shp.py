import numpy as np
import matplotlib.pyplot as plt
import os
import datetime

# Taxi2pointData.scala先生成网格统计数据

import pandas as pd




max_lat = 0
max_lon = 0
min_lat = 200
min_lon = 200


RedionData = []
with open("data/sz_points_GCJ02_v4.csv", "r") as fin:
    lines = fin.readlines()
    for line in lines:
        if line[-1] == "\n":
            line = line[:-1]
        RedionData.append(line.split(","))

for k in range(len(RedionData)):#绘制整个城市的区域
    y_arr = []
    x_arr = []
    region_min_lat = float(RedionData[k][4])
    min_lat = min(min_lat,region_min_lat)
    region_min_lon = float(RedionData[k][3])
    min_lon = min(min_lon, region_min_lon)
    region_max_lat = float(RedionData[k][6])
    max_lat = max(max_lat, region_max_lat)
    region_max_lon = float(RedionData[k][5])
    max_lon = max(max_lon, region_max_lon)

    for j in range(7, len(RedionData[k]), 2):
        # print(j)
        x_arr.append(float(RedionData[k][j]))
        y_arr.append(float(RedionData[k][j + 1]))

    plt.plot(x_arr, y_arr,color="k",linewidth=0.1)

print(min_lon)
print(min_lat)
print(max_lon)
print(max_lat)

# exit()

# df = pd.read_csv(r'data/sz_points_v3.csv',header=None)
# mat = df.values

# max_vals = mat.max(axis=0)
# max_lat = max_vals[5]
# max_lon = max_vals[6]
# min_vals = mat.min(axis=0)
# min_lat = max_vals[3]
# min_lon = max_vals[4]

# topN_OD_Region = []
# topN_OD_Region.append([1,3])
# i = 0
# # # 绘制绘制起点和终点
# if topN_OD_Region[i][0] == topN_OD_Region[i][1]:  # 起点跟终点是同一个区域
#     y_arr = []
#     x_arr = []
#     RegionNum = topN_OD_Region[i][0]
#     for j in range(7, len(RedionData[RegionNum]), 2):
#         # print(j)
#         x_arr.append(float(RedionData[RegionNum][j]))
#         y_arr.append(float(RedionData[RegionNum][j + 1]))
#     plt.fill(x_arr,y_arr,alpha=0.3,color="green")
# else:
#     y_arr = []
#     x_arr = []
#     RegionNum = topN_OD_Region[i][0]
#     for j in range(7, len(RedionData[RegionNum]), 2):
#         # print(j)
#         x_arr.append(float(RedionData[RegionNum][j]))
#         y_arr.append(float(RedionData[RegionNum][j + 1]))
#     plt.fill(x_arr, y_arr, alpha=0.3, color="orange")
#     y_arr = []
#     x_arr = []
#     RegionNum = topN_OD_Region[i][1]
#     for j in range(7, len(RedionData[RegionNum]), 2):
#         # print(j)
#         x_arr.append(float(RedionData[RegionNum][j]))
#         y_arr.append(float(RedionData[RegionNum][j + 1]))
#     plt.fill(x_arr, y_arr, alpha=0.3, color="blue")
# centerX = 113.99466909048306
# centerY = 22.592960639012034

# # 高德地图拾取系统
# center = [[113.897469,22.457764],#SCT行政大楼
#           [114.531248,22.462121] ,#日出观景台
#           [114.587138,22.655723],# 红排角
#           [113.954324,22.505089],#弯月山谷-观景平台
#           [113.952761,22.488265], #深圳观桥公园
#           [113.916166,22.476449], #深圳湾游艇会大楼
#           ]
# for i in range(len(center)):
#     plt.scatter(center[i][0], center[i][1], color='r',s=0.1)

# with open(r"D:\subwayData\mutiOD\TaxiPointInData\2018-12-18\part-00000",'r') as fin:
#     lines = fin.readlines()
#     for line in lines:
#         if line[-1] == "\n":
#             line = line[:-1]
#         line_split = line.split(",")
#         lat = float(line_split[0])
#         lon = float(line_split[1])
#         num =  int(line_split[2])


# 数据已经转换成GCJ02
df = pd.read_csv(r'D:\subwayData\mutiOD\TaxiPointInData\2018-12-18\part-00000',header=None)
mat = df.values
max_val = mat.max(axis=0)[-1]
from geo_utile import gcj02towgs84
from geo_utile import wgs84togcj02
from geo_utile import bd09_to_gcj02

plt.scatter(min_lon,min_lat, color='b', s=0.1,alpha=1)
plt.scatter(max_lon,min_lat, color='b', s=0.1,alpha=1)
plt.scatter(min_lon,max_lat, color='b', s=0.1,alpha=1)
plt.scatter(max_lon,max_lat, color='b', s=0.1,alpha=1)


for i in range(mat.shape[0]):
    # [lon,lat] = wgs84togcj02(mat[i][0], mat[i][1])
    # [lon,lat] = gcj02towgs84(mat[i][0], mat[i][1])
    # [lon, lat] = bd09_to_gcj02(mat[i][0], mat[i][1])
    [lon, lat] = [mat[i][0], mat[i][1]]

    # if lat > (max_lat+0.5) or lat < (min_lat-0.2) or lon > (max_lon+0.5) or lon < (min_lon-0.2):
    # if lat > max_lat or lat < min_lat or lon > max_lon or lon < min_lon:
        # print(mat[i])
        # continue

    # print(mat[i])
    plt.scatter(lon,lat, color='r', s=0.5,alpha=mat[i][2]/max_val*9/10+0.1)
plt.savefig("pdf/FreeCount.pdf")
# # plt.show()
