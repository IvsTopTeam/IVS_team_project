from our_library import *


def dev():
    num_list = list(map(int, input().split()))      # nacte cisla do listu

    count = len(num_list)                           # N

    sum_std = 0
    for i in range(count):
        sum_std = our_add(sum_std, num_list[i])     # suma vsech cisel v listu

    average = our_div(sum_std, count)               # prumer cisel

    sum_pow = 0
    for i in range(count):
        sum_pow = our_add(sum_pow, our_pow(num_list[i], 2))     # suma vsech (cisel na druhou)

    # vypocet vzorcem pro vyberovou smerodatnou odchylku
    total_help = our_mul(count, our_pow(average, 2))            # N*(avg^2)
    total = our_sqrt(2, our_div(our_sub(sum_pow, total_help), our_sub(count, 1)))

    print(round(total, 3))


dev()