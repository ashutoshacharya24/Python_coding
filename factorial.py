# Question: Write a program which can compute the factorial of a given numbers. The results should be printed in a comma-separated sequence on a single line. Suppose the following input is supplied to the program: 8 Then, the output should be: 40320

# Hints: In case of input data being supplied to the question, it should be assumed to be a console input.


# Solution:

def fact(number):
    if number == 0:
        return 1
    return number * fact(number - 1)

number=int(input("Enter a Number: "))
print(fact(number))
