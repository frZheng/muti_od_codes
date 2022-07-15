start_index = 0
end_index = 50
import os
path = r"D:\subwayData\mutiOD\testOut"
dirs = os.listdir(path)
with open("out.csv","w",encoding="UTF-8") as fout:
    for dir in dirs:
        print(dir)
        fout.write(dir + "\n")
        with open(path + "\\" + dir +  r"\part-00000","r",encoding="UTF-8") as fin:
        # with open(r"D:\subwayData\mutiOD\SubwayRecordDataTestOut\20180401\part-00000", "r", encoding="UTF-8") as fin:
            lines = fin.readlines()
            # print(len(lines))
            # fout.write(dir + "\n")
            fout.write("最前面50条记录\n")
            for i in range(start_index,end_index):
                # print(lines[i][:-1])
                fout.write(lines[i])
            fout.write("前后50条记录\n")
            # print("\n")
            for i in range(len(lines)-50, len(lines)):
            # for i in range(start_index, len(lines)):
            #     print(lines[i][:-1])
                fout.write(lines[i])
        # print("\n\n")
        fout.write("\n\n")