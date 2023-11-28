# assuming that numbers can either be natural or whole numbers

array = [130,360,20,370,110,361,20]

first_large = 0
second_large = 0

for i in array:
    if i > first_large:
        second_large = first_large
        first_large = i

    elif i > second_large:
        second_large = i

print(second_large)