#Дано список
'''
data = [1,2,31,23,213,213,123,1,1,1,21,2,3,231,2321,31,31,23,13,2,23,23,2,2321]
'''
# та
'''
data2 = [3,2,4,34,5,45,6,65,756,4,56,856,756,67,856,234,54,754,235,547,34,346,455,3,54,634,434,634,5,2345]
'''
# Задачі
# 1
'''
Позбутись дублювання у списках data і data2
'''
data = [1, 2, 31, 23, 213, 213, 123, 1, 1, 1, 21, 2, 3, 231, 2321, 31, 31, 23, 13, 2, 23, 23, 2, 2321]
data2 = [3, 2, 4, 34, 5, 45, 6, 65, 756, 4, 56, 856, 756, 67, 856, 234, 54, 754, 235, 547, 34, 346, 455, 3, 54, 634, 434, 634, 5, 2345]

unique_data = list(set(data))
unique_data2 = list(set(data2))

print("Унікальні елементи data:", unique_data)
print("Унікальні елементи data2:", unique_data2)
# 2
'''
Знайти унікальні елементи для data
Знайти унікальні елементи для data2
'''
data = [1, 2, 31, 23, 213, 213, 123, 1, 1, 1, 21, 2, 3, 231, 2321, 31, 31, 23, 13, 2, 23, 23, 2, 2321]
data2 = [3, 2, 4, 34, 5, 45, 6, 65, 756, 4, 56, 856, 756, 67, 856, 234, 54, 754, 235, 547, 34, 346, 455, 3, 54, 634, 434, 634, 5, 2345]

unique_data = list(set(data))
unique_data2 = list(set(data2))

unique_data_add = set(data) - set(data2)
unique_data2_add = set(data2) - set(data)

print("Елементи у data, яких немає у data2:", unique_data_add)
print("Елементи у data2, яких немає у data:", unique_data2_add)

print("Унікальні елементи data:", unique_data)
print("Унікальні елементи data2:", unique_data2)

# 3
'''
знайти перетин між data і data2
сформувати із нього кортеж
'''
intersection = set(unique_data).intersection(set(unique_data2))
intersection_tuple = tuple(intersection)

print("Перетин між unique_data і unique_data2:", intersection_tuple)


