#ego to etreksa me .txt file ke ebala tis tetrades tin mia kato apo tin ali px: 1234
#                                                                               0987
#                                                                               1510
#                                                                               2020
#                                                                               2432
#                                                                               ....

import errno

# Main()

text = input("Please Enter the Text File Name or Path ")

while True :
    try:
        f = open(text, 'r')
        break
    except IOError as e:
        if e.errno == errno.EACCES:
            print("file exists, but isn't readable")
        elif e.errno == errno.ENOENT:
            print("file isn't readable because it isn't there or you have entered wrong name")
        text = input("Please Enter again the correct Text File Name or Path ")

number = input("Please Enter a 6-digit Integer: ")

while len(number) != 6 : 
    number = input("Thats not a 6-digit integer. Please Enter an 6-digit Integer: ")

number = [int(x) for x in str(number)]                  #xorizo ta psifia tou 6-digit ari8mou ke ta bazo xorista se lista
number.sort()

contents = f.read().splitlines()                        #diabazi olo to text ke to xorizi se lista grami grami

i = 0
count = 0
while i < len(contents) and count < 4 :                 #ektelite oso exi antikimena to txt file
    count = 0                                           
    lst = []                                            #dimiourgo lista pou 8a apo8ikeusi tin 4ada pou mpori na ftiaxti
    for digit in range(len(number)) :                   #apo tin 6ada
        if count == 4 :                                 #ka8e psifio apo ton 6-digit ari8mo sigkrinete me ka8e psifio
            break                                       #tou 4-digit ari8mou gia ka8e ari8mo tis listas
        for char in contents[i] :                       #an ine idios count++ kai otan count = 4 tote telioni  
            if char == str(number[digit]) :
                lst.insert(count , contents[i])         #kratai tin sosti 4ada
                count = count + 1
                temp = contents[i]
                temp = temp.replace(char , '' , 1)      #bgazo ton char pou sigkri8ike gia na min diplometri8i
                contents[i] = temp
                break
            if count == 4 :
                break
    i = i + 1

if count == 4 : 
    print("Iparxi dia8esimi tetrada kai einai o ari8mos " , lst[0])
else :
    print("Den iparxi dia8esimi tetrada")

f.close()