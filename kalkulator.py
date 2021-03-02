#kalkulator
import logging

print("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")
operation = input("Wybierz działanie: ")
a = input("Podaj liczbę: ")
b = input("Podaj drugą liczbę: ")

if operation == "1":
    logging.info("Dodaję %s i %s" % (a, b))
    print(float(a) + float(b))
elif operation == "2":
    logging.info("Odejmuję %s od %s" % (b, a))
    print(float(a) - float(b))
elif operation == "3":
    logging.info("Mnożę %s i %s" % (a, b))
    print(float(a) * float(b))
elif operation == "4":
    logging.info("Dzielę %s przez %s" % (a, b))
    if b == "0":
        logging.error("Nie dziel przez 0!")
    else:
        print(float(a) / float(b))