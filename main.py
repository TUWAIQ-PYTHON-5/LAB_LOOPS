for number in range(45,210):
    if number == 100:
        continue
    if number == 205:
        break
    print("Number : ",number)


userAnswer:int = int(input("What is the product of 7 * 24 ? "))
rightAnswer:int = 7*24
while not userAnswer == rightAnswer:
    userAnswer:int=int(input("Re-Enter--Your Answer is wrong try again.. : "))
else:
    print("You answered this Question correctly")

    