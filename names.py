name = input("Please write the name: ")

file = open("name.txt", "a")
file.write(name)
file.close()
