#Working on lists

list1= [10, 30, 20 ,40 ,50]

max=max(list1)
min=min(list1)
sum=sum(list1)

list1.append(60)

print(max)
print(min)
print(sum)
print(list1)

list1.remove(40)
print(list1)

list1.sort()
print(list1)

# list1.reverse()
# print(list1)
print(list1[::-1])