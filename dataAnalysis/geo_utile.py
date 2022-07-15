# from math import radians
# from math import cos
# from math import sin
# from math import degrees
# from math import atan2
from math import *

def center_geolocation(geolocations):
    '''
    输入多个经纬度坐标(格式：[[lon1, lat1],[lon2, lat2],....[lonn, latn]])，找出中心点
    :param geolocations:
    :return:中心点坐标  [lon,lat]
    '''
    # 求平均数  同时角度弧度转化 得到中心点
    x = 0  # lon
    y = 0  # lat
    z = 0
    lenth = len(geolocations)
    for lon, lat in geolocations:
        lon = radians(float(lon))
        #  radians(float(lon))   Convert angle x from degrees to radians
        # 	                    把角度 x 从度数转化为 弧度
        lat = radians(float(lat))
        x += cos(lat) * cos(lon)
        y += cos(lat) * sin(lon)
        z += sin(lat)
        x = float(x / lenth)
        y = float(y / lenth)
        z = float(z / lenth)
    return (degrees(atan2(y, x)), degrees(atan2(z, sqrt(x * x + y * y))))


# 得到离中心点里程最近的里程
def geodistance(lon1, lat1, lon2, lat2):
    '''
    得到两个经纬度坐标距离 单位为千米 （计算不分前后顺序）
    :param lon1: 第一个坐标 维度
    :param lat1: 第一个坐标 经度
    :param lon2: 第二个坐标 维度
    :param lat2: 第二个坐标 经度
    :return: distance 单位千米
    '''
    # lon1,lat1,lon2,lat2 = (120.12802999999997,30.28708,115.86572000000001,28.7427)
    lon1, lat1, lon2, lat2 = map(radians, [float(lon1), float(lat1), float(lon2), float(lat2)])  # 经纬度转换成弧度
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    distance = 2 * asin(sqrt(a)) * 6371 * 1000  # 地球平均半径，6371km
    distance = round(distance / 1000, 3)
    print(distance)
    return distance


def getMaxestDistance(geolocations, centre):
    '''
    中心点 距离 多个经纬度左边 最远的距离
    :param geolocations: 多个经纬度坐标(格式：[[lon1, lat1],[lon2, lat2],....[lonn, latn]])
    :param centre: 中心点   centre [lon,lat]
    :return: 最远距离  千米
    '''
    distantces = []
    for lon, lat in geolocations:
        d = geodistance(lat, lon, centre[1], centre[0])
        distantces.append(d)
    # print(distantces)
    return max(distantces)


def getOnePolyygen(geolocations):
    '''
    输入多个经纬度坐标(格式：[[lon1, lat1],[lon2, lat2],....[lonn, latn]])，找出距该多边形中心点最远的距离
    :param geolocations:多个经纬度坐标(格式：[[lon1, lat1],[lon2, lat2],....[lonn, latn]])
    :return:center,neartDistance  多边形中心点  最远距离
    '''
    center = center_geolocation(geolocations)  # 得到中心点
    neartDistance = getMaxestDistance(geolocations, center)
    # print(center,"-----------------",neartDistance)
    return center, neartDistance


 # 获取不规则多边形重心点
 # web:https://www.giserdqy.com/algorithm/4602/
 # @param 输入多个经纬度坐标(格式：[[lon1, lat1],[lon2, lat2],....[lonn, latn]])，找出中心点
 # @return 中心点
def getCenterOfGravityPoint(geolocations):

        area = 0 #多边形面积
        Gx = 0
        Gy = 0 # 重心的x、y
        lenth = len(geolocations)
        for i in range(1,lenth+1,1):
            iLat = geolocations[i%lenth][1]
            iLng = geolocations[i%lenth][0]
            nextLat = geolocations[i-1][1]
            nextLng = geolocations[i-1][0]
            temp = (iLat * nextLng - iLng * nextLat) / 2.0
            area += temp
            Gx += temp * (iLat + nextLat) / 3.0
            Gy += temp * (iLng + nextLng) / 3.0

        Gx = Gx / area
        Gy = Gy / area
        return Gy,Gx


 # 获取不规则多边形中心点,对于凹多边形，可能在边界的外围
 #
 # @param 输入多个经纬度坐标(格式：[[lon1, lat1],[lon2, lat2],....[lonn, latn]])，找出中心点
 # @return 中心点
def getCenterOfCenterPoint(geolocations):

        sumLat = 0
        sumLng = 0
        lenth = len(geolocations)
        for i in range(1,lenth+1,1):
            iLat = geolocations[i%lenth][1]
            iLng = geolocations[i%lenth][0]
            sumLat += iLat
            sumLng += iLng

        Gx = sumLat / lenth
        Gy = sumLng / lenth
        return Gy,Gx


# -*- coding: utf-8 -*-
import json
import math

x_pi = 3.14159265358979324 * 3000.0 / 180.0
pi = 3.1415926535897932384626  # π
a = 6378245.0  # 长半轴
ee = 0.00669342162296594323  # 扁率


def bd09_to_gcj02(bd_lon, bd_lat):
    """
    百度坐标系(BD-09)转火星坐标系(GCJ-02)
    百度——>谷歌、高德
    :param bd_lat:百度坐标纬度
    :param bd_lon:百度坐标经度
    :return:转换后的坐标列表形式
    """
    x = bd_lon - 0.0065
    y = bd_lat - 0.006
    z = math.sqrt(x * x + y * y) - 0.00002 * math.sin(y * x_pi)
    theta = math.atan2(y, x) - 0.000003 * math.cos(x * x_pi)
    gg_lng = z * math.cos(theta)
    gg_lat = z * math.sin(theta)
    return [gg_lng, gg_lat]

def wgs84togcj02(lng, lat):
    """
    WGS84转GCJ02(火星坐标系)
    :param lng:WGS84坐标系的经度
    :param lat:WGS84坐标系的纬度
    :return:
    """
    if out_of_china(lng, lat):  # 判断是否在国内
        return lng, lat
    dlat = transformlat(lng - 105.0, lat - 35.0)
    dlng = transformlng(lng - 105.0, lat - 35.0)
    radlat = lat / 180.0 * pi
    magic = math.sin(radlat)
    magic = 1 - ee * magic * magic
    sqrtmagic = math.sqrt(magic)
    dlat = (dlat * 180.0) / ((a * (1 - ee)) / (magic * sqrtmagic) * pi)
    dlng = (dlng * 180.0) / (a / sqrtmagic * math.cos(radlat) * pi)
    mglat = lat + dlat
    mglng = lng + dlng
    return [mglng, mglat]


def gcj02towgs84(lng, lat):
    """
    GCJ02(火星坐标系)转GPS84
    :param lng:火星坐标系的经度
    :param lat:火星坐标系纬度
    :return:
    """
    if out_of_china(lng, lat):
        return lng, lat
    dlat = transformlat(lng - 105.0, lat - 35.0)
    dlng = transformlng(lng - 105.0, lat - 35.0)
    radlat = lat / 180.0 * pi
    magic = math.sin(radlat)
    magic = 1 - ee * magic * magic
    sqrtmagic = math.sqrt(magic)
    dlat = (dlat * 180.0) / ((a * (1 - ee)) / (magic * sqrtmagic) * pi)
    dlng = (dlng * 180.0) / (a / sqrtmagic * math.cos(radlat) * pi)
    mglat = lat + dlat
    mglng = lng + dlng
    return [lng * 2 - mglng, lat * 2 - mglat]


def bd09_to_wgs84(bd_lon, bd_lat):
    lon, lat = bd09_to_gcj02(bd_lon, bd_lat)
    return gcj02towgs84(lon, lat)

def gcj02_to_bd09(lng, lat):
    """
    火星坐标系(GCJ-02)转百度坐标系(BD-09)
    谷歌、高德——>百度
    :param lng:火星坐标经度
    :param lat:火星坐标纬度
    :return:
    """
    z = math.sqrt(lng * lng + lat * lat) + 0.00002 * math.sin(lat * x_pi)
    theta = math.atan2(lat, lng) + 0.000003 * math.cos(lng * x_pi)
    bd_lng = z * math.cos(theta) + 0.0065
    bd_lat = z * math.sin(theta) + 0.006
    return [bd_lng, bd_lat]

def wgs84_to_bd09(lon, lat):
    lon, lat = wgs84togcj02(lon, lat)
    return gcj02_to_bd09(lon, lat)

def transformlat(lng, lat):
    ret = -100.0 + 2.0 * lng + 3.0 * lat + 0.2 * lat * lat + \
          0.1 * lng * lat + 0.2 * math.sqrt(math.fabs(lng))
    ret += (20.0 * math.sin(6.0 * lng * pi) + 20.0 *
            math.sin(2.0 * lng * pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(lat * pi) + 40.0 *
            math.sin(lat / 3.0 * pi)) * 2.0 / 3.0
    ret += (160.0 * math.sin(lat / 12.0 * pi) + 320 *
            math.sin(lat * pi / 30.0)) * 2.0 / 3.0
    return ret



def transformlng(lng, lat):
    ret = 300.0 + lng + 2.0 * lat + 0.1 * lng * lng + \
          0.1 * lng * lat + 0.1 * math.sqrt(math.fabs(lng))
    ret += (20.0 * math.sin(6.0 * lng * pi) + 20.0 *
            math.sin(2.0 * lng * pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(lng * pi) + 40.0 *
            math.sin(lng / 3.0 * pi)) * 2.0 / 3.0
    ret += (150.0 * math.sin(lng / 12.0 * pi) + 300.0 *
            math.sin(lng / 30.0 * pi)) * 2.0 / 3.0
    return ret


def out_of_china(lng, lat):
    """
    判断是否在国内，不在国内不做偏移
    :param lng:
    :param lat:
    :return:
    """
    if lng < 72.004 or lng > 137.8347:
        return True
    if lat < 0.8293 or lat > 55.8271:
        return True
    return False



if __name__ == '__main__':
    # arr = [114.70656835252136,22.800128052372962,114.70686829867881,22.800909284835573,114.70756217779875,22.80144993449303,114.70826297101088,22.801468563313488,114.70903439987555,22.801360131994322,114.70974364534801,22.800739549117875,114.70983478628997,22.799930803368266,114.70946729153839,22.79904225872199,114.70856503834355,22.798616452223484,114.70746068215287,22.798699781726643,114.70675425858946,22.799107286076868,114.70656835252136,22.800128052372962]
    # print("len: ", len(arr))
    # in_arr = []
    # for i in range(int(len(arr)/2)):
    #     in_arr.append([arr[i*2],arr[i*2+1]])
    # res = center_geolocation(in_arr)
    # print(res[0], res[1])
    # res = getCenterOfCenterPoint(in_arr)
    # print(res[0], res[1])
    # res = getCenterOfGravityPoint(in_arr)
    # print(res[0],res[1])

    # WGS - 84：GPS坐标系
    # GCJ - 02：火星坐标系，国测局02年发布的坐标体系，高德，腾讯等使用。
    # BD - 09：百度坐标系，百度自研，百度地图使用。
    # 22.589892,113.999642(腾讯，高德，谷歌）
    # 113.99965353851252,22.59008223916924 (地铁数据 cat part-m-00000 | grep 塘朗)
    # 113.999462,22.590233(公交数据 cat part-r-00000 | grep 塘朗地铁站)
    # [lng, lat] = [113.999666,22.590097] #SCT行政大楼
    [lng, lat] = [113.890185,22.575738333333334]
    # [dstlng, dstlat] = gcj02towgs84(lng, lat)
    # print(str(dstlng) + "," + str(dstlat))

    [dstlng, dstlat] = gcj02towgs84(lng, lat)
    print(str(dstlng) + "," + str(dstlat))
