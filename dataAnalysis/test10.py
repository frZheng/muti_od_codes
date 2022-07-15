import numpy as np
import matplotlib.pyplot as plt
import os
import datetime

# data = "2018-12-01 00:00:05,粤BDD3287,112135,1543591271000,1543593547000,76.5,2.6,18.274,2.466,0:10:10,1,00000000000000000000,0.0,114.02544,22.630413333333333,114.10153333333334,22.547933333333333"
# data_split = data.split(",")
# print(len(data_split))
# exit()
RedionData = []
with open("data/sz_points_v3.csv", "r") as fin:
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
# 高德地图拾取系统
center = [[113.897469,22.457764],#SCT行政大楼
          [114.531248,22.462121] ,#日出观景台
          [114.587138,22.655723],# 红排角
          [113.954324,22.505089],#弯月山谷-观景平台
          [113.952761,22.488265], #深圳观桥公园
          [113.916166,22.476449], #深圳湾游艇会大楼
          ]
from geo_utile import gcj02towgs84
from geo_utile import wgs84togcj02
from geo_utile import bd09_to_gcj02

for i in range(len(center)):
    [lng,lat] = gcj02towgs84(center[i][0], center[i][1])
    plt.scatter(lng,lat, color='r',s=0.1)
plt.savefig("pdf/test.pdf")
# # plt.show()

# import datetime
# test_dt = datetime.datetime.strptime('2018-11-09','%Y-%m-%d') + datetime.timedelta(days=1)
# test = test_dt.strftime('%Y-%m-%d')
# print(test)
# test = test_dt.strftime('%Y%m%d')
# print(test)

# import numpy as np
#
# a = np.array([[1,2,3],[4,5,6]])
# b = np.sum(a,axis=1)
# b = np.reshape(b,newshape=[-1,1])
# c = a/b
# print(b)
# print(c)


# str = "2018-12-18 00:00:00,粤B4C0N7,121749,1545062175000,1545062402000,15.0,3.38,2.499,6.635,0:0:5,1,ffffffffffffffffffff,0.0,114.12190166666667,22.572741666666666,114.111825,22.587381666666666"
# str_split = str.split(",")
# for i in range(len(str_split)):
#     print(i, str_split[i])



import os
from PyPDF2 import PdfFileReader, PdfFileWriter
import time
#file_name = ['周报-郑富荣-202001-2.pdf','周报-郑富荣-202101-3.pdf']

# def getFileName(filedir):
#     file_list = [os.path.join(root, filespath) \
#                  for root, dirs, files in os.walk(filedir) \
#                  for filespath in files \
#                  if str(filespath).endswith('pdf')
#                  ]
#     return file_list if file_list else []

# pdf_fileName = getFileName('./')
# print(pdf_fileName)

'''
file_name = []
file_name.append(pdf_fileName[-2])
file_name.append(pdf_fileName[-1])
print(file_name)
'''

# pdf_fileName = ["pdf/Free2Pub_201812_all.pdf","pdf/Free2Pub_201812_weekay.pdf","pdf/Free2Pub_201812_weekend.pdf"]
# output = PdfFileWriter()
# outputPages = 0
# for i in range(len(pdf_fileName)):
#     input = PdfFileReader(open(pdf_fileName[i], "rb"))
#     pageCount = input.getNumPages()
#     outputPages += pageCount
#
#     for iPage in range(pageCount):
#         output.addPage(input.getPage(iPage))
#
# outfile = "pdf/testOut.pdf"
# print(outfile,pdf_fileName[-1])
# #outfile = '周报-郑富荣-20210124.pdf'
# print("合并后的总页数:%d."%outputPages)
# outputStream = open(outfile, "wb")
# output.write(outputStream)
# outputStream.close()
#
# '''
# if pdf_fileName[-1] is outfile:
#     pass
#     print('文件已经覆盖')
# else:
#     #os.remove(pdf_fileName[-1])
#     print('文件已经删除')
# '''


# # Str = "https://datacenter-web.eastmoney.com/api/data/v1/get?callback=jQuery1123038360958864323935_1657677989274&sortColumns=PUBLIC_START_DATE&sortTypes=-1&pageSize=50&pageNumber=1&reportName=RPT_BOND_CB_LIST&columns=ALL&quoteColumns=f2~01~CONVERT_STOCK_CODE~CONVERT_STOCK_PRICE%2Cf235~10~SECURITY_CODE~TRANSFER_PRICE%2Cf236~10~SECURITY_CODE~TRANSFER_VALUE%2Cf2~10~SECURITY_CODE~CURRENT_BOND_PRICE%2Cf237~10~SECURITY_CODE~TRANSFER_PREMIUM_RATIO%2Cf239~10~SECURITY_CODE~RESALE_TRIG_PRICE%2Cf240~10~SECURITY_CODE~REDEEM_TRIG_PRICE%2Cf23~01~CONVERT_STOCK_CODE~PBV_RATIO&quoteType=0&source=WEB&client=WEB"
# Str = "https://datacenter-web.eastmoney.com/api/data/v1/get?callback=jQuery112307850950474318004_1657678377543&sortColumns=PUBLIC_START_DATE&sortTypes=-1&pageSize=50&pageNumber=1&reportName=RPT_BOND_CB_LIST&columns=ALL&quoteColumns=f2~01~CONVERT_STOCK_CODE~CONVERT_STOCK_PRICE%2Cf235~10~SECURITY_CODE~TRANSFER_PRICE%2Cf236~10~SECURITY_CODE~TRANSFER_VALUE%2Cf2~10~SECURITY_CODE~CURRENT_BOND_PRICE%2Cf237~10~SECURITY_CODE~TRANSFER_PREMIUM_RATIO%2Cf239~10~SECURITY_CODE~RESALE_TRIG_PRICE%2Cf240~10~SECURITY_CODE~REDEEM_TRIG_PRICE%2Cf23~01~CONVERT_STOCK_CODE~PBV_RATIO&quoteType=0&source=WEB&client=WEB"
# Str_split = Str.split("&")
# for i in Str_split:
#     print(i)
