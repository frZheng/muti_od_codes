import os,time

SubwayDataPath = "/home/zzhaojuanjuan/zfr_file/tripChaining"
fileNames = sorted(os.listdir(SubwayDataPath))
for fileName in fileNames:
    if "2018" in fileName:
        print(str(time.strftime("\n%Y-%m-%d %H:%M:%S", time.localtime())))
        print(fileName)
        cmd = "hadoop fs -rm -r /user/zhaojuanjuan/zfr_files/tripChaining/*"
        print(cmd)
        os.system(cmd)

        cmd = "hadoop fs -rm -r .Trash"
        print(cmd)
        os.system(cmd)

        cmd = "hadoop fs -put " + SubwayDataPath + "/" + fileName + " /user/zhaojuanjuan/zfr_files/tripChaining/" + fileName
        print(cmd)
        os.system(cmd)

        # hadoop fs -mkdir /user/zhaojuanjuan/zfr_files/inFlow
        # hadoop fs -mkdir /user/zhaojuanjuan/zfr_files/outFlow
        # hadoop fs -mkdir /user/zhaojuanjuan/zfr_files/odFlow
        # hadoop fs -mkdir /user/zhaojuanjuan/zfr_files/szRegionData
        # hadoop fs -put /home/zzhaojuanjuan/zfr_file/szRegionData/sz_points.csv /user/zhaojuanjuan/zfr_files/szRegionData/
        cmd = ("spark2-submit --master yarn "
               "--class Trip2Statistics "
               "--num-executors 16 "
               "--conf spark.driver.cores=4 "
               "--conf spark.driver.memory=4g  "
               "--conf spark.executor.cores=8 "
               "--conf spark.executor.memory=8g  "
               "--conf spark.default.parallelism=1000  "
               "--conf spark.shuffle.memoryFraction=0.5 "
               "/home/zzhaojuanjuan/zfr_file/jars/firstSparkTest-1.0-SNAPSHOT.jar  "
               "hdfs://compute-5-2:8020/user/zhaojuanjuan/zfr_files/tripChaining/" + fileName + " "
               "hdfs://compute-5-2:8020/user/zhaojuanjuan/zfr_files/inFlow/" + fileName + " "
                "hdfs://compute-5-2:8020/user/zhaojuanjuan/zfr_files/outFlow/" + fileName + " "
                "hdfs://compute-5-2:8020/user/zhaojuanjuan/zfr_files/odFlow/" + fileName + " "
               )
        print(cmd)
        os.system(cmd)

        cmd = "rm -rf /home/zzhaojuanjuan/zfr_file/inFlow/" + fileName
        print(cmd)
        os.system(cmd)
        cmd = "rm -rf /home/zzhaojuanjuan/zfr_file/outFlow/" + fileName
        print(cmd)
        os.system(cmd)
        cmd = "rm -rf /home/zzhaojuanjuan/zfr_file/odFlow/" + fileName
        print(cmd)
        os.system(cmd)

        cmd = "hadoop fs -get  /user/zhaojuanjuan/zfr_files/inFlow/*  /home/zzhaojuanjuan/zfr_file/inFlow/"
        print(cmd)
        os.system(cmd)
        cmd = "hadoop fs -get  /user/zhaojuanjuan/zfr_files/outFlow/*  /home/zzhaojuanjuan/zfr_file/outFlow/"
        print(cmd)
        os.system(cmd)
        cmd = "hadoop fs -get  /user/zhaojuanjuan/zfr_files/odFlow/*  /home/zzhaojuanjuan/zfr_file/odFlow/"
        print(cmd)
        os.system(cmd)

        cmd = "hadoop fs -rm -r /user/zhaojuanjuan/zfr_files/inFlow/*"
        print(cmd)
        os.system(cmd)

        cmd = "hadoop fs -rm -r /user/zhaojuanjuan/zfr_files/outFlow/*"
        print(cmd)
        os.system(cmd)

        cmd = "hadoop fs -rm -r /user/zhaojuanjuan/zfr_files/odFlow/*"
        print(cmd)
        os.system(cmd)

        cmd = "hadoop fs -rm -r /user/zhaojuanjuan/zfr_files/tripChaining/*"
        print(cmd)
        os.system(cmd)

        cmd = "hadoop fs -rm -r .Trash"
        print(cmd)
        os.system(cmd)


