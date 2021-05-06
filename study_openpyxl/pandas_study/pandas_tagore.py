#-*-coding:utf-8 -*-
'''
Created on 2019年6月10日

@author: wanghongliang
'''
import pandas as pd
import os

def wrt_and_rt_excel(filepath):
    try:
        #读取csv所有内容
        df = pd.read_csv(filepath,low_memory = False) 
        #根据列名取得想要的列
        pf= df[['Metadata.seq_no','Metadata.Sensor.Gps.positioning_time','Metadata.Sensor.Gps.lat','Metadata.Sensor.Gps.lng','Metadata.Sensor.Gps.quality','Metadata.Sensor.Gps.positioning_status','Metadata.Sensor.Gps.satellite_num','Metadata.Sensor.Gps.pdop','Metadata.Sensor.Gps.direction','Metadata.Sensor.Gps.altitude','Metadata.Sensor.Gps.speed','Metadata.Sensor.Gps.flag','Metadata.Sensor.Speed.speed','Metadata.Sensor.Speed.pulse','Metadata.Sensor.Speed.flag']]
        #去掉全部为空的行
        pf=pf.dropna(how = 'all')
        #重命名表头
        pf.rename(columns={'Metadata.seq_no':'seq_no','Metadata.Sensor.Gps.positioning_time':'positioning_time','Metadata.Sensor.Gps.lat':'lat','Metadata.Sensor.Gps.lng':'lng','Metadata.Sensor.Gps.quality':'quality','Metadata.Sensor.Gps.positioning_status':'status','Metadata.Sensor.Gps.satellite_num':'satellite_num','Metadata.Sensor.Gps.pdop':'pdop','Metadata.Sensor.Gps.direction':'direction','Metadata.Sensor.Gps.altitude':'altitude','Metadata.Sensor.Gps.speed':'Gps.speed','Metadata.Sensor.Gps.flag':'Gps.flag','Metadata.Sensor.Speed.speed':'Speed.speed','Metadata.Sensor.Speed.pulse':'pulse','Metadata.Sensor.Speed.flag':'Speed.flag'},inplace=True)
        #print(pf)
        #获取路径目录
        path = os.path.dirname(filepath)
        #print(path)
        #获取路径文件名
        filename = os.path.basename(filepath)
        filenewname=filename.split('.')
        #print(filenewname)
        #拼接路径
        newpath = os.path.join(path,filenewname[0])
        #print(newpath)
        #存储到excel
        pf.to_excel(newpath +'.xlsx',index=None)
        print('parse done!')
        
    except Exception as err:
        print(err)



wrt_and_rt_excel(r'E:\code\EclipsePython36Workspaces\PythonExcel\pandas_study\120_1_D.csv')















