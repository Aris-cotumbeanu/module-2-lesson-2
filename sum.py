n = int(input("Enter a number which sum you want to find: "))
sum = 0
for i in range(1, n + 1):
    sum += i
print("The sum of numbers from 1 to", n, "is:", sum)