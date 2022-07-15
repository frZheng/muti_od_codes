start_index = 0
end_index = 50
import os

with open(r"D:\subwayData\mutiOD\testOut\20180401\part-00000", "r", encoding="UTF-8") as fin:
    lines = fin.readlines()
    print(len(lines))

    for i in range(0, len(lines)):
        # if ";" in lines[i]:
        if "\t" in lines[i]:
            print(lines[i][:-1])

        # fout.write(lines[i])
# print("\n\n")
# fout.write("\n\n")