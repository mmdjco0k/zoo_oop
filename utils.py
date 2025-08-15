def print_info(animal):
    print(f"\nname is {animal["name"]}")
    print(f"id is {animal["id"]}")
    print(f"age is {animal["age"]}")
    print(f"weight is {animal["weight"]}")

    animal_type = animal["animal_type"]
    match animal_type:
        case "lion":
            print(f"The size of the {animal["name"]} tail is {animal["tail_size"]} cm")
            print(f"The strength of the {animal["name"]} is {animal['strength']}")
            print(f"The {animal["name"]} {'is the' if animal["herd_leader"] else 'is not the'} herd leader")
        case "rat":
            print(f"The color of {animal["name"]} is {animal['color']} ")
            print(f"The {animal["name"]} {'can' if animal['climbing'] else 'can not'} climb")
            print(f"The {animal["name"]} {'can' if animal['digging'] else 'can not'} digging")
        case "snake":
            print(f"{animal["name"]} is {'venomous' if animal["venomous"] else 'not venomous'}")
            print(f"{animal["name"]} is {'tamed' if animal["tamed"] else 'not tamed'}")
            print(f'{animal["name"]} length is {animal["length"]}')
