srednica1 =float(input("Podaj średnicę pizzy nr 1: "))
cena1 =float(input("Podaj cenę pizzy nr 1: "))
srednica2 =float(input("Podaj średnicę pizzy nr 2: "))
cena2 =float(input("Podaj cenę pizzy nr 2: "))
promien1 =srednica1/2
promien2=srednica2/2
pole1=3.14 * promien1 * promien1
#pole1=3.14 * (promien1**2)
pole2=3.14 * promien2 * promien2
#pole2=3.14 * (promien2**2)
op1 = pole1/cena1
op2 = pole2/cena2
if op1 > op2:
    print("Pizza nr 1 bardziej się opłaca")
elif op1 == op2:
    print("Tak samo się opłacają")
else:
    print ("Pizza nr 2 bardziej się opłaca")


