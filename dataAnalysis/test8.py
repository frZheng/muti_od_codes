import os, time

TaxiDataPath = "/home/parastor/backup/data/SZTaxi/data/business"
hadoopPath = "/user/uc/frzheng/zfr_files"
localPath = "/home/frzheng/zfrFile"
fileNames = sorted(os.listdir(TaxiDataPath))
for fileName in fileNames:
    if "2018-12-01" in fileName:
        print(str(time.strftime("\n%Y-%m-%d %H:%M:%S", time.localtime())))
        print(fileName)
        cmd = "hadoop fs -rm -r " + hadoopPath + "/taxiData/*"
        print(cmd)
        os.system(cmd)

        cmd = "hadoop fs -rm -r .Trash"
        print(cmd)
        os.system(cmd)

        cmd = "hadoop fs -put " + TaxiDataPath + "/" + fileName + " " + hadoopPath+ "/taxiData/" + fileName
        print(cmd)
        os.system(cmd)

        # cd /home/parastor/backup/data
        # scp -P 22 -r zhaojuanjuan@172.16.4.102:/parastor/backup/data/SZTaxi/ ./
        # hadoop fs -mkdir /user/zhaojuanjuan/zfr_files/taxiData
        # hadoop fs -mkdir /user/zhaojuanjuan/zfr_files/TaxiOutFlow
        # hadoop fs -mkdir /user/zhaojuanjuan/zfr_files/TaxiODFlow
        # hadoop fs -mkdir /user/zhaojuanjuan/zfr_files/szRegionData
        # hadoop fs -put /home/zzhaojuanjuan/zfr_file/szRegionData/sz_points.csv /user/zhaojuanjuan/zfr_files/szRegionData/

        # hadoop fs -mkdir /user/uc/frzheng/zfr_files/taxiData
        # hadoop fs -mkdir /user/uc/frzheng/zfr_files/TaxiOutFlow
        # hadoop fs -mkdir /user/uc/frzheng/zfr_files/TaxiODFlow
        # hadoop fs -mkdir /user/uc/frzheng/zfr_files/szRegionData
        # hadoop fs -mkdir /user/uc/frzheng/zfr_files/jars
        # hadoop fs -put /home/frzheng/zfrFile/szRegionData/sz_points.csv /user/uc/frzheng/zfr_files/szRegionData/
        cmd = ("spark2-submit --master yarn "
               "--class Taxi2Statistics "
               "--num-executors 16 "
               "--conf spark.driver.cores=4 "
               "--conf spark.driver.memory=4g  "
               "--conf spark.executor.cores=8 "
               "--conf spark.executor.memory=8g  "
               "--conf spark.default.parallelism=1000  "
               "--conf spark.shuffle.memoryFraction=0.5 "
              + hadoopPath + "/jars/firstSparkTest-1.0-SNAPSHOT.jar  "
              + hadoopPath + "/taxiData/" + fileName + "/" + fileName + "_0 "  # 绝对路径
              + hadoopPath + "/TaxiInFlow/" + fileName + " "
              + hadoopPath + "/TaxiOutFlow/" + fileName + " "                                                                                                                                                                                                                                                     
              + hadoopPath + "/TaxiODFlow/" + fileName + " "
               )
        print(cmd)
        os.system(cmd)

        cmd = "rm -rf " + hadoopPath + "/TaxiInFlow/" + fileName
        print(cmd)
        os.system(cmd)
        cmd = "rm -rf " + hadoopPath +"/TaxiOutFlow/" + fileName
        print(cmd)
        os.system(cmd)
        cmd = "rm -rf " + hadoopPath +"/TaxiODFlow/" + fileName
        print(cmd)
        os.system(cmd)

        cmd = "hadoop fs -get  " + hadoopPath +"/TaxiInFlow/*  " + localPath + "/TaxiInFlow/"
        print(cmd)
        os.system(cmd)
        cmd = "hadoop fs -get  " + hadoopPath +"/TaxiOutFlow/* " + localPath + "/TaxiOutFlow/"
        print(cmd)
        os.system(cmd)
        cmd = "hadoop fs -get  " + hadoopPath +"/TaxiODFlow/*  " + localPath + "/TaxiODFlow/"
        print(cmd)
        os.system(cmd)

        cmd = "hadoop fs -rm -r " + hadoopPath +"/TaxiInFlow/*"
        print(cmd)
        os.system(cmd)

        cmd = "hadoop fs -rm -r " + hadoopPath +"/TaxiOutFlow/*"
        print(cmd)
        os.system(cmd)

        cmd = "hadoop fs -rm -r " + hadoopPath +"/TaxiODFlow/*"
        print(cmd)
        os.system(cmd)

        cmd = "hadoop fs -rm -r " + hadoopPath +"/taxiData/*"
        print(cmd)
        os.system(cmd)

        cmd = "hadoop fs -rm -r .Trash"
        print(cmd)
        os.system(cmd)


