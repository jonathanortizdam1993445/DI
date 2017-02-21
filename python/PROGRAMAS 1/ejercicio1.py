print("Indica valor de A");
varA=input();
print("Indica valor de B");
varB=input();
if varA.isdigit()==False or varB.isdigit()==False:
    print("cadena involucrada");
elif varA > varB:
    print("Grande");
elif varA==varB:
    print("Igual");
else:
    print("Mas pequeño");
