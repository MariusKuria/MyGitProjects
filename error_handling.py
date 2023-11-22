def main():
    x = get_int("What's x? ")
    print(f"X is {x}")

def get_int(question):  
    while True:
        try:
            x = int(input(question))
        
        except ValueError:
            print("x is not an integer") #vietoje print galime naudoti pass, tik tuomet 
        #tik tuomet kartos input uzklausa whats x
        else:
            return x # break galime istrinti, nes return yra galingesnis

main() 
