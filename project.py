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

def main():
    lang = pass_lang(input("Enter language of password(rus/eng):").lower())
    shuffle(signs)
    pswrd = ""
    for i in range(len(signs)):
        pswrd += signs[i]
    print("Your password is:", pswrd)

if __name__ == "__main__":
    lenght = int(input("Enter password lenght:"))
    signs = []
    main()
