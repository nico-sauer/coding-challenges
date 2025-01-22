#Fizz - Buzz Challenge - 101Computing.net
#challenge 1
def fizz(n):
    return n % 3 == 0
def buzz (n):
    return n % 5 == 0
    
for i in range(1,101):
    
    if fizz(i):
        if buzz(i):
            print("fizz-buzz")
        else:
            print("fizz")
    elif buzz(i):
        print("buzz")
    else:
        print(i)
        
#challenge 2 
#Fizz - Buzz Challenge - 101Computing.net
def fizz(n):
    return n % 3 == 0
def buzz (n):
    return n % 5 == 0
    
score = 0
while True :
    i = int(input("Enter a number divisible by 3 to type 'fizz' or a number divisible by 5 to type 'buzz'. Enter a number divisible by both to type 'fizz-buzz': "))
    if fizz(i):
        if buzz(i):
            print("fizz-buzz")
            score += 1
        else:
            print("fizz")
            score += 1
    elif buzz(i):
        print("buzz")
        score += 1
    else:
        break
        
print("Final Score: ", score)
        

#challenge 3

def fizz(n):
    return n % 3 == 0
def buzz (n):
    return n % 5 == 0
    
score = 30
while score > 0 :
    i = int(input("Enter a number divisible by 3 to type 'fizz' or a number divisible by 5 to type 'buzz'. Enter a number divisible by both to type 'fizz-buzz': "))
    if fizz(i):
        if buzz(i):
            print("fizz-buzz")
        else:
            print("fizz")
    elif buzz(i):
        print("buzz")
    else:
        print("- 10 points")
        score -= 10
print("Game over")
