#Program to convert a uppercase string into lowercase and vice-versa also to check if a string starts with vowel or not

str_lower="i am ayaan"
str_upper="YOU ARE NOT AYAAN"

print("String 1 : ", str_lower)
print("String 2 : ", str_upper)

strupr=str_lower.upper()
strlwr=str_upper.lower()

print("String 1 : ", strupr)
print("String 2 : ", strlwr)


if (str_lower[0] == 'A' or str_lower[0] == 'a' or 
    str_lower[0] == 'E' or str_lower[0] == 'e' or
    str_lower[0] == 'I' or str_lower[0] == 'i' or
    str_lower[0] == 'O' or str_lower[0] == 'o' or
    str_lower[0] == 'U' or str_lower[0] == 'u') :
    print("The String 1 ", str_lower, " starts with a vowel")

else:
    print("The String 1 ", str_lower, " does not start with a vowel")



if (str_upper[0] == 'A' or str_upper[0] == 'a' or 
    str_upper[0] == 'E' or str_upper[0] == 'e' or
    str_upper[0] == 'I' or str_upper[0] == 'i' or
    str_upper[0] == 'O' or str_upper[0] == 'o' or
    str_upper[0] == 'U' or str_upper[0] == 'u') :
    print("The String 2 ", str_upper, " starts with a vowel")

else:
    print("The String 2 ", str_upper, " does not start with a vowel")
