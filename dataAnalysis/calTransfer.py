totalOD = 0
totalTrip = 0
transfer = 0

#数据
#(0,2878567)
# (1,214117)
# (2,9142)
# (3,348)
# (4,31)
# (5,3)
# (6,1)
# with open(r"D:\subwayData\mutiOD\countDiffModeNum\20180401-noRandom\part-00000", "r", encoding="UTF-8") as fin:
# with open(r"D:\subwayData\mutiOD\countDiffModeNum\20180401-hasRandom\part-00000", "r", encoding="UTF-8") as fin:
with open(r"D:\subwayData\mutiOD\countDiffModeNum\20180401\part-00000", "r", encoding="UTF-8") as fin:
    lines = fin.readlines()

    for i in range(len(lines)):
        lines[i] = lines[i][1:-2] #去掉回车和括号
        line_split = lines[i].split(",")
        curTransferNum = (int(line_split[1]) * (int(line_split[0]) + 1))
        totalOD += curTransferNum
        totalTrip += int(line_split[1])
    print(totalTrip)
    print(totalOD,"\n")

    for i in range(len(lines)):
        line = lines[i]
        print(line)
    print("\n")
    for i in range(len(lines)):
        line = lines[i]
        # print(line)
        # print(line.split(",")[1])
        line_split = line.split(",")
        curTransferNum = (int(line_split[1]) * (int(line_split[0]) + 1))
        # totalOD += curTransferNum

        if i != 0:
            transfer += curTransferNum
        print(curTransferNum)
        # print(curTransferNum/totalOD)
        # print(int(line_split[1]) / totalTrip)
        # print(i,"totalOD",totalOD)
        # print(i,"transfer",transfer)
    print("\n")
    for i in range(len(lines)):
        line = lines[i]
        # print(line)
        # print(line.split(",")[1])
        line_split = line.split(",")
        curTransferNum = (int(line_split[1]) * (int(line_split[0]) + 1))

        if i != 0:
            transfer += curTransferNum
        print(curTransferNum/totalOD)
    print("\n")
    for i in range(len(lines)):
        line = lines[i]
        # print(line)
        # print(line.split(",")[1])
        line_split = line.split(",")
        curTransferNum = (int(line_split[1]) * (int(line_split[0]) + 1))

        if i != 0:
            transfer += curTransferNum
        print(int(line_split[1]) / totalTrip)

# print("\nresult:")
# print(totalOD)
# print(transfer)
# print(transfer/totalOD)