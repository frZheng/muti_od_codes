# data = "2018-12-18 00:00:00,粤B4C0N7,121749,1545062175000,1545062402000,15.0,3.38,2.499,6.635,0:0:5,1,ffffffffffffffffffff,0.0,114.12190166666667,22.572741666666666,114.111825,22.587381666666666,269,246"
# data_split = data.split(",")
# for i in range(len(data_split)):
#     print(i,data_split[i])
with open(r"D:\subwayData\mutiOD\TaxiODFlow\20181201\part-00000","r") as fin:
    lines = fin.readlines()
    for line in lines:
        if line[-1] == "\n":
            line = line[:-1]
            line_split = line.split(",")
            if line_split[1] == "93" and line_split[3] == "89":
                print(line)
