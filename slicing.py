#Reversing a string and checking if it is a palindrome

a="racecar"
sliced_a=a[::-1]
print (sliced_a)

if a == sliced_a:
    print("The string is a Palindrome")

else:
    print("The string is a not Palindrome")
