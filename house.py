def main():
    name = input("Name ")
    match name:
        case "Harry" |"Hermione"|"Ron":
            print("Gryffindor")
        case "Draco":
            print("Slytherin")
        case _:
            print("Who?")
while True:
    main()
