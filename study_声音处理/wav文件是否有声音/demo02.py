"""
@author: wanghongliang
@file: demo02.py
@time: 2022/3/23 14:04 
"""
import wave
import numpy as np
import math
from scipy.io import wavfile

wav_path = r"D:\Study\python\python3_study\python3_study\study_声音处理\录音\test.wav"

# method 1: absSum
def calVolume(waveData, frameSize, overLap):
    wlen = len(waveData)
    step = frameSize - overLap
    frameNum = int(math.ceil(wlen*1.0/step))
    volume = np.zeros((frameNum,1))
    for i in range(frameNum):
        curFrame = waveData[np.arange(i*step,min(i*step+frameSize,wlen))]
        curFrame = curFrame - np.median(curFrame) # zero-justified
        volume[i] = np.sum(np.abs(curFrame))
    return volume

# method 2: 10 times log10 of square sum
def calVolumeDB(waveData, frameSize, overLap):
    wlen = len(waveData)
    step = frameSize - overLap
    frameNum = int(math.ceil(wlen*1.0/step))
    volume = np.zeros((frameNum,1))
    for i in range(frameNum):
        curFrame = waveData[np.arange(i*step,min(i*step+frameSize,wlen))]
        curFrame = curFrame - np.median(curFrame) # zero-justified
        volume[i] = 10*np.log10(np.sum(curFrame*curFrame))
    return volume

def findIndex(vol,thres):
    l = len(vol)
    ii = 0
    silence_start = False
    index = np.zeros(l,dtype=np.int32)
    for i in range(l-1):
        if((vol[i]-thres)*(vol[i+1]-thres)<0):
            if ii == 0 and vol[i]-thres < 0:
                silence_start = True
            index[ii]=i
            ii = ii+1
    return silence_start, index[0:ii]

def cutMute(strData, frameSize):
    dataNew = None
    waveData = np.frombuffer(strData, dtype=np.int16)
    waveData = waveData*1.0/max(abs(waveData))  # normalization（0.1）

    vol = calVolume(waveData, frameSize, 0)
    #print("vol conteng: %s"%(vol))
    threshold1 = max(vol)*0.10
    threshold2 = min(vol)*10.0
    threshold3 = max(vol)*0.05+min(vol)*5.0
    threshold3 = 1
    silence_start, findex = findIndex(vol,threshold3)
    findex = findex*frameSize*2
    index_num = len(findex)
    #print("findex len: %s, content: %s"%(index_num,findex))
    if index_num == 0:
        dataNew = strData
    elif index_num == 1:
        if silence_start:
            dataNew = strData[findex[0]:]
        else:
            dataNew = strData[:findex[0]]
    else:
        for i in range(0,len(findex)):
            end = findex[i]
            if silence_start:
                if i == 1:
                    start = findex[i - 1]
                    dataNew = strData[int(start):int(end)]
                elif i % 2:
                    start = findex[i - 1]
                    dataNew = dataNew + strData[int(start):int(end)]
                elif i == index_num - 1:
                    start = findex[i]
                    dataNew = dataNew + strData[int(start):]
            else:
                if i == 0:
                    dataNew = strData[:int(end)]
                elif i % 2 == 0:
                    start = findex[i - 1]
                    dataNew = dataNew + strData[int(start):int(end)]
                elif i == index_num - 1:
                    start = findex[i]
                    dataNew = dataNew + strData[int(start):]

    waveNew = np.fromstring(dataNew, dtype=np.int16)
    return waveNew



