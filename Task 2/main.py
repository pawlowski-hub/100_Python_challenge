''' Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320 '''
given_number = int(input('Enter given number: '))
result = 1
for number in range(1, (given_number+1)):
    result = number * result

print(result)
