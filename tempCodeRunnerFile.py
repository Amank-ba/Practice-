def count_long_lists(data):
    count = 0
    for i in data:
        if len(i) >= 3:
            count += 1
    return count

print(count_long_lists([[1,2,3], [4,5,6,7], [8], [9,10,11,12,13]]))