a = int(input('Digite o 1 lado do triangulo'))
b = int(input('Digite o 2 lado do triangulo'))
c = int(input('Digite o 3 lado do triangulo'))
if (a > 0) and (b > 0) and  (c > 0):
    if (a + b > c) and (a + c > b) and (b + c > a):
        if (a != b) and (a != c) and (b != c):
            print('escaleno')
        else:
            if a == b and a == c and b == c:
                print('equilatero')
            else:
                print('isoceles')
    else:
        print('não dar para fazer um triangulo')
else:
    print('não dar para fazer um triangulo')