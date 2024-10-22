"""
# Review of return statements
def test():
    secret_num = 5

    #print(secret_num)
    return secret_num

#test()
#print(secret_num)

my_var = test()
print(my_var)
"""


"""
def average_of_3(num1, num2, num3):
    average = (num1 + num2 + num3) / 3

    return average # a return statement immediately terminates the function

    print("Hello!") # unreachable code

result = average_of_3(20, 28, 16)
print(result)

# format the output
formatted_answer = format(result, ".2f")
print(formatted_answer)

# more examples of function calls
result2 = average_of_3(1, 50, 42)
result3 = average_of_3(20, 30, 40)

print(result2, result3)

overall_average = average_of_3(result, result2, result3)
print(overall_average)

print( average_of_3(1, 2, 3) )
"""









"""
# Returning multiple values
def scramble_letters(c1, c2, c3):
    word1 = c1 + c2 + c3
    word2 = c1 + c3 + c2
    word3 = c2 + c1 + c3
    word4 = c2 + c3 + c1
    word5 = c3 + c1 + c2
    word6 = c3 + c2 + c1

    return word1, word2, word3, word4, word5, word6

w1, w2, w3, w4, w5, w6 = scramble_letters("a", "b", "c")
print(w1, w2, w3, w4, w5, w6)

my_var1 = scramble_letters("c", "a", "t")
print(my_var1)
"""








# The inner workings of functions
"""
# Example #1
def fun1(x):
    print("fun1")
    x += 1
    fun3(x)

def fun2(x):
    print("fun2")
    x += 2

def fun3(x):
    print("fun3")
    x += 3
    fun2(x)

x = fun1(0)
print(x)
"""



"""
# Example #2
def fun1(x):
    print("fun1")
    x += 1
    fun3(x)

    return x

def fun2(x):
    print("fun2")
    x += 2

    return x

def fun3(x):
    print("fun3")
    x += 3
    fun2(x)

    return x

x = fun1(0)
print(x)
"""




# Example #3
def fun1(x):
    print("fun1")
    x += 1
    x = fun3(x)

    return x

def fun2(x):
    print("fun2")
    x += 2

    return x

def fun3(x):
    print("fun3")
    x += 3
    x = fun2(x)

    return x

x = fun1(0)
print(x)














import khye_functions

result = khye_functions.sum_of_5(1, 2, 3, 4, 5)
print(result)























































