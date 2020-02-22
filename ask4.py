def isPrime(n) :
    if n == 1 :
        return False #o ari8mos 1 den ine protos

    for i in range(2 , n) :
        if n % i == 0 :
            return False
    return True

# Main()

string = input("Enter text ")
string = [x for x in str(string)]
while len(string) < 1 :
    string = input("Please enter at least one character ")
    string = [x for x in str(string)]

i = 1
number = ord(string[0])
while i < len(string) :
    number = str(number) + str(ord(string[i]))
    i = i + 1
     
number = int(number)
if isPrime(number) :
    print(number , " is prime")
else :
    print(number , " is not prime")