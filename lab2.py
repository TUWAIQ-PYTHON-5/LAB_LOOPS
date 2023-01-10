
# requirement 1

for num in range (45,210):
    if num == 100:
        continue
    if num == 205:
        break
    
    print(num)



# requirement 2



while True:
    user = int (input ("what is the product of 7 * 24 ?"))
    if user != 168:
        print("Your Answer is wrong try again..")
        continue
    else:
        print("You answered this Question correctly")
        break

        


