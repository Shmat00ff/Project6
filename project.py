from random import *

def pass_lang(x):
    if x == "rus":
        chars = ["А", "а", "Б", "б", "В", "в", "Г", "г", "Д", "д", "Е", "е", "Ё", "ё", "Ж", "ж", "З", "з", "И", "и",
                 "Й", "й", "К", "к", "Л", "л", "М", "м", "Н", "н", "О", "о", "П", "п", "Р", "р", "С", "с", "Т", "т",
                 "У", "у", "Ф", "ф", "Х", "х", "Ц", "ц", "Ч", "ч", "Ш", "ш", "Щ", "щ", "Ъ", "ъ", "Ы", "ы", "Ь", "ь",
                 "Э", "э", "Ю", "ю", "Я", "я"]
        for i in range(lenght):
            password = choice(chars)
            signs.append(password)
    if x == "eng":
        chars = ["A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i", "K", "k",
                 "L", "l", "M", "m", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t", "V", "v",
                 "X", "x", "Y", "y", "Z", "z"]
        for i in range(lenght):
            password = choice(chars)
            signs.append(password)

def int_pass(x):
    if x == "yes":
        n = int(input("How many numbers do you want to add?"))
        chars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for i in range(n):
            password = choice(chars)
            signs.append(password)

def special_pass(y):
    if y == "yes":
        n = int(input("How many signs do you want to add?"))
        chars = ["+", "-", "=", "$", "%", "!", "/", "#", "*", "?"]
        for i in range(n):
            password = choice(chars)
            signs.append(password)

def main():
    lang = pass_lang(input("Enter language of password(rus/eng):").lower())
    inter = int_pass(str(input("Do you want to add numbers into your password(yes/no):")).lower())
    special = special_pass(str(input("Do you want to add special signs into your password(yes/no):")).lower())
    shuffle(signs)
    pswrd = ""
    for i in range(len(signs)):
        pswrd += signs[i]
    print("Your password is:", pswrd)

if __name__ == "__main__":
    lenght = int(input("Enter password lenght:"))
    signs = []
    main()
