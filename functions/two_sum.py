def two_sum(list, target):
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if list[j] == target - list[i]:
                return [i, j]
