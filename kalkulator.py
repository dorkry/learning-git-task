#kalkulator
import logging
logging.basicConfig(level=logging.INFO)

print("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")
operation = input("Wybierz działanie: ")
a = float(input("Podaj liczbę: "))
b = float(input("Podaj drugą liczbę: "))

if operation == "1":
    logging.info(f"Dodaję {a} i {b}")
    print(a + b)
elif operation == "2":
    logging.info(f"Odejmuję {b} od {a}")
    print(b - a)
elif operation == "3":
    logging.info(f"Mnożę {a} i {b}")
    print(a * b)
elif operation == "4":
    logging.info(f"Dzielę {a} przez {b}")
    print(a / b)