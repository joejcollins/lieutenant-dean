from my_module.models.person import Person

alice = Person.find_by_file("alice.json")
print(alice.to_primitive())
alice.update({
    "age": 50,
    "bald": True,
    "hair_colour": "Black",
    "female": True,
    "male": True,
    "gender": "Male"
    })
print(alice.to_primitive())
print(alice.to_primitive(role='remove_deprecated'))
alice.validate()
alice.save()

people = Person.all()
print(people[2].to_primitive())
print(people[2].to_primitive(role='remove_deprecated'))