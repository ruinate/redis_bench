def dict_chunk(dicts, size):
    new_list = []
    dict_len = len(dicts)
    # 获取分组数
    while_count = dict_len // size + 1 if dict_len % size != 0 else dict_len / size
    split_start = 0
    split_end = size
    while while_count > 0:
        # 把字典的键放到列表中，然后根据偏移量拆分字典
        new_list.append([k for k in dicts[split_start:split_end]])
        split_start += size
        split_end += size
        while_count -= 1
    return new_list