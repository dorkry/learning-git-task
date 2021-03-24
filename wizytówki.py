# wizytówki
class Card:
    def __init__(self, name, surname, company_name, position_in_company, email):
        self.name = name
        self.surname = surname
        self.company_name = company_name
        self.position_in_company = position_in_company
        self.email = email
        
        self.lenght = len(self.name) + len(self.surname) + 1


# print obiect
    def __str__(self):
        return f'{self.name}, {self.surname}, {self.email}'
   
# contact
    def contact(self):
        print(f"Kontaktuję się z {self.name} {self.surname},{self.position_in_company},{self.email}")
        return

# dekorator- tu coś nie działa tak jak powinno :)
    @property
    def label_lenght(self):
        return len(self.name) + len(self.surname) + 1        

# dziedziczenie:
class BaseContact(Card):
    def __init__(self, phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.phone = phone

    def contact(self):
        print(f"Wybieram numer {self.phone} i dzwonię do {self.name} {self.surname}")
        return

class BusinessContact(Card):
    def __init__(self, business_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.business_phone = business_phone

    def contact(self):
        print(f"Wybieram numer {self.business_phone} i dzwonię do {self.name} {self.surname}")
        return

contacts = []
contacts.append(Card("Andrzej","Nowak", "MI6", "CEO", "andrzej.nowak@mi6.com"))
contacts.append(Card("Kordian", "Zordon", "Ż&M", "tester", "kordzord@zm.com"))
contacts.append(Card("Sewryn", "Burza", "Medical Comp.", "product manager", "s.burza@o2.pl"))
contacts.append(Card("Joanna", "Nowak", "KKM", "secretary", "nowakj.kkm@gmail.com"))
contacts.append(Card("Katarzyna", "Kowalska", "Health and Life", "prodact owner", "kk.hal@wp.pl"))

for person in contacts:
    print(person.name, person.surname, person.email)
    print(person)

by_name = sorted(contacts, key = lambda contact: contact.name)
by_surname = sorted(contacts, key = lambda contact: contact.surname)
by_email = sorted(contacts, key = lambda contact: contact.email)

for i in by_name:
    print(i)

for i in by_surname:
    print(i)

for i in by_email:
    print(i)

base =  BaseContact("1122334455", "Andrzej","Nowak", "MI6", "CEO", "andrzej.nowak@mi6.com")
base.contact()
print(base.label_lenght)

business = BusinessContact("2233445566","Andrzej","Nowak", "MI6", "CEO", "andrzej.nowak@mi6.com")
business.contact()