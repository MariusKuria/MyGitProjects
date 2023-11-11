def even_or_odd():
    x = int(input("Please add number: "))
    if is_even(x):
        print("Even!")
    else:
        print("Odd!")

def is_even(n):
    return n % 2 == 0 
    
even_or_odd()

