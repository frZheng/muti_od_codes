import numpy as np
import matplotlib.pyplot as plt
import os
import datetime

if __name__ == "__main__":

    # 背景尺寸
    width = 3
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
    date = "2018-12-01"
    # topN_OD_Data_Pub = [[] for i in range(len(topN_OD_Region))]

    StartTime = 6 * 60  # 统计起始时间为6点
    EndtTime = 23 * 60  # 统计起始时间为23点
    TimeSlot = 30  # 统计的时间间隔
    TimeSlotNum = int((EndtTime-StartTime)/TimeSlot)

    topN_OD_Data_Free = np.zeros(shape=[len(topN_OD_Region),TimeSlotNum,TimeSlotNum], dtype=np.int32)

    with open(path + "\TaxiODFlow\\" + date +"\part-00000", "r") as fin:
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
                    topN_OD_Data_Free[j,ot,dt] = passengerNum
                    break
    topN_Ot_Data_Free = np.sum(topN_OD_Data_Free,axis=2) #将下车时间纬度累加后得到，在起点从出发时间出发到终点的人数

    # print(topN_Ot_Data_Pub)
    # exit()
    topN_OD_Data_Pub = np.zeros(shape=[len(topN_OD_Region), TimeSlotNum, TimeSlotNum], dtype=np.int32)
    PubDate = date.replace("-","") # -为分隔符，改为无分隔符
    with open(path + "\odFlow\\" + PubDate +"\part-00000", "r") as fin:
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
    topN_Ot_Data_Pub = np.sum(topN_OD_Data_Pub, axis=2)  # 将下车时间纬度累加后得到，在起点从出发时间出发到终点的人数

    mats = [topN_Ot_Data_Pub,topN_Ot_Data_Free]
    labels = ["Pub", "Taxi"]
    colors = ["orange", "blue"]
    fig = plt.figure(dpi=dpi, figsize=(width, height))

    for i in range(len(topN_OD_Region)):
        plt.subplot(len(topN_OD_Region), 1, 1 + i, frameon=True)
        for j in range(len(labels)):
            y = mats[j][i]
            x = np.linspace(0, y.shape[0],y.shape[0])
            plt.plot(x, y, label=labels[j], color=colors[j])
            plt.legend(prop=font, labelspacing=0.1, borderaxespad=0.1, borderpad=0.1, handletextpad=0.1, frameon=True,
                   loc="best", handlelength=1, ncol=3)


        start_date = datetime.datetime.strptime("6:00", '%H:%M')
        plt.draw()
        x_labels = plt.gca().get_xticklabels()
        date_list = []
        i = 0
        for lab in x_labels:
            text = lab._text
            if i == 0:
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
            i += 1

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

    plt.savefig("pdf/Free2Pub_{}.pdf".format(PubDate), bbox_inches='tight')#保存到当前文件下savefile.pdf
    # plt.show()
    # plt.close()
    # exit()



