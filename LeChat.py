import json

class Person:
    def __init__(self, name, stamina, weapon):
        self.name = name
        self.stamina = stamina
        self.weapon = weapon

    def display_details_person(self):
        print(f"Name: {self.name}, stamina: {self.stamina}")

    def attaque(self,defenseur):

        defenseur.stamina = defenseur.stamina - self.weapon

        return defenseur

def create_person_objects_from_json(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
        persons = []
        for item in data:
            person = Person(item['name'], item['stamina'], item['weapon'])
            persons.append(person)
        return persons

def main():
    json_file = 'characters2.json'  # Chemin vers votre fichier JSON
    persons = create_person_objects_from_json(json_file)

    person1 = persons[0]
    person2 = persons[1]

    sortDeLaBoucle = 0

    while not sortDeLaBoucle:
        defenseur = person2
#        defenseur = person1.attaque(defenseur)
        person1.attaque(defenseur)
        defenseur = person1
#        defenseur = person2.attaque(defenseur)
        person2.attaque(defenseur)
        if person1.stamina<=0 or person2.stamina<=0 :
            sortDeLaBoucle=1


    for person in persons:
        person.display_details_person()
        print()  # Ajoute une ligne vide entre chaque personne

if __name__ == "__main__":
    main()
