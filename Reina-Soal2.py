def positif(angka):
    return angka > 0

def negatif(angka):
    return angka < 0

def nol(angka):
    return angka == 0

def genap(angka):
    return angka % 2 == 0

def ganjil(angka):
    return angka % 2 != 0

def prima(angka):
    if angka <= 1:
        return False
    if angka <= 3:
        return True
    if angka % 2 == 0 or angka % 3 == 0:
        return False
    i = 5
    while i * i <= angka:
        if angka % i == 0 or angka % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    angka = int(input("Masukkan sebuah bilangan: "))
    
    if positif(angka):
        print("[Positif, ", end="")
    elif negatif(angka):
        print("[Negatif, ", end="")
    else:
        print("[Nol, ]", end="")
    
    if genap(angka):
        print("Genap, ", end="")
    else:
        print("Ganjil, ", end="")
    
    if prima(angka):
        print("Prima]")
    else:
        print("Komposit]")

main()