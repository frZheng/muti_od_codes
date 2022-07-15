

#hadoop fs -mkdir /user/zhaojuanjuan/zfr_files
#hadoop fs -mkdir /user/zhaojuanjuan/zfr_files/SubwayData
#hadoop fs -mkdir /user/zhaojuanjuan/zfr_files/SubwayDataOut

#hadoop fs -rm -r /user/zhaojuanjuan/zfr_files/SubwayData/*
#hadoop fs -rm -r  .Trash
#hadoop fs -put /parastor/backup/datum/BusOD/SubwayOD /user/zhaojuanjuan/zfr_files/SubwayData/ 
#spark2-submit --master yarn --class SubwayTrip2ToODv2 --num-executors 16 --conf spark.driver.cores=4 --conf spark.driver.memory=4g  --conf spark.executor.cores=8 --conf spark.executor.memory=8g  --conf spark.default.parallelism=1000  --conf spark.shuffle.memoryFraction=0.5 /home/zzhaojuanjuan/zfr_file/jars/firstSparkTest-1.0-SNAPSHOT.jar  /parastor/backup/datum/BusOD/SubwayOD /home/zzhaojuanjuan/zfr_file/SubwayODOut

python3 py/SubwayTrip2ToODv.py >> ./logsubwayTrip2ToODv.txt