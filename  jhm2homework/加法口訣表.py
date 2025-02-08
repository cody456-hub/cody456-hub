size = int(input("Input Addition Table Size smaller 10:"))

print("------------------------------------------------------------")

for a in range(1, size + 1 ):
    for b in range(1, size + 1 ):
        sum = a + b        
        print(f"{a} + {b} = {sum}  ", end=" ")

    print()

print("------------------------------------------------------------")