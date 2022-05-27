import os
import json
import re


class redis:
    def __init__(self):
        path = os.path.abspath(os.path.join(os.getcwd(),os.path.pardir))
        path_re = path + '\\data\\redis.log'
        self.qps_msg = []
        self.time_msg = []
        self.retime_msg = []
        self.file_r = open(path_re, "r", encoding='UTF-8')

    def time(self):
        for line in self.file_r:
            redis_log = (json.dumps(line))
            if 'requests completed in' in redis_log:
                number = re.findall('-?\d+.?\d+', redis_log)
                # b = number[1] + '/s'
                self.time_msg.append(number[1])
        return self.time_msg

    def qps(self):
        for line in self.file_r:
            redis_log = (json.dumps(line))
            if 'requests per second' in redis_log:
                number = re.findall('-?\d+.?\d+', redis_log)
                # print(number)
                self.qps_msg.append(number[0])
        return self.qps_msg

    def Retime(self):
        list_1 = []
        for line in self.file_r:
            redis_log = (json.dumps(line))
            list_1.append(line)
        b = []
        mill = []
        for i, j in enumerate(list_1):
            if 'requests per second' in j:
                b.append(i - 1)
        # print(b)
        for i in b:
            mill.append(list_1[i])
        for j in mill:
            number_2 = re.findall('\d+', j)
            self.retime_msg.append(number_2[2])
        # print(len(mill))
        return self.retime_msg


Redis = redis()



