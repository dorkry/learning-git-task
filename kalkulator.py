#kalkulator
import logging
logging.basicConfig(level=logging.INFO)

def getdata():
    print("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie, 0 Koniec:")
    operation = input("Wybierz działanie: ")
    if operation != "0":
        a = float(input("Podaj liczbę: "))
        b = float(input("Podaj drugą liczbę: "))
    else:
        a = 0
        b = 0
    return (operation, a, b)

def add(x, y):
    return x + y

def substract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

if __name__ == "__main__":
    while True:
        (operation, a, b) = getdata()

        if operation == "1":
            logging.info(f"Dodaję {a} i {b}")
            print(add(a, b))
        elif operation == "2":
            logging.info(f"Odejmuję {b} od {a}")
            print(substract(a, b))
        elif operation == "3":
            logging.info(f"Mnożę {a} i {b}")
            print(multiply(a, b))
        elif operation == "4":
            logging.info(f"Dzielę {a} przez {b}")
            print(divide(a, b))
        elif operation == "0":
            logging.info("Koniec")
            break