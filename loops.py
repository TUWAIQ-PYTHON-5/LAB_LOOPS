

for i in range(45,210):
    
    if i == 100:
        continue
    elif i == 205:
        break
    print(i)

print("\n================================")

num : int = int(input("what is the product of 7 * 24 ? "))
while True:
    if num == 168:
     print("You answered this Question correctly")
     break
    else:
     print("Your Answer is wrong try again..")
     num : int = int(input("what is the product of 7 * 24 ? "))
     
    




