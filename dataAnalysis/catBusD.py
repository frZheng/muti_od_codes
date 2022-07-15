import os
path = r"D:\subwayData\mutiOD\BusD\20180401"
pathNames = os.listdir(path)
id = "326612033"
for pathName in pathNames:
    fileName = os.path.join(path,pathName,"withtime\part-r-00000")
    print(fileName)
    with open(fileName,"r",encoding="UTF-8") as fin:
        lines = fin.readlines()
        for line in lines:
           if id in lines:
               print(line[:-1])

