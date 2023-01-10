for i in range(45, 211):
    if i == 100:
        continue
    if i == 205:
        break
    print(i)
question = "What is the product of 7 * 24 ?"
answer = 168

while True:
    user_answer = int(input(question))
    if user_answer == answer:
        print("You answered this Question correctly")
        break
    else:
        print("Your Answer is wrong try again..")
