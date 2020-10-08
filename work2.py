data = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

sort_data = [data[el] for el in range(1, len(data)) if data[el-1] < data[el]]

print(sort_data)