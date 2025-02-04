secret_word = "ay 7aga"
user_guess= ""
count = 0
count_limit = 3
finish = False

print("This is a Simple Game try to guess the Secret Word, You have 3 tries")

while user_guess != secret_word and not finish:
    if count < count_limit:
        user_guess = input("Enter your guess")
        count += 1
    else:
        finish = True

if finish:
    print("You Lose")
else:
    print("You Win")