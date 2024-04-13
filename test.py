import json

class Person:
    def __init__(self, name, age, city, weapon):
        self.name = name
        self.age = age
        self.city = city
        self.weapon = weapon

    def display_details_person(self):
        print(f"Name: {self.name}, Age: {self.age}, City: {self.city}, Weapon: {self.weapon}")

class Weapon:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def display_details_weapon(self):
        print(f"Name: {self.name}, Level: {self.level}")



def create_person_objects_from_json(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
        persons = []
        for item in data:
            person = Person(item['name'], item['age'], item['city'], item['weapon'])
            persons.append(person)
        return persons

def create_weapons_objects_from_json(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
        weapons = []
        for item in data:
            weapon = Weapon(item['name'], item['level'])
            weapons.append(weapon)
        return weapons

def main():
    json_file = 'personnages.json'  # Chemin vers votre fichier JSON
    persons = create_person_objects_from_json(json_file)

    for person in persons:
        person.display_details_person()
        print()  # Ajoute une ligne vide entre chaque personne

    json_file = 'armes.json'  # Chemin vers votre fichier JSON
    weapons = create_weapons_objects_from_json(json_file)

    for weapon in weapons:
        weapon.display_details_weapon()
        print()  # Ajoute une ligne vide entre chaque personne

if __name__ == "__main__":
    main()
