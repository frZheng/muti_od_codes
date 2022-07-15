import os,time,datetime

SubwayDataPath = "/home/zzhaojuanjuan/zfr_file/SubwayODOut"
BusDataPath = "/parastor/backup/datum/BusOD/BusD"
HomeAndWorkPath = "/parastor/backup/datum/BusOD/HomeAndWork/Month"

# fileNames = sorted(os.listdir(SubwayDataPath))
startTime = datetime.datetime.strptime("20181201", "%Y%m%d")
endTime = datetime.datetime.strptime("20181231", "%Y%m%d")
# print(startTime)
# print(endTime > startTime)
# print(endTime.date() - startTime.date())
# exit()
# startTime = datetime.timedelta(days=1)
# datetime.timedelta(days=1)

curTime = startTime
# date = curTime.strftime("%Y%m%d")
# print(date)
# exit()
while curTime <= endTime:
    fileName = curTime.strftime("%Y%m%d")
    curTime = curTime + datetime.timedelta(days=1)
    if "20181201" in fileName:
        print(str(time.strftime("\n%Y-%m-%d %H:%M:%S", time.localtime())))
        print(fileName)
        cmd = "hadoop fs -rm -r /user/zhaojuanjuan/zfr_files/subwayODData/*"
        print(cmd)
        # os.system(cmd)

        cmd = "hadoop fs -rm -r .Trash"
        print(cmd)
        # os.system(cmd)

        cmd = "hadoop fs -put " + SubwayDataPath + "/" + fileName + " /user/zhaojuanjuan/zfr_files/subwayODData/" + fileName
        print(cmd)
        # os.system(cmd)

        cmd = "hadoop fs -put " + BusDataPath + "/" + fileName + " /user/zhaojuanjuan/zfr_files/BusOD/" + fileName
        print(cmd)
        # os.system(cmd)

        cmd = "hadoop fs -put " + HomeAndWorkPath + "/" + fileName + " /user/zhaojuanjuan/zfr_files/HomeAndWorkPath/" + fileName
        print(cmd)
        # os.system(cmd)

        # hadoop fs -mkdir /user/zhaojuanjuan/zfr_files/subwayODData
        # hadoop fs -put /home/zzhaojuanjuan/zfr_file/szRegionData/sz_points.csv /user/zhaojuanjuan/zfr_files/szRegionData/
        cmd = ("spark2-submit --master yarn "
               "--class TripChaining2ODv8 "
               "--num-executors 16 "
               "--conf spark.driver.cores=4 "
               "--conf spark.driver.memory=4g  "
               "--conf spark.executor.cores=8 "
               "--conf spark.executor.memory=8g  "
               "--conf spark.default.parallelism=1000  "
               "--conf spark.shuffle.memoryFraction=0.5 "
               "/home/zzhaojuanjuan/zfr_file/jars/firstSparkTest-1.0-SNAPSHOT.jar  "
               # "hdfs://compute-5-2:8020/user/zhaojuanjuan/zfr_files/tripChaining/" + fileName + " "
               # "hdfs://compute-5-2:8020/user/zhaojuanjuan/zfr_files/inFlow/" + fileName + " "
               #  "hdfs://compute-5-2:8020/user/zhaojuanjuan/zfr_files/outFlow/" + fileName + " "
               #  "hdfs://compute-5-2:8020/user/zhaojuanjuan/zfr_files/odFlow/" + fileName + " "
               )

        if os.path.isdir(BusDataPath + "/" + fileName):
            print("文件夹存在")
            if os.path.isdir(BusDataPath + "/" + fileName + "/common") and os.path.isfile(BusDataPath + "/" + fileName + "/common/withtime/part-r-00000"):
                cmd += "hdfs://compute-5-2:8020/user/zhaojuanjuan/zfr_files/BusOD/" + fileName + "/common "
                print("common 存在")
            else:
                cmd += "null "
                print("common 不存在")

            if os.path.isdir(BusDataPath + "/" + fileName + "/last") and os.path.isfile(BusDataPath + "/" + fileName + "/last/withtime/part-r-00000"):
                cmd += "hdfs://compute-5-2:8020/user/zhaojuanjuan/zfr_files/BusOD/" + fileName + "/last "
                print("last 存在")
            else:
                cmd += "null "
                print("last 不存在")

            if os.path.isdir(BusDataPath + "/" + fileName + "/passengerflow") and os.path.isfile(BusDataPath + "/" + fileName + "/passengerflow/withtime/part-r-00000"):
                cmd += "hdfs://compute-5-2:8020/user/zhaojuanjuan/zfr_files/BusOD/" + fileName + "/passengerflow "
                print("passengerflow 存在")
            else:
                cmd += "null "
                print("passengerflow 不存在")

            # if os.path.isdir(BusDataPath + "/" + fileName + "/random") and os.path.isfile(BusDataPath + "/" + fileName + "/random/withtime/part-r-00000"):
            #     cmd += "hdfs://compute-5-2:8020/user/zhaojuanjuan/zfr_files/BusOD/" + fileName + "/random "
            #     print("random 存在")
            # else:
            #     cmd += "null "
            #     print("random 不存在")
            cmd += "null " # 直接不要random

            if os.path.isdir(BusDataPath + "/" + fileName + "/stationflow") and os.path.isfile(BusDataPath + "/" + fileName + "/stationflow/withtime/part-r-00000"):
                cmd += "hdfs://compute-5-2:8020/user/zhaojuanjuan/zfr_files/BusOD/" + fileName + "/stationflow "
                print("stationflow 存在")
            else:
                cmd += "null "
                print("stationflow 不存在")


        else:
            cmd += "null " # common
            cmd += "null " # last
            cmd += "null " # passengerflow
            cmd += "null " # random
            cmd += "null " # stationflow
            print("文件夹不存在")
        if os.path.isdir(SubwayDataPath + "/" + fileName) and os.path.isfile(
                SubwayDataPath + "/" + fileName + "/part-00000"):
            cmd += "hdfs://compute-5-2:8020/user/zhaojuanjuan/zfr_files/subwayODData/" + fileName
            print("SubwayDataPath 存在")
        else:
            cmd += "null "
            print("SubwayDataPath 不存在")

        if os.path.isdir(HomeAndWorkPath + "/" + fileName):
            if os.path.isdir(HomeAndWorkPath + "/" + fileName + "/Home") and os.path.isfile(
                    HomeAndWorkPath + "/" + fileName + "/Home/part-r-00000"):
                cmd += "hdfs://compute-5-2:8020/user/zhaojuanjuan/zfr_files/HomeAndWork/" + fileName + "/Home/part-r-00000 "
                print("Home 存在")
            else:
                cmd += "null "
                print("Home 不存在")
            if os.path.isdir(HomeAndWorkPath + "/" + fileName + "/Work") and os.path.isfile(
                    HomeAndWorkPath + "/" + fileName + "/Work/part-r-00000"):
                cmd += "hdfs://compute-5-2:8020/user/zhaojuanjuan/zfr_files/HomeAndWork/" + fileName + "/Work/part-r-00000 "
                print("Work 存在")
            else:
                cmd += "null "
                print("Work 不存在")
        else:
            print("HomeAndWorkPath 不存在")
            cmd += "null "
            cmd += "null "
        cmd += "hdfs://compute-5-2:8020/user/zhaojuanjuan/zfr_files/tripChaining/" + fileName + " "
        print(cmd)
        # os.system(cmd)

        cmd = "rm -rf /home/zzhaojuanjuan/zfr_file/tripChaining/" + fileName
        print(cmd)
        # os.system(cmd)

        cmd = "hadoop fs -get  /user/zhaojuanjuan/zfr_files/tripChaining/*  /home/zzhaojuanjuan/zfr_file/tripChaining/"
        print(cmd)
        # os.system(cmd)

        cmd = "hadoop fs -rm -r /user/zhaojuanjuan/zfr_files/tripChaining/*"
        print(cmd)
        # os.system(cmd)


        cmd = "hadoop fs -rm -r /user/zhaojuanjuan/zfr_files/subwayODData/*"
        print(cmd)
        # os.system(cmd)

        cmd = "hadoop fs -rm -r /user/zhaojuanjuan/zfr_files/BusOD/*"
        print(cmd)
        # os.system(cmd)

        cmd = "hadoop fs -rm -r /user/zhaojuanjuan/zfr_files/HomeAndWork/*"
        print(cmd)
        # os.system(cmd)

        cmd = "hadoop fs -rm -r .Trash"
        print(cmd)
        # os.system(cmd)



