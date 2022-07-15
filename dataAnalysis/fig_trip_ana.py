import numpy as np
import matplotlib.pyplot as plt
import os


if __name__ == "__main__":

    # 背景尺寸
    width = 10.5
    height = 3
    dpi = 1200

    xysize = 13
    size3 = -0.3
    psize = 15

    font = {'family': 'Times New Roman', 'weight': 'bold', 'size': psize}





    path_common = r"data"
    # path_common = r"D:\subwayData\BusD_test"
    file_names_list = sorted(os.listdir(path_common))

    print(file_names_list)

    for file_name in file_names_list:
        npz_file_name = os.path.join(path_common,file_name)
        traval_time_array = np.load(npz_file_name)["matrix"]
        fig = plt.figure(dpi=dpi, figsize=(width, height))
        y = traval_time_array
        x = np.linspace(0-200, y.shape[0]-200,y.shape[0])
        plt.plot(x, y, label="num", color="orange")
        plt.legend(prop=font, labelspacing=0.1, borderaxespad=0.1, borderpad=0.1, handletextpad=0.1, frameon=True,
               loc="best", handlelength=1, ncol=3)



        plt.title("Date " + file_name.split("_")[-2], font)
        # plt.grid(ls='--')
        # plt.ylim(-2, 2) #设置y轴范围,可以不设置

        # plt.xlim(-200, 201)  # 设置y轴范围,可以不设置
        x_axis = 'trip time(second)'# x轴的文字
        plt.xlabel(x_axis, font)
        y_axis = "number"# y轴的文字
        plt.ylabel(y_axis, font)
        plt.xticks(fontproperties=font["family"], size=font["size"], weight=font['weight'])
        plt.yticks(fontproperties=font["family"], size=font["size"], weight=font['weight'])

        plt.savefig("pdf/{}.pdf".format(file_name.split(".")[0]), bbox_inches='tight')#保存到当前文件下savefile.pdf
        plt.close()
        # exit()


