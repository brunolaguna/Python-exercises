print("True = número primo.\nFalse = número composto.")
n = int(input("Digite um número de 0 a 100: "))
i = -1

while(i < 7):
    i = i + 1
    if(i == 0 or i == 4 or i == 1 or i == 6):
        print(f"False: {i}")
    else:
        print(f"True: {i}")
for i in range(8, n + 1):
    if(i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0):
        print(f"False: {i}")
    else:
        print(f"True: {i}")
