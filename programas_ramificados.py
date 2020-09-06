num_1 =int(input("Escoge un entero:"))
num_2 =int(input("Escoge otro entero:"))

if num_1 > num_2:
    print(str(num_1) + " es mayor que " + str(num_2))
elif num_1 < num_2:
    print(str(num_2) + " es mayor que " + str(num_1))
else:
    print(str(num_1) + " es igual que " + str(num_2))