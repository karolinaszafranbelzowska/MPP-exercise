# Question 5: Modify the previous program such that only multiples of
# three or five are considered in the sum, e.g. 3,5,6,9,10,12,15 for n = 17.

# taken from: https://adriann.github.io/programming_problems.html

n = int(input("Enter a number: "))

sum = 0

for i in range(1, n+1):
    if ((i % 3) == 0) or ((1 % 5) == 0):
        print(i)
        sum = sum + i

print("The sum of 1 to %d, was %d" % (n, sum))