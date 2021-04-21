total = 0

list1 = [1,2,3,4,5,5]
lenght = len(list1)
for i in range(0, len(list1)):
    totalq = total + list1[i]
    average = total / lenght
print("Sum of all elements in given list1: ", totalq)

total2 = 0
list2 = [5,6,7,8,9,12]

for i in range(0, len(list2)):
    totals = total2 + list2[i]
print("Sum of all elements in given list2: ", totals)

mod = totalq % totals
if mod > 0:
    print("It is an odd value")
else:
    print("It is not an odd value")