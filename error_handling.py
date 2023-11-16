def main():
    x = get_int()
    print(f"X is {x}")

def get_int():  
    while True:
        try:
            x = int(input("What's x? "))
        
        except ValueError:
            print("x is not an integer")
        else:
            break
    return x

main() 
