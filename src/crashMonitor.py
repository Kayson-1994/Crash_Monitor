#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : crashMonitor.py
@Author: Excellent Shen
@Date  : 19-3-27 上午8:01
@Desc  :
"""
import threading  # 线程模块
import time

g_obj = None


def start_service():
    global g_obj
    g_obj = Monitor()
    print("g_obj is {0}".format(g_obj))
    g_obj.start_monitor()


def stop_service():
    global g_obj
    if g_obj is not None:
        g_obj.stop_monitor()


class Monitor(object):
    def __init__(self):
        self.g_flag = True

    def start(self):  # 定义每个线程要运行的函数
        while self.g_flag:
            print('g_flag in start is {0}'.format(self.g_flag))
            time.sleep(3)

    def stop(self):
        for n in range(2):
            print("g_flag in stop is {0}".format(self.g_flag))
            n += 1

        self.g_flag = False
        print("g_flag is {}".format(self.g_flag))

    def start_monitor(self):
        print("start_service")
        t1 = threading.Thread(target=self.start)
        t1.start()  # 启动线程

    def stop_monitor(self):
        self.stop()
