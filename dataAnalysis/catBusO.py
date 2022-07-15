import os
path = r"/home/parastor/backup/datum/BusOD/BusO/20180401"
fileNames = sorted(os.listdir(path))
print(fileNames)
id = "326612033"
for fileName in fileNames:
    if not "part-r-00" in fileName: continue
    absFileName = os.path.join(path,fileName)
    print(fileName)
    with open(absFileName,"r",encoding="UTF-8") as fin:
        lines = fin.readlines()
        for line in lines:
           if id in lines:
               print(line[:-1])

