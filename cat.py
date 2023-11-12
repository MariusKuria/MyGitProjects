# naudojame while
"""
i = 0

while i < 3:
    print("meow")
    i += 1
"""

# naudojame for

for i in range(3):
    print("meow")

# jei norime kelis kartus isprint ta pati tiesiog zodi padauhina, end 
# nepalieka tucios eilutes *

print("Kietai\n" * 10, end="")

# kitas cariantas\

while True:
    n = int(input("Whats n? "))
    if n > 0:
        break

for _ in range(n):
    print("kiss")