import os,datetime

# 先在命令行上传文件到HDFS
# 运行程序后输出到HDFS,
# 手动下载到本地

# SubwayDataPath = "/home/parastor/backup/datum/BusOD/SubwayOD"
# hadoopPath = "hdfs://172.169.8.175:8020/user/uc/frzheng/zfr_files"
hadoopPath = "hdfs://172.169.8.175:9000/user/uc/frzheng/zfr_files"
# localPath = "/home/frzheng/zfrFile"
# fileNames = sorted(os.listdir(SubwayDataPath))
startTime = datetime.datetime.strptime("20181201", "%Y%m%d")
endTime = datetime.datetime.strptime("20181231", "%Y%m%d")
curTime = startTime
while curTime <= endTime:
    fileName = curTime.strftime("%Y%m%d")
    curTime = curTime + datetime.timedelta(days=1)
    if "20181201" in fileName:

        cmd = ("spark-submit --master yarn "
               "--class SubwayTrip2ToODv3 "
               # "--num-executors 16 "
               # "--conf spark.driver.cores=4 "
               # "--conf spark.driver.memory=4g  "
               # "--conf spark.executor.cores=8 "
               # "--conf spark.executor.memory=8g  "
               # "--conf spark.default.parallelism=1000  "
               # "--conf spark.shuffle.memoryFraction=0.5 "
               + "/home/frzheng/zfrFile/jars/SparkTest-1.0-SNAPSHOT.jar  "
               + hadoopPath + "/SubwayData/" + fileName + " "
               + hadoopPath + "/SubwayDataOut/" + fileName + " "
               )
        print(cmd)
        # os.system(cmd)


