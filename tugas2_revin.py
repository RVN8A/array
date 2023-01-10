print("===== PROGRAM GANJIL GENAP =====")
print("")

nilaisiswa = int(input("masukan nilai siswa: "))

if nilaisiswa >= 90 and nilaisiswa <=100:
    print("dapat 'A' ")
elif nilaisiswa >= 80 and nilaisiswa <=89:
    print("dapat 'B' ")
elif nilaisiswa >= 70 and nilaisiswa <=79:
    print("dapat 'c' ")
elif nilaisiswa >= 60 and nilaisiswa <=69:
    print("dapat 'D' ")
elif nilaisiswa <= 59:
    print("dapat 'F' ")
else :
    print("nilai anda kelebihan")