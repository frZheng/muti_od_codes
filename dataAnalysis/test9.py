import os, time
import shutil
TaxiDataPath = "D:/subwayData/mutiOD/taxiData"
fileNames = sorted(os.listdir(TaxiDataPath))

def del_dir(path):
  try:
    shutil.rmtree(path)
  except OSError as e:
    print("Error: %s - %s." % (e.filename, e.strerror))

for fileName in fileNames:
    if "2018-12-01" in fileName:
        print(str(time.strftime("\n%Y-%m-%d %H:%M:%S", time.localtime())))

        # print(fileName)
        # cmd = "hadoop fs -rm -r /user/zhaojuanjuan/zfr_files/taxiData/*"
        # print(cmd)
        # os.system(cmd)
        #
        # cmd = "hadoop fs -rm -r .Trash"
        # print(cmd)
        # os.system(cmd)

        # cmd = "hadoop fs -put " + TaxiDataPath + "/" + fileName + " /user/zhaojuanjuan/zfr_files/taxiData/" + fileName
        # print(cmd)
        # os.system(cmd)

        TaxiInFlow = "D:/subwayData/mutiOD/TaxiInFlow/" + fileName
        del_dir(TaxiInFlow)
        TaxiOutFlow = "D:/subwayData/mutiOD/TaxiOutFlow/" + fileName
        TaxiODFlow = "D:/subwayData/mutiOD/TaxiODFlow/" + fileName
        del_dir(TaxiOutFlow)
        del_dir(TaxiODFlow)
        cmd = ("spark-submit --master local "
               "--class Taxi2Statistics "
               # "--num-executors 16 "
               # "--conf spark.driver.cores=4 "
               # "--conf spark.driver.memory=4g  "
               # "--conf spark.executor.cores=8 "
               # "--conf spark.executor.memory=8g  "
               # "--conf spark.default.parallelism=1000  "
               # "--conf spark.shuffle.memoryFraction=0.5 "
               "/D:/subwayData/spark/code/firstSparkTest/target/firstSparkTest-1.0-SNAPSHOT.jar  "
               + TaxiDataPath + "/" + fileName + "/" + fileName + "_0 "  # 绝对路径
               + TaxiInFlow + " "
               + TaxiOutFlow + " "
               + TaxiODFlow + " "
               + "D:/subwayData/mutiOD/szRegionData" + " "
               + "null "
               )
        print(cmd)
        # smd_split = cmd.split(" ")
        # for k in smd_split:
        #   print(k)
        os.system(cmd)

        # cmd = "rm -rf /home/zzhaojuanjuan/zfr_file/TaxiInFlow/" + fileName
        # print(cmd)
        # os.system(cmd)
        # cmd = "rm -rf /home/zzhaojuanjuan/zfr_file/TaxiOutFlow/" + fileName
        # print(cmd)
        # os.system(cmd)
        # cmd = "rm -rf /home/zzhaojuanjuan/zfr_file/TaxiODFlow/" + fileName
        # print(cmd)
        # os.system(cmd)

        # cmd = "hadoop fs -get  /user/zhaojuanjuan/zfr_files/TaxiInFlow/*  /home/zzhaojuanjuan/zfr_file/TaxiInFlow/"
        # print(cmd)
        # os.system(cmd)
        # cmd = "hadoop fs -get  /user/zhaojuanjuan/zfr_files/TaxiOutFlow/*  /home/zzhaojuanjuan/zfr_file/TaxiOutFlow/"
        # print(cmd)
        # os.system(cmd)
        # cmd = "hadoop fs -get  /user/zhaojuanjuan/zfr_files/TaxiODFlow/*  /home/zzhaojuanjuan/zfr_file/TaxiODFlow/"
        # print(cmd)
        # os.system(cmd)
        #
        # cmd = "hadoop fs -rm -r /user/zhaojuanjuan/zfr_files/TaxiInFlow/*"
        # print(cmd)
        # os.system(cmd)
        #
        # cmd = "hadoop fs -rm -r /user/zhaojuanjuan/zfr_files/TaxiOutFlow/*"
        # print(cmd)
        # os.system(cmd)
        #
        # cmd = "hadoop fs -rm -r /user/zhaojuanjuan/zfr_files/TaxiODFlow/*"
        # print(cmd)
        # os.system(cmd)
        #
        # cmd = "hadoop fs -rm -r /user/zhaojuanjuan/zfr_files/taxiData/*"
        # print(cmd)
        # os.system(cmd)
        #
        # cmd = "hadoop fs -rm -r .Trash"
        # print(cmd)
        # os.system(cmd)


