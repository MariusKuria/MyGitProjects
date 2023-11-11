name = input("Where do live? ")

match name:
    case "Rimas" | "Paulius" | "SS":
        print("sestokai")
    case "Karve":
        print("seima")
    case _ :
        print("What?")