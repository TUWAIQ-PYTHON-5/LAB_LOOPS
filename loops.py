for number in range(45, 210):
    if number == 100:
        continue
    elif number == 205:
        break



    usrAnswer: int = int(input("What is the prodect of 7 x 24 ?"))
    while usrAnswer != 168: 
        print("Your Answer is wrong, try again")
    else:
        print("You answerd this Question correctly")