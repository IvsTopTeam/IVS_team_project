from our_library import *


def main():
    num_list = list(map(int, input().split()))
    sum_std = 0
    count = len(num_list)

    for i in range(count):
        sum_std = our_add(sum_std, num_list[i])

    average = our_div(sum_std, count)

    sum_tot = 0
    help_num = our_mul(count, our_pow(average, 2))
    for i in range(count):
        sum_tot = our_add(sum_tot, our_sub(our_pow(num_list[i], 2), help_num))

    total = our_sqrt(2, our_div(sum_tot, our_sub(count, 1)))
    print(total)


if __name__ == "__main__":
    main()