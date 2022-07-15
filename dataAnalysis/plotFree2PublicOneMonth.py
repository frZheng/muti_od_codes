import numpy as np
import matplotlib.pyplot as plt
import os
import datetime

if __name__ == "__main__":

    # 背景尺寸
    width = 6
    height = 30
    dpi = 1200

    xysize = 13
    size3 = -0.3
    psize = 3

    font = {'family': 'Times New Roman', 'weight': 'bold', 'size': psize}

    topN_OD_Region = []
    path = "D:\subwayData\mutiOD"
    with open(path + "\TopNTaxiODFlow\part-00000","r") as fin:
        lines = fin.readlines()
        for i in range(20):
            line = lines[i][:-1]
            line_split = line.split(",")
            topN_OD_Region.append([int(line_split[0]),int(line_split[1])])
    # print(topN_OD_Region)
    # exit()
    # topN_OD_Data_Pub = [[] for i in range(len(topN_OD_Region))]

    StartTime = 6 * 60  # 统计起始时间为6点
    EndtTime = 23 * 60  # 统计起始时间为23点
    TimeSlot = 30  # 统计的时间间隔
    TimeSlotNum = int((EndtTime-StartTime)/TimeSlot)

    topN_OD_Data_Free = np.zeros(shape=[len(topN_OD_Region),TimeSlotNum,TimeSlotNum], dtype=np.int32)
    topN_OD_Data_Pub = np.zeros(shape=[len(topN_OD_Region), TimeSlotNum, TimeSlotNum], dtype=np.int32)
    dateNum = 30+1
    StartDateStr = "20181201"
    StartDate = datetime.datetime.strptime(StartDateStr, '%Y%m%d')
    for data_i in range(dateNum):
        dateDT = StartDate + datetime.timedelta(days=data_i)
        weekday = dateDT.weekday()
        # if weekday > 4: # 5,6 对应周末
        #     continue
        # print(weekday)
        # exit()
        date = dateDT.strftime('%Y%m%d')
        # print(date)
        TaxiFile = path + "\TaxiODFlow\\" + date +"\part-00000"
        PubDate = date.replace("-", "")  # -为分隔符，改为无分隔符
        PubFile = path + "\odFlow\\" + PubDate + "\part-00000"

        if os.path.exists(TaxiFile):
            print(TaxiFile)
            with open(TaxiFile, "r") as fin:
                lines = fin.readlines()
                for line in lines:
                    if line[-1] == "\n":
                        line = line[:-1]
                    line_split = line.split(",")
                    ot = int(line_split[0])
                    oRegion = int(line_split[1])
                    dt = int(line_split[2])
                    dRegion = int(line_split[3])
                    passengerNum = int(line_split[4])

                    for j in range(len(topN_OD_Region)):
                        if topN_OD_Region[j][0] == oRegion and topN_OD_Region[j][1] == dRegion:
                            topN_OD_Data_Free[j,ot,dt] += passengerNum
                            break

        if os.path.exists(PubFile):
            print(PubFile)
            with open(PubFile, "r") as fin:
                lines = fin.readlines()
                for line in lines:
                    if line[-1] == "\n":
                        line = line[:-1]
                    line_split = line.split(",")
                    ot = int(line_split[0])
                    oRegion = int(line_split[1])
                    dt = int(line_split[2])
                    dRegion = int(line_split[3])
                    passengerNum = int(line_split[4])

                    for j in range(len(topN_OD_Region)):
                        if topN_OD_Region[j][0] == oRegion and  topN_OD_Region[j][1]==dRegion:
                            topN_OD_Data_Pub[j,ot,dt] = passengerNum
                            break
    topN_Ot_Data_Free = np.sum(topN_OD_Data_Free, axis=2)  # 将下车时间纬度累加后得到，在起点从出发时间出发到终点的人数
    topN_Ot_Data_Pub = np.sum(topN_OD_Data_Pub, axis=2)  # 将下车时间纬度累加后得到，在起点从出发时间出发到终点的人数



    npz_file_name_Free = "tmp/topN_Ot_Data_Free.npz"
    npz_file_name_Pub = "tmp/topN_Ot_Data_Pub.npz"

    np.savez_compressed(npz_file_name_Free, matrix=topN_Ot_Data_Free)
    np.savez_compressed(npz_file_name_Pub, matrix=topN_Ot_Data_Pub)

    topN_Ot_Data_FreeInt = np.load(npz_file_name_Free)["matrix"]
    # with open("data/topN_Ot_Data_Free_F2P.csv","w") as fout:
    #     for j in range(len(topN_OD_Region)):
    #         msg = ""
    #         msg += str(topN_OD_Region[j][0])
    #         msg += ","
    #         msg += str(topN_OD_Region[j][1])
    #         msg += ","
    #         for k in range(TimeSlotNum):
    #             msg += str(topN_Ot_Data_FreeInt[j][k])
    #             msg += ","
    #         msg = msg[:-1]
    #         msg += "\n"
    #         fout.write(msg)


    topN_Ot_Data_PubInt = np.load(npz_file_name_Pub)["matrix"]

    # with open("data/topN_Ot_Data_Pub_F2P.csv","w") as fout:
    #     for j in range(len(topN_OD_Region)):
    #         msg = ""
    #         msg += str(topN_OD_Region[j][0])
    #         msg += ","
    #         msg += str(topN_OD_Region[j][1])
    #         msg += ","
    #         for k in range(TimeSlotNum):
    #             msg += str(topN_Ot_Data_PubInt[j][k])
    #             msg += ","
    #         msg = msg[:-1]
    #         msg += "\n"
    #         fout.write(msg)



    with open("data/F2P.csv","w") as fout:
        for j in range(len(topN_OD_Region)):
            msg = ""
            # msg += str(topN_OD_Region[j][0])
            # msg += ","
            # msg += str(topN_OD_Region[j][1])
            # msg += ","
            for k in range(TimeSlotNum):
                msg += str(topN_Ot_Data_FreeInt[j][k])
                msg += ","
            msg = msg[:-1]
            msg += "\n"
            fout.write(msg)

            msg=""
            for k in range(TimeSlotNum):
                msg += str(topN_Ot_Data_PubInt[j][k])
                msg += ","
            msg = msg[:-1]
            msg += "\n"
            fout.write(msg)
            fout.write("\n")

    topN_Ot_Data_FreeInt = topN_Ot_Data_FreeInt + 1  # 为了防止只有一个乘客的情况
    topN_Ot_Data_PubInt = topN_Ot_Data_PubInt + 1  # 为了防止只有一个乘客的情况
    # exit()
    topN_Ot_Data_FreeNSum = np.sum(topN_Ot_Data_FreeInt,axis=1)
    topN_Ot_Data_FreeNSum = np.reshape(topN_Ot_Data_FreeNSum, newshape=[-1, 1])
    topN_Ot_Data_Free = topN_Ot_Data_FreeInt/topN_Ot_Data_FreeNSum
    # topN_Ot_Data_Free = topN_Ot_Data_FreeInt
    topN_Ot_Data_PubNSum = np.sum(topN_Ot_Data_PubInt, axis=1)
    topN_Ot_Data_PubNSum = np.reshape(topN_Ot_Data_PubNSum, newshape=[-1, 1])
    topN_Ot_Data_Pub = topN_Ot_Data_PubInt / topN_Ot_Data_PubNSum
    # topN_Ot_Data_Pub = topN_Ot_Data_PubInt

    # print(topN_Ot_Data_Pub)
    topN_Ot_Data_Free[np.isnan(topN_Ot_Data_Free)] = 0
    topN_Ot_Data_Pub[np.isnan(topN_Ot_Data_Pub)] = 0
    # print(topN_Ot_Data_Pub)
    # exit()
    RegionData = []
    with open("data/sz_points_GCJ02_v4.csv", "r") as fin:
        lines = fin.readlines()
        for line in lines:
            if line[-1] == "\n":
                line = line[:-1]
            line_split = line.split(",")
            oneRegionData = []
            for pointsData in line_split:
                oneRegionData.append(float(pointsData))
            RegionData.append(oneRegionData)

    mats = [topN_Ot_Data_Pub,topN_Ot_Data_Free]
    labels = ["Pub", "Taxi"]
    colors = ["orange", "blue"]
    fig = plt.figure(dpi=dpi, figsize=(width, height))
    print("figure")
    for i in range(len(topN_OD_Region)):
        plt.subplot(len(topN_OD_Region), 2, 1 + i*2, frameon=True)
        for j in range(len(labels)):
            y = mats[j][i]
            y = y[2:-4]  # 只绘制7点到9点
            x = np.linspace(0, y.shape[0],y.shape[0])
            plt.plot(x, y, label=labels[j], color=colors[j])
            plt.legend(prop=font, labelspacing=0.1, borderaxespad=0.1, borderpad=0.1, handletextpad=0.1, frameon=True,
                   loc="best", handlelength=1, ncol=3)


        start_date = datetime.datetime.strptime("7:00", '%H:%M')
        plt.draw()
        x_labels = plt.gca().get_xticklabels()
        date_list = []
        j = 0
        for lab in x_labels:
            text = lab._text
            if j == 0:
                text = text[1:]
            # print(type(text))
            # if text[0:1] == "-":
            #     print("yes")
            #
            # print(text)
            # print(int(text[1:]))
            text = str(start_date + datetime.timedelta(minutes=30 * int(text)))
            text = text[11:11 + 5]
            # print(text)
            date_list.append(text)
            j += 1

        # print(date_list)
        plt.gca().set_xticklabels(date_list)

        # plt.title("Flow Ana Region " + str(region), font)
        # plt.grid(ls='--')
        # plt.ylim(-2, 2) #设置y轴范围,可以不设置

        # plt.xlim(-200, 201)  # 设置y轴范围,可以不设置
        x_axis = 'Time'# x轴的文字
        plt.xlabel(x_axis, font)
        y_axis = "number"# y轴的文字
        plt.ylabel(y_axis, font)
        plt.xticks(fontproperties=font["family"], size=font["size"], weight=font['weight'])
        plt.yticks(fontproperties=font["family"], size=font["size"], weight=font['weight'])
        plt.subplot(len(topN_OD_Region), 2, 1 + i * 2 + 1, frameon=True)
        for k in range(len(RegionData)):  # 绘制整个城市的区域
            y_arr = []
            x_arr = []
            for j in range(7, len(RegionData[k]), 2):
                # print(j)
                x_arr.append(float(RegionData[k][j]))
                y_arr.append(float(RegionData[k][j + 1]))

            plt.plot(x_arr, y_arr, color="k", linewidth=0.1)
        # # 绘制绘制起点和终点
        if topN_OD_Region[i][0] == topN_OD_Region[i][1]:  # 起点跟终点是同一个区域
            y_arr = []
            x_arr = []
            RegionNum = topN_OD_Region[i][0]
            for j in range(7, len(RegionData[RegionNum]), 2):
                # print(j)
                x_arr.append(float(RegionData[RegionNum][j]))
                y_arr.append(float(RegionData[RegionNum][j + 1]))
            plt.fill(x_arr, y_arr, alpha=0.3, color="green")
            centerX = RegionData[RegionNum][1]
            centerY = RegionData[RegionNum][2]
            plt.scatter(centerX, centerY, color='green', s=1)
            # plt.annotate(s="OD", xy=(centerX, centerY), color='r',weight="ultralight")
        else:
            y_arr = []
            x_arr = []
            RegionNum = topN_OD_Region[i][0]
            for j in range(7, len(RegionData[RegionNum]), 2):
                # print(j)
                x_arr.append(float(RegionData[RegionNum][j]))
                y_arr.append(float(RegionData[RegionNum][j + 1]))
            plt.fill(x_arr, y_arr, alpha=0.3, color="orange")
            centerX = RegionData[RegionNum][1]
            centerY = RegionData[RegionNum][2]
            plt.scatter(centerX, centerY, color='orange', s=1)
            # plt.annotate(s="O", xy=(centerX, centerY), color='r',weight="ultralight")
            y_arr = []
            x_arr = []
            RegionNum = topN_OD_Region[i][1]
            for j in range(7, len(RegionData[RegionNum]), 2):
                # print(j)
                x_arr.append(float(RegionData[RegionNum][j]))
                y_arr.append(float(RegionData[RegionNum][j + 1]))
            plt.fill(x_arr, y_arr, alpha=0.3, color="blue")
            centerX = RegionData[RegionNum][1]
            centerY = RegionData[RegionNum][2]
            plt.scatter(centerX, centerY, color='blue', s=1)
            # plt.annotate(s="D", xy=(centerX, centerY), color='r',weight="ultralight")

        # x_axis = 'Time'  # x轴的文字
        # plt.xlabel(x_axis, font)
        # y_axis = "number"  # y轴的文字
        # plt.ylabel(y_axis, font)
        plt.xticks(fontproperties=font["family"], size=font["size"], weight=font['weight'])
        plt.yticks(fontproperties=font["family"], size=font["size"], weight=font['weight'])
    plt.savefig("pdf/Free2Pub_{}.pdf".format("201812"), bbox_inches='tight')#保存到当前文件下savefile.pdf
    # plt.show()
    # plt.close()
    # exit()



