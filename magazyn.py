#magazyn

import logging
logging.basicConfig(level=logging.INFO)

def close():
    return 0

menu = {
 "exit": close
}

if __name__ == "__main__":
    while True:
        choice = input("What do you want to do?")
        try:
            menu_func = menu[choice]
        except KeyError:
            print("Unknown action")
        else:    
            result = menu_func()
            if result == 0:
                print("Thank you! Bye!")
                break
