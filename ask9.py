count = False
while True:
    if count == False :
        count = True
        try:
            number = int(input("Enter an Integer: "))
        except ValueError:
            continue
        else:
            break
    else :
        try:
            number = int(input("You didnt enter an integer. Please Enter an Integer: "))
        except ValueError:
            continue
        else:
            break

if (number < 10 and number > -10):
    print(number)
elif (number >= 10):
    while number >= 10:
        number=number*3
        number=number+1
        newNumber = 0
        while number >0:
            digit = number % 10
            newNumber = newNumber + digit
            number = number//10
        number = newNumber
        print(number)
else:
    while (number <= -10 or number >= 10):
        number=number*3
        number=number+1
        newNumber = 0
        positiveNumber = abs(number)
        while positiveNumber > 0:
            digit = positiveNumber % 10
            newNumber = newNumber + digit
            positiveNumber = positiveNumber // 10
        number = newNumber
        print(number)