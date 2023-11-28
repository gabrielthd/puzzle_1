array_with_duplicates = [1,2,3,1,4,5,2,3,1,2]

new_array = []

for i in array_with_duplicates:

    if i not in new_array:
        new_array.append(i)

print(new_array)