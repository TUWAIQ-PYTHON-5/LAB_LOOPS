

for number in range(45, 210):
    if number == 100:
        continue
    if number == 205:
        break
    print (number)



user_input: str = input("what is the product of 7 * 24 ?" )
while  user_input == "168":
     print("You answered this Question correctly")
     break
else:    
    print("Your Answer is wrong try again.. ")
