# Задача №3
import os


def sum_files(file1, file2, file3):
    dict = {}
    dic_str = {}

    with open(file1, 'r', encoding='utf-8') as f:
        data_1 = f.readlines()
    dict[file1] = len(data_1)
    dic_str[file1] = ''.join(data_1)

    with open(file2, 'r', encoding='utf-8') as f:
        data_2 = f.readlines()
    dict[file2] = len(data_2)
    dic_str[file2] = ''.join(data_2)

    with open(file3, 'r', encoding='utf-8') as f:
        data_3 = f.readlines()
    dict[file3] = len(data_3)
    dic_str[file3] = ''.join(data_3)

    sorted_dict = {}
    sorted_keys = sorted(dict, key=dict.get)
    for i in sorted_keys:
        sorted_dict[i] = dict[i]

    with open('files/sorted/summ.txt', 'a', encoding='utf-8') as f:
        for i, j in enumerate(sorted_keys):
            f.write(j[13:] + '\n')
            f.write(str(sorted_dict[sorted_keys[i]]) + '\n')
            f.write(dic_str[sorted_keys[i]] + '\n')


sum_files('files/sorted/1.txt', 'files/sorted/2.txt', 'files/sorted/3.txt')
