

with open(r"./data/recordsV2.csv", "w", encoding="UTF-8") as fout:
    with open(r"D:\subwayData\mutiOD\testOut\20180401\part-00000", "r", encoding="UTF-8") as fin:
        lines = fin.readlines()
        # print(len(lines))
        for i in range(len(lines)):
            line = lines[i][:-1]
            line_split = line.split("?")
            fout.write(line_split[0] + "\n")
            for i in range(1, len(line_split)):
                if i % 2!=0:
                    fout.write("出行链" + str(int((i - 1)/2) + 1)+ "\n")
                    fout.write(line_split[i]+ "\n")
                else:
                    orgs = line_split[i].split("!")
                    for j in orgs:
                        fout.write(j+ "\n")


