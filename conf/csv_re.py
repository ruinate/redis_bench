# 导入CSV模块
import csv
from log_re import redis_msg
from logging import log
# 1. 创建文件对象（指定文件名，模式，编码方式）
with open("redis_msg.csv", "w", encoding="utf-8", newline="") as f:
    # 2. 基于文件对象构建 csv写入对象
    csv_writer = csv.writer(f)
    # 3. 构建列表头
    csv_writer.writerow(["数据量", "QPS/s","响应时间", "完成时间"])
    # 4. 写入csv文件内容
    for  i in  redis_msg():
            csv_writer.writerow([i[0],i[2],i[3],i[1]])
    print("写入数据成功")
    # 5. 关闭文件
    f.close()