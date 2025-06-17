import random
n = random.randint(1,100)
a = -1
guesses = 0
while a!=n:
    
    guesses += 1
    a = int(input("guess a number : "))
    print(f"no entered by u is {a}")
    
    if a > n:
        print("Lower number please")
    elif a < n:
        print("Higher number please")
    else:
        print("Congratulations! You guessed the correct number!") 
                 
print(f"total no of guesses is {guesses} guesses")

