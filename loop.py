
#range 

for number in range(45,210):
     if (number == 100): 
         continue
     print(number)
     if (number == 205):
          break 


#while 


while True:
    user_n = int(input("what is the product of 7 * 24 ?"))
    if user_n == 168:
       print( "You answered this Question correctly")  
       break
    else:
      print("Your Answer is wrong try again..")

