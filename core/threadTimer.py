#coding=utf-8
import threading
import time
import sys

exec_count = 0

def heart_beat(func, param):
    # print time.strftime('%Y-%m-%d %H:%M:%S')
    func(getCurTime(), param)
    # print( getCurTime(), param)
    threading.Timer(0.016, heart_beat, (func,getCurTime())).start()

def getCurTime():
	return int(round(time.time() * 1000))
# def printF(param1, param2):
# 	print(" wcs ", param1, param2)
# # 	pass
# heart_beat(printF,getCurTime())
# print("count:")