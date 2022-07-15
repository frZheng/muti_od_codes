import os
import numpy as np
import datetime
import time
import math

cal_start_time = time.time()
# file_name = "shenzhen-station.txt"
# station_dict_list = []
# txt_file = []
# with open(file_name,"r",encoding='utf-8') as fin:
#     for line in fin.readlines():
#         line = line[:-1] # 去掉\n
#         txt_file.append(line)
# print("txt len:",len(txt_file))
# for i in range(0,len(txt_file),1):
#     station_dict_list.append([txt_file[i].split("-")[0],int(txt_file[i].split("-")[1])])
# print(len(station_dict_list))
# print(station_dict_list)
# station_dict = dict(station_dict_list)
# # print(station_dict)
# print(station_dict["上塘"])
#
#
# # 一天的开始时间,默认是七点钟,单位分钟
# start_time = 5*60
# # 一天结束时间,默认是23点钟,单位分钟
# end_time = 23*60*60
# y_end_time = 23*60*60
# # 一天的工作时长
# lenOfDay = end_time - start_time
# y_lenOfDay = y_end_time - start_time
#
#
# # num_of_station = 118
# num_of_station = len(txt_file)
# time_list = [[] for i in range(num_of_station*num_of_station)]
# # 遍历文件每一条记录,将数组中对应的元素加一
# # 暂时没考虑数据丢失


path_common = r"D:\subwayData\BusD"
# path_common = r"D:\subwayData\BusD_test"
date_names_list = sorted(os.listdir(path_common))

print(date_names_list)
traval_time_array = np.zeros(shape=[400 + 1],dtype=np.int32)

for date_name in date_names_list:
    file_names_list = sorted(os.listdir(os.path.join(path_common,date_name)))
    for file_name in file_names_list:
        abs_file_name = os.path.join(path_common,date_name,file_name,"withtime/part-r-00000")
        print(abs_file_name)
        real_data_num = 0

        if os.path.isfile(abs_file_name):
            with open(abs_file_name, 'r',encoding='utf-8') as fin:
                # 读取所有行
                for line in fin.readlines():
                    # print('line num', line_num)
                    # print(line)
                    t_in = 0
                    t_out = 0
                    in_station = -1
                    out_station = -1

                    if line[-1] == "\n":
                        line = line[:-1] # 去掉\n

                    # txtFile.append(line)
                    line_split_list = line.split(',')
                    # print(line_split_list)


                    t_in_index = 5
                    t_in_datetime = datetime.datetime.strptime(line_split_list[t_in_index], "%Y-%m-%dT%H:%M:%S.%fZ")
                    # 入闸时间,小时乘以60,加上所在的分钟,,单位分钟
                    t_in = t_in_datetime.hour*60*60 + t_in_datetime.minute*60 + t_in_datetime.second

                    t_out_index = 11
                    t_out_datetime = datetime.datetime.strptime(line_split_list[t_out_index], "%Y-%m-%dT%H:%M:%S.%fZ")
                    # 出闸时间,小时乘以60,加上所在的分钟,,单位分钟
                    t_out = t_out_datetime.hour * 60*60 + t_out_datetime.minute*60 + t_out_datetime.second

                    traval_time = (t_out - t_in) / 60
                    traval_time = int(np.around(traval_time))

                    # if (t_in < start_time or
                    #         t_in >= end_time or
                    #         t_out < start_time or
                    #         t_out >= y_end_time or
                    #         t_in > t_out or
                    #         (not (t_out_datetime.day == t_in_datetime.day)) or
                    #         (traval_time > 180)):
                    #     # print(t_in, t_out, traval_time)
                    #     # print(line_split_list)
                    #     continue

                    traval_time = traval_time if traval_time > -200 else -200
                    traval_time = traval_time if traval_time < 200 else 200
                    traval_time = traval_time + 200

                    real_data_num += 1
                    traval_time_array[traval_time] += 1


        print("real_data_num: ",real_data_num)



    today = str(datetime.date.today().strftime("%Y%m%d"))
    npz_file_name = 'data/travelTime_tripNum_{}_{}'.format(date_name,today)
    #np.savez(npz_file_name, in_matrix=in_matrix)
    print("load shape: ",traval_time_array.shape)
    np.savez_compressed(npz_file_name, matrix=traval_time_array)
    traval_time_array = np.load(npz_file_name+".npz")["matrix"]
    print("load shape: ",traval_time_array.shape)
    # exit()


