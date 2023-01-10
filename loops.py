for number in range(45, 210):
  if number == 100:
        continue
  elif number == 205:
        break
  print(number)


User_Answer : int= (input("24 * 7 ="))
while (User_Answer != 168):
      print("Wrong answer, try again")
      User_Answer = int(input("24 * 7 ="))
else:
      print("your answer is correct")