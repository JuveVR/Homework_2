
person = {"name": "Artur",
          "surname": "Pirozhkov",
          "age": 96,
          "occupation": "surgeon",
          "income": 2000}
print(person)

person.update({"age":97, "occupation": "pensioner", "income": 200})
print("Here is updated retired person: " + str(person))
print(person.items())