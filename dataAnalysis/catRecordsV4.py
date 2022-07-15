

with open(r"./data/recordsV2.csv", "w", encoding="UTF-8") as fout:
    with open(r"D:\subwayData\mutiOD\testOut\20180401\part-00000", "r", encoding="UTF-8") as fin:
        lines = fin.readlines()
        # print(len(lines))
        # print(len(lines[0].split(",")))
        for i in range(len(lines)):
            line = lines[i][:-1]
            line_split = line.split(",")

            # fout.write(line_split[0] + "\n")
            for j in range(0, 14):
                fout.write(line_split[j] + ",")
            fout.write("\n换乘站点序列\n")
            tmp = line_split[14].split("\t")
            for j in tmp:
                fout.write(j + "?\n")

            fout.write("原始记录\n")
            tmp = line_split[15].split("\t")
            for j in tmp:
                fout.write(j + "?\n")

            fout.write("\n")



