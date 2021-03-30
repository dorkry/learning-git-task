# wizytówki
from faker import Faker

class BaseContact:
    def __init__(self, name, surname, email, phone):
        self.name = name
        self.surname = surname
        self.email = email
        self.phone = phone
                
    # print obiect
    def __str__(self):
        return f'{self.name}, {self.surname}, {self.email}'

    def __repr__(self):
        return str(self)
   
    # contact
    def contact(self):
        print(f"Kontaktuję się z {self.name} {self.surname},{self.email}")
        return

    # dekorator
    @property
    def label_lenght(self):
        return len(self.name) + len(self.surname) + 1        

    def contact(self):
        print(f"Wybieram numer {self.phone} i dzwonię do {self.name} {self.surname}")
        return

class BusinessContact(BaseContact):
    def __init__(self, business_phone, company_name, position_in_company, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.business_phone = business_phone
        self.company_name = company_name
        self.position_in_company = position_in_company
        
    def contact(self):
        print(f"Wybieram numer {self.business_phone} i dzwonię do {self.name} {self.surname}")
        return

def create_contacts(type, number):
    contact_list = []
    fake = Faker()
    if type == "Base":
        for i in range(number):
           name = fake.first_name()
           surname = fake.last_name()
           mail = fake.email()
           phone = fake.phone_number()           
           contact_list.append(BaseContact(name, surname, mail, phone))

    elif type == "Business":
        for i in range(number):
           name = fake.first_name()
           surname = fake.last_name()
           mail = fake.email()
           phone = fake.phone_number()
           phone2 = fake.phone_number()
           company = fake.company()
           job = fake.job()
           contact_list.append(BusinessContact(phone2, company, job, name, surname, mail, phone))

    return contact_list

#test
contacts = [
    BaseContact("Andrzej","Nowak", "andrzej.nowak@mi6.com", "11223344"),
    BaseContact("Kordian", "Zordon", "kordzord@zm.com", "22334455"),
    BaseContact("Sewryn", "Burza", "s.burza@o2.pl", "33445566"),
    BaseContact("Joanna", "Nowak", "nowakj.kkm@gmail.com", "44556677"),
    BaseContact("Katarzyna", "Kowalska", "kk.hal@wp.pl", "55667788")
]

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

business = BusinessContact("2233445566","MI6", "CEO", "Andrzej","Nowak", "andrzej.nowak@mi6.com", "11223344")
business.contact()

print(create_contacts("Base", 5))

print(create_contacts("Business", 3))
