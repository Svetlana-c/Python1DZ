#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
print('x y z F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            Left = not(x or y or z)
            Right = not(x) and not(y) and not(z)
            f = Left == Right
            print(x, y, z, f)