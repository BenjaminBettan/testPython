import json

class PhoneNumber:
    def __init__(self, phone_type, number):
        self.phone_type = phone_type
        self.number = number

    def display_details1(self):
        print(f"Type: {self.phone_type}, Number: {self.number}")

class Person:
    def __init__(self, name, age, city, phone_numbers):
        self.name = name
        self.age = age
        self.city = city
        self.phone_numbers = [PhoneNumber(p['type'], p['number']) for p in phone_numbers]

    def display_details2(self):
        print(f"Name: {self.name}, Age: {self.age}, City: {self.city}")
        if self.phone_numbers:
            print("Phone Numbers:")
            for phone_number in self.phone_numbers:
                phone_number.display_details1()
        else:
            print("No phone numbers")

def create_person_objects_from_json(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
        persons = []
        for item in data:
            person = Person(item['name'], item['age'], item['city'], item['phone_numbers'])
            persons.append(person)
        return persons

def main():
    json_file = 'json.json'  # Chemin vers votre fichier JSON
    persons = create_person_objects_from_json(json_file)

    for person in persons:
        person.display_details2()
        print()  # Ajoute une ligne vide entre chaque personne

if __name__ == "__main__":
    main()
