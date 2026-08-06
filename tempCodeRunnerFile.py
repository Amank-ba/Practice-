def more_even(num):
    even_count = 0
    odd_count = 0
    for i in num:
        if i %2 == 0:
            even_count += 1
        else:
            odd_count += 1
        return even_count > odd_count
print(more_even([2,4,6,7,9,1,11,13]))