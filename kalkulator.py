print ("=====KALKULATOR SEDERHANA====")

#deklarasi variabel input
angka1 = int(input("masukan angka ke-1 : "))
angka2 = int(input("masukan angka ke-2 : "))

#PROSES
#HASIL = angka1 + angka2
penjumlahan = angka1 + angka2
pengurangan = angka1 - angka2
perkalian   = angka1 * angka2
pembagian   = angka1 / angka2
Mod         = angka1 % angka2

#OUTPUT
print("")
print(angka1, "+", angka2, " = ", penjumlahan)
print(angka1, "-", angka2, " = ", pengurangan)
print(angka1, "*", angka2, " = ", perkalian)
print(angka1, "/", angka2, " = ", pembagian)
print(angka1, "%", angka2, " = ", Mod)

