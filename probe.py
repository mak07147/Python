some_array = [11, 1, 2, 8, 3, 4, 5]
odd_arr = sorted([i for i in some_array if i % 2 != 0])
arrs_odd = odd_arr[::-1]
final_arr = []
for el in some_array:
    if el % 2 != 0:
        b = arrs_odd.pop()
        final_arr.append(b)
print(final_arr)