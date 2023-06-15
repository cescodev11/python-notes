name = input("What's your name? ")

match name:
    case"Harry" | "Heromine" | "Ron":
        print("Griffinydor")
    case "Draco":
        print("Syltherin")
    case _:
        print("Who? ")
