import random

lowerbound = input("Enter Loewr Bound : ")
upperbound = input("Enter Upper Bound : ")
lowerbound = int(lowerbound)
upperbound = int(upperbound)

randomNumber = random.randint(lowerbound, upperbound)

a = 1
count = 0
while(a == 1):
    number = input("Guess it : ")
    number = int(number)
    if(number < randomNumber):
        print("Chota hai")
        count += 1
        continue
    elif(number > randomNumber):
        print("Bada hai")
        count += 1
        continue
    elif(number == randomNumber):
        print("Sahi pakde Hai")
        Output_string = "You Guessed it in {} times".format(count+1)
        print(Output_string)
        break
