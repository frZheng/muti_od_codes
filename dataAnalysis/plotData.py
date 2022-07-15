import numpy as np
import matplotlib.pyplot as plt
import os
import datetime

def get_flow_data(path = r"D:\subwayData\mutiOD\inFlow\20180401\part-00000"):
    # data = []

    matrix = np.zeros(shape=[int((23 - 6) * 60 / 30), 2047, 1], dtype=np.int32)
    with open(path,"r") as fin:
        lines = fin.readlines()
        for line in lines:
            if line[-1] == "\n":
                line = line[:-1]
                line_splits = line.split(",")
                one_data = []
                for val in line_splits:
                    one_data.append(int(val))
                matrix[one_data[0],one_data[1],0] = one_data[2]
                # data.append(one_data)
    # data.sort(key=lambda x:x[2],reverse=True)
    # np_data = np.array(data)
    # data.sort(key=lambda x: x[2], reverse=False)
    # print(np_data)
    # np_data
    return matrix
# get_in_flow_data()
# exit()
if __name__ == "__main__":

    # 背景尺寸
    width = 10.5
    height = 3
    dpi = 1200

    xysize = 13
    size3 = -0.3
    psize = 15

    font = {'family': 'Times New Roman', 'weight': 'bold', 'size': psize}

    in_mat = get_flow_data()
    out_mat = get_flow_data(r"D:\subwayData\mutiOD\outFlow\20180401\part-00000")
    mats = [in_mat,out_mat]
    labels = ["In", "Out"]
    colors = ["orange", "blue"]
    fig = plt.figure(dpi=dpi, figsize=(width, height))
    region = 194
    # region = 1769
    for i in range(len(mats)):
        y = mats[i][:,region,0]
        x = np.linspace(0, y.shape[0],y.shape[0])
        plt.plot(x, y, label=labels[i], color=colors[i])
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

    plt.title("Flow Ana Region " + str(region), font)
    # plt.grid(ls='--')
    # plt.ylim(-2, 2) #设置y轴范围,可以不设置

    # plt.xlim(-200, 201)  # 设置y轴范围,可以不设置
    x_axis = 'Time'# x轴的文字
    plt.xlabel(x_axis, font)
    y_axis = "number"# y轴的文字
    plt.ylabel(y_axis, font)
    plt.xticks(fontproperties=font["family"], size=font["size"], weight=font['weight'])
    plt.yticks(fontproperties=font["family"], size=font["size"], weight=font['weight'])

    # plt.savefig("pdf/{}.pdf".format(file_name.split(".")[0]), bbox_inches='tight')#保存到当前文件下savefile.pdf
    plt.show()
    # plt.close()
    # exit()



