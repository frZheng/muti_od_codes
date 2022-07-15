start_index = 0
end_index = 50
import os

with open(r"D:\subwayData\mutiOD\testOut\20180401\part-00000", "r", encoding="UTF-8") as fin:
    lines = fin.readlines()
    print(len(lines))
    # fout.write(dir + "\n")
    # fout.write("最前面50条记录\n")
    for i in range(start_index,end_index):
        print(lines[i][:-1])
        # fout.write(lines[i])
    # fout.write("前后50条记录\n")
    print("\n")
    for i in range(len(lines)-50, len(lines)):
    # for i in range(start_index, len(lines)):
        print(lines[i][:-1])
        # fout.write(lines[i])
# print("\n\n")
# fout.write("\n\n")