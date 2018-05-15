#!/usr/bin/python

import psutil
import sys
import math


def printMetrics(param):
    if param == "cpu":
        print("======== CPU METRICS ========")
        metrics = psutil.cpu_times()
        for metric in metrics._fields:
            print("system.cpu.{} : {} {}".format(metric, getattr(metrics, metric), "sec"))
    else:
        print("======== MEMORY METRICS ========")
        metrics = psutil.virtual_memory()
        swapped_mem = psutil.swap_memory()
        for metric in metrics._fields:
            print("{} : {}".format(metric, convert_size(getattr(metrics, metric))))

        for metric in swapped_mem._fields:
            print("swap {} : {}".format(metric, convert_size(getattr(swapped_mem, metric))))


def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])


if __name__ == "__main__":
    if len(sys.argv) == 1 or len(sys.argv) > 2:
        raise Exception("{} requires 1 argument - cpu or mem".format(sys.argv[0]))
    elif sys.argv[1] != "cpu" and sys.argv[1] != "mem":
        raise Exception("{}: illegal option --{}".format(sys.argv[0], sys.argv[1]))
    else:
        printMetrics(sys.argv[1])
















