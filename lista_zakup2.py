#lista zakupów
shopping={
    "Piekarnia":["chleb", "pączek", "bułki"],
    "Warzywniak":["marchew", "seler", "rukola"]
    }
number=0
#new comment to commit to Git
for shop in shopping.keys():
    products=""
    for i in shopping[shop]:
        products=products  + i.capitalize()+","
    print("Idę do ",shop.capitalize(), "i kupuję ",products)
    number=number+len(shopping[shop])
#the end-second commit
#greetings
print("Greetings for Trinidad and Tobago!")

    