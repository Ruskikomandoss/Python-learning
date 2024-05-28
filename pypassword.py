import random


def password_length():
    while True:
        length = int(input("Jak długie ma być hasło? Podaj ilość znaków:\nWpisz: "))
        if not str(length).isdecimal():
            print(f"Zamiast liczby wpisałeś: {type(length).__name__}. Nie tak się umawialiśmy")
        elif length > 50:
            print("Bez przesady, chyba trochę za dużo?")
        else:
            return length


def symbols(length_of_password, new_password):
    while True:
        symbols_count = int(input("Ile symboli specjalnych ma się znajdować w Twoim haśle?\nWpisz: "))
        if not str(symbols_count).isdecimal():
            print("Ale cyfrę wpisz")
        elif symbols_count >= length_of_password:
            print(f"Symboli musi być zdecydowanie mniej niż łącznie liter w haśle. Polecamy maksymalnie taką ilość: {int(length_of_password/3)}")
        else:
            symbols_list = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "[", "]", "{", "}"]
            for _ in range(symbols_count):
                new_password.append(random.choice(symbols_list))
            return new_password


def numbers(length_of_password, symbols_of_password):
    while True:
        num = int(input("Ile cyfr ma się znajdować w haśle?\nWpisz: "))
        if not str(num).isdecimal():
            print("Ale cyfrę wpisz")
        elif num >= (length_of_password - len(symbols_of_password)):
            print(f"Liczb nie może być więcej niż pozostałych znaków w Twoim haśle. Polecamy maksymalnie taką liczb: {int((length_of_password-len(symbols_of_password))/3)}")
        else:
            for _ in range(num):
                symbols_of_password.append(random.randint(0,9))
            return symbols_of_password


def password_creation(numbers_of_password, length_of_password):
    for _ in range(length_of_password-len(numbers_of_password)):
        numbers_of_password.append(chr(random.choice(list(range(65,91))+list(range(97,123)))))
        random.shuffle(numbers_of_password)
    return ''.join(map(str, numbers_of_password))



def main():
    new_password = []
    print("Witamy w generatorze haseł PyPassword!")
    length_of_password = password_length()
    symbols_of_password = symbols(length_of_password, new_password)
    numbers_of_password = numbers(length_of_password, symbols_of_password)
    prepared_password = password_creation(numbers_of_password, length_of_password)
    return print(prepared_password)



if __name__ == "__main__":
    main()
