# import numpy as np
# a = np.array([[1,2],
#      [4,5]])
# # print(a)
# # print(a[:,:2])
# # print(a[1])
# a += (1,2)
# print(a)

import os
import datetime
# 地铁数据没有20180418,20140612这两天数据,其他数据量还需要再检查
# path_list = sorted(os.listdir("D:\subwayData\mutiOD\SubwayData"))

# 公交数据没有
# 20180418
# 20180609
# 20180610
# 20180612
# 20180814
# 20180816
# 20180825
# 20180826
# 20180827
# 这个文件
# path_list = sorted(os.listdir("D:\subwayData\mutiOD\BusD"))

# 公交数据没有
# 20180418
# 20180609
# 20180610
# 20180612
# 20180817
# 20180825
# 20180826
# 20180827
# 20181228

#20180418,20180609,20180610,20180612,20180817,20180825,20180826,20180827,20181228
# path_list = sorted(os.listdir("D:\subwayData\mutiOD\HomeAndWork\Day"))

#
path_list = sorted(os.listdir("G:\subwayData\mutiOD\HomeAndWork\Month"))
print(path_list)

# bb=datetime.datetime.strptime(path_list[0],"%Y%m%d")
# bb1=datetime.datetime.strptime(path_list[1],"%Y%m%d")
# delta_time = bb1 - bb
# print(delta_time.total_seconds())

one_day_seconds = 24*60*60
for i in range(1,len(path_list)):
     delta_time = datetime.datetime.strptime(path_list[i], "%Y%m%d") - datetime.datetime.strptime(path_list[i-1], "%Y%m%d")
     if delta_time.total_seconds() != one_day_seconds:
          print(path_list[i])

