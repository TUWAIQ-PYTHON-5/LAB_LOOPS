#first request
for number in range(45,210):

    if number == 100:
        continue
    elif number == 205:
        break
    print(number)

#second request
while True:
    answer = int(input("what is the product of 7 * 24? "))
    if answer == 168:
        print("You answered this Question correctly")
        break
    else:
        print("Your Answer is wrong try again..")
