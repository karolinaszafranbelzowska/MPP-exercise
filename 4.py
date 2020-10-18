# Question 4: Write a program that asks the user for a number n
# and prints the sum of the numbers 1 to n.

# taken from: https://adriann.github.io/programming_problems.html

n = int(input("Enter a number: "))

sum = 0

for i in range(1, n+1):
    sum = sum + i

print("The sum of 1 to %d, was %d" % (n, sum))