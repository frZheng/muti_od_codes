import numpy as np
import matplotlib.pyplot as plt
import os
import datetime
import pandas as pd

# # 背景尺寸
# width = 6
# height = 30
# dpi = 1200
#
# xysize = 13
# size3 = -0.3
# psize = 3
#
# font = {'family': 'Times New Roman', 'weight': 'bold', 'size': psize}
# fig = plt.figure(dpi=dpi, figsize=(width, height))
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
    for j in range(7, len(RedionData[k]), 2):
        # print(j)
        x_arr.append(float(RedionData[k][j]))
        y_arr.append(float(RedionData[k][j + 1]))

    plt.plot(x_arr, y_arr,color="k",linewidth=0.1)


from geo_utile import wgs84togcj02
df = pd.read_csv(r'D:\subwayData\mutiOD\TaxiAnomalData\20181218\part-00000',header=None)
# print(df)
val = df.values
for i in range(val.shape[0]):
    olng = val[i,13]
    olat = val[i,14]
    # dlng = df[i,15]
    # dlat = df[i,16]

    [lng,lat] = wgs84togcj02(olng, olat)
    print(lng,lat)
    plt.scatter(lng,lat, color='r',s=0.1)
plt.savefig("pdf/TaxiAnormalData.pdf")
