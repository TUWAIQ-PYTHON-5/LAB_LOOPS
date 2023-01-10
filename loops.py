#1 
for number in range(45, 210, 1):
    if number == 100:
        continue
    elif number == 205:
        break
    print(number)

#2
'''
'''

usrAnswer: int = int(input("What is the prodect of 7 x 24 ?"))
while usrAnswer != 168: 
        usrAnswer: int = int(input("Your Answer is wrong, try again"))
else:
    print("You answerd this Question correctly")
