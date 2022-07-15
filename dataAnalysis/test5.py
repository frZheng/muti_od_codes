
import os

fileNames = sorted(os.listdir("./"))
for fileName in fileNames:
    if "2018" in fileName:
        cmd = "rm -r ../" + fileName
        print(cmd)
        os.system(cmd)
        cmd = "mv " + fileName + " ../" + fileName
        print(cmd)
        os.system(cmd)

# SubwayDataPath = "/parastor/backup/datum/BusOD/SubwayOD"
# fileNames = sorted(os.listdir(SubwayDataPath))
# for fileName in fileNames:
#     if "2018" in fileName:
#         print(fileName)
#         cmd = "hadoop fs -rm -r /user/zhaojuanjuan/zfr_files/SubwayData/*"
#         print(cmd)
#         os.system(cmd)
#         cmd = "hadoop fs -rm -r .Trash"
#         print(cmd)
#         os.system(cmd)
#         cmd = "hadoop fs -put /parastor/backup/datum/BusOD/SubwayOD/" + fileName +  " /user/zhaojuanjuan/zfr_files/SubwayData/"+ fileName
#         print(cmd)
#         os.system(cmd)
#
#         cmd = ("spark2-submit --master yarn "
#                           "--class SubwayTrip2ToODv3 "
#                           "--num-executors 16 "
#                           "--conf spark.driver.cores=4 "
#                           "--conf spark.driver.memory=4g  "
#                           "--conf spark.executor.cores=8 "
#                           "--conf spark.executor.memory=8g  "
#                           "--conf spark.default.parallelism=1000  "
#                           "--conf spark.shuffle.memoryFraction=0.5 "
#                           "/home/zzhaojuanjuan/zfr_file/jars/firstSparkTest-1.0-SNAPSHOT.jar  "
#                           "hdfs://compute-5-2:8020/user/zhaojuanjuan/zfr_files/SubwayData/" + fileName + " "
#                           "hdfs://compute-5-2:8020/user/zhaojuanjuan/zfr_files/SubwayDataOut/" + fileName + " "
#                )
#         print(cmd)
#         os.system(cmd)
#         cmd = "hadoop fs -get  /user/zhaojuanjuan/zfr_files/SubwayDataOut/*  /home/zzhaojuanjuan/zfr_file/SubwayODOut/"
#         print(cmd)
#         os.system(cmd)
