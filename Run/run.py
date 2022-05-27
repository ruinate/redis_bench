from conf.log_re import redis
from conf.group_ import dict_chunk
import csv


# 解析数据进行分组
def group_redis():
    redis_sum = []
    for i, j, k in zip(redis().qps(), redis().Retime(), redis().time()):
        c = [i, j, k]
        redis_sum.append(c)
    res = dict_chunk(redis_sum, 4)
    # 按照4个进行分组
    redis_bench = []
    redis_bench_P = []
    for k, v in enumerate(res):
        if k % 2 == 1:
            redis_bench_P.append(v)
        else:
            redis_bench.append(v)
    # 按照12个进行分组
    redis_msg_ = []
    redis_msg_P = []
    # 数据
    for i in redis_bench:
        for j in i:
            for k in j:
                redis_msg_.append(k)
    redis_msg_ = dict_chunk(redis_msg_, 12)
    # 开启管道传输数据
    for i in redis_bench_P:
        for j in i:
            for k in j:
                redis_msg_P.append(k)
    redis_msg_P = dict_chunk(redis_msg_P, 12)
    redis_msg_sum = [redis_msg_,redis_msg_P]
    return redis_msg_sum


def run_csv(filename,msg):
    header = []
    for j in range(1, 91):
        header.append(j)
    with open(filename, 'w', newline='') as cf:
        csvfile = csv.writer(cf)
        # 表头写入
        csvfile.writerow(header)
        for column in zip(*[i for i in msg]):
            # 数据写入
            csvfile.writerow(column)
    cf.close()


if __name__ == '__main__':
    run_csv('redis_P.csv',group_redis()[1])
