for number in range(45, 210):
    if number == 100:
        continue
    if number == 205:
        break
    print (number)




user_intpput = input("what is the product of 7 * 24 ?" )

while int(user_intpput) != 7*24:
      print("Your Answer is wrong try again..")
      user_intpput = input ("what is the product of 7 * 24 ?")

else :
      print("You answered this Question correctly " ) 