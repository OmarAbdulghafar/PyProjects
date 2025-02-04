# Strong Password Generator
import string
import random

s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

charctar_number = input("How many charracter for password ?")

while True:
    try:
        charctar_number = int(charctar_number)
        if charctar_number < 6:
            print("You need at least 6 character")
            charctar_number = input("How many charracter for password ?")
        else:
            break
    except:
        print("Pls inter number only")
        charctar_number = input("How many charracter for password ?")

random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

part1 = round(charctar_number * (30/100))
part2 = round(charctar_number * (20/100))

password = []

for i in range(part1):
    password.append(s1[i])
    password.append(s2[i])

for i in range(part2):
    password.append(s3[i])
    password.append(s4[i])

random.shuffle(password)
password = "".join(password[0:])

print(password)
