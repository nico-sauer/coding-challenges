#task 1 writing lines
for i in range(100):
   print(“I will listen to my teacher and complete my work on time.”)
   
#task 2 count from 0 to 500 in steps of 5
for i in range(0,505, 5):
   print(i)

#task 3 countdown from 100 to 0
count = 100
for _ in range(100):
   print(count)
   count -= 1
   
#task 3 display x 12 multiplication table
n = 1
for _ in range(10):
    multiply = n * 12
    print("{} x 12 = {}".format (n,multiply))
    n += 1

#task 4 ask for user input to display times table
n = 1
table = int(input("Which times table would you like to see?\n>"))
for _ in range(10):
    multiply = n * table
    print("{} x {} = {}".format (n, table, multiply))
    n += 1

#task 5 recite alphabet using ascii values and for loop
n = 65
for _ in range(26):
    letter = chr(n)
    print(letter)
    n += 1
    
#task 6 input positive integer and calculate iterative sum 
num = int(input("Enter positive integer: "))
sum = num
if num > 0:
    for i in range(num): 
       sum = sum + i
    print("Iterative Sum for {} = {}".format (num, sum))
else:
    print("Invalid.")


#task 7 calculate factorial 
num = int(input("Enter positive integer: "))
sum = num 
factor = sum - 1

if num > 0:
    while factor > 0: 
        sum = sum * factor
        factor -= 1
    print("Factorial Sum for {} = {}".format (num, sum))
else:
    print("Invalid.")