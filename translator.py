# This simple project convert pattern of chars into specific char

def translate(str):
    translation = ""
    for letter in str:
        if letter in "AEIOUaeiou":
            translation = translation + "z"
        else:
            translation = translation + letter
    return translation

print(translate(input("enter the word: ")))