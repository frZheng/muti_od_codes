# pip install pyshp
# pip install osgeo
# conda install geopandas

# import shapefile
import matplotlib.pyplot as plt
# import matplotlib.animation as animation
import numpy as np
import time




def pltFigure():
    with open("data/sz_points_GCJ02_v4.csv", "r") as fin:
        lines = fin.readlines()
        # for i in range(len(lines)):

        # regionNum = 1561
        # x = 114.032365
        # y = 22.740262
        #
        # centerX = 113.97221006447938
        # centerY = 22.551999823686387

        for lineNum in range(100,101):
            # lineNum = 0
            with open("D:\subwayData\mutiOD\stationsOutputV4\part-00000","r",encoding="UTF-8") as f:
                allLine = f.readlines()
                line = allLine[lineNum]
                line = line[:-1]
                line_split = line.split(",")
                regionNum = int(line_split[3])
                x = float(line_split[1])
                y = float(line_split[2])
                centerX = float(line_split[4])
                centerY = float(line_split[5])
            print(x,y,regionNum)
            for i in range(regionNum,regionNum+1):
                line = lines[i][:-1]
                line_split = line.split(",")
                x_arr = []
                y_arr = []
                # print(len(line_split))
                y_arr_oneline = []
                for j in range(7, len(line_split), 2):
                    # print(j)
                    x_arr.append(float(line_split[j]))
                    y_arr.append(float(line_split[j + 1]))
                # print(y_arr)
                # print(x_arr)
                plt.plot(x_arr,y_arr)

                plt.scatter(x, y,color='k',s=1)
                plt.annotate(s = "P",xy=(x,y),color='k')
                plt.scatter(centerX, centerY, color='r',s=1)
                plt.annotate(s="C", xy=(centerX, centerY), color='r')
                plt.show()
                time.sleep(2)
                plt.close()

pltFigure()
