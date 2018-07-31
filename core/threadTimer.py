#coding=utf-8
import threading
import time
import sys

def heart_beat(func, param, isRunning=True):
    # print time.strftime('%Y-%m-%d %H:%M:%S')
    if isRunning:
        func(getCurTime(), param)
        # print( getCurTime(), param)
        threading.Timer(0.016, heart_beat, (func,getCurTime())).start()

# def setAA():


def getCurTime():
	return int(round(time.time() * 1000))
# def printF(param1, param2):
# 	print(" wcs ", param1, param2)
# # 	pass
# heart_beat(printF,getCurTime())
# # print("count:")