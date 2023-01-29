#guess the number
n = 19
x = 0
print("You have 5 guesses to complete the game\nEnter number\n")
while(x<=5):
    i = int(input(""))
    x = x+1
    if x<6:
        if i==n:
            print("congo")
            print("you took",x,"guesses to finish")
            break
        elif i>n:
            print("try lower num")
            print("you have ",5-x+1," guesses left")
            continue
        elif i<n:
            print("try higher num")
            print("you have ",5-x+1," guesses left")
        continue
    else:
        print("Game Over")