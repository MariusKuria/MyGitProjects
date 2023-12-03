for _ in range(3):
    name = input("Please write the name: ")

    file = open("name.txt", "a")
    file.write(f"{name}\n")
    file.close()


4500*70