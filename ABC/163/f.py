import random
from math import log2
import sys, re, os
from collections import deque, defaultdict, Counter


result_num = 5
for i in range(result_num):
    # two
    counter = 10000
    entropy = []
    ans = 0
    p = [0] * 2
    for i in range(counter):
        l = [random.randint(0, 1) for i in range(128)]
        ratio = [0] * 2
        one_num = sum(l)
        ratio[0], ratio[1] = 128 - one_num, one_num
        p[0], p[1] = ratio[0] / 128, ratio[1] / 128    
        ans = p[0] * log2(1/p[0]) + p[1] * log2(1/p[1])
        entropy.append(ans)
    a = sum(entropy)/counter

    # four 64
    # p_list = []
    times = 64
    entropy = []
    for i in range(counter):
        l = [random.randint(0, 3) for i in range(times)]
        num_dic = Counter(l)
        # print(num_dic)
        ans = 0
        for num in num_dic.values():
            p = num/times
            # p_list.append(entropy)
            ans += p * log2(1/p)
        entropy.append(ans)
    b = sum(entropy)/counter

    # eight 32
    times = 32
    entropy = []
    for i in range(counter):
        l = [random.randint(0, 15) for i in range(times)]
        num_dic = Counter(l)
        # print(num_dic)
        ans = 0
        for num in num_dic.values():
            p = num/times
            # p_list.append(entropy)
            ans += p * log2(1/p)
        entropy.append(ans)
    c = sum(entropy)/counter
    print(a, b, c)