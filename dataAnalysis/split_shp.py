import os, shapefile, shutil

if __name__ == '__main__':
    path = r"D:\subwayData\csjs_tools\map\sects"
    mapBasePolyShpFile = os.path.join(path,"sects.shp")
    # 目标文件 夹 存放地址
    folderPolyAimMap = r'D:\subwayData\csjs_tools\map\sub_sects'
    # 原文件的投影地址
    projectionFile = os.path.join(path,"sects.prj")

    print('Start...')
    rPolyShp = shapefile.Reader(mapBasePolyShpFile)
    for numFlag in range(rPolyShp.numRecords):
        fileName = f'1_3_{numFlag + 1}'
        # 目标Shp文件地址
        aimPolyMap = fr'{folderPolyAimMap}\{fileName}.shp'
        wPolyShp = shapefile.Writer(target=aimPolyMap, shapeType=5)
        # 添加名为'Size'的浮点型，6位有效，2位小数点的字段
        wPolyShp.field('Size', 'F', 6, 2)

        # 读取原文件第一个要素的线点集
        # 添加异常处理，以防存在空Shp文件
        try:
            baseLinkPoint = [[list(i) for i in rPolyShp.shape(numFlag).points]]
        except IndexError:
            shutil.copy(projectionFile, f'{aimPolyMap[:-4]}.prj')
            continue
        # 将线点集写入到面点击中
        wPolyShp.poly(baseLinkPoint)

        # 写入面积信息
        wPolyShp.record(shapefile.signed_area(rPolyShp.shape(numFlag).points))

        # 关闭写文件
        wPolyShp.close()
        # 这里偷懒，已知'.shp'这个字符串的len
        shutil.copy(projectionFile, f'{aimPolyMap[:-4]}.prj')
        print(numFlag, '已经完成')
    print('End...')


