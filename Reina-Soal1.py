def hitung_fpb (x,y):
    while y:
        x,y=y,x%y
        return x
    
def hitung_kpk (x,y):
    return(x*y)

angka1=int(input("Masukkan angka pertama : "))
angka2=int(input("Masukkan angka kedua : "))

fpb=hitung_fpb(angka1, angka2)
kpk=hitung_kpk(angka1, angka2)

print(f"FPB dari {angka1} dan {angka2} adalah {fpb}")
print(f"KPK dari {angka1} dan {angka2} adalah {kpk}")