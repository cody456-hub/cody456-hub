size = int(input("請輸入加法口訣表的大小（小於10的正整數）："))

print("------------------------------------------------------------")

for i in range(1, size + 1):
    for j in range(1, size + 1):
        sum = i + j        
        if sum_ij < 10:
            print(f"{i} + {j} = {sum}  ", end=" ")
        else:
            print(f"{i} + {j} = {sum} ", end=" ")
    print()

print("------------------------------------------------------------")