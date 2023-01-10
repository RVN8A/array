print ("======PROGRAM KASIR 3 BARANG======")

#DEKLARASI VARIABEL INPUT
B1 = raw_input("masukan B1 : ")
HargaB1 = int(input("masukan HargaB1 : "))
B2 = raw_input("masukan B2 : ")
HargaB2 = int(input("masukan HargaB2 : "))
B3 = raw_input("masukan B3 : ")
HargaB3 = int(input("masukan HargaB3 : "))
uang = int(input('masukkan uang pelanggan'))

total = HargaB1 + HargaB2 + HargaB3
diskon1 = total * 0.2
diskon2 = total - diskon1
kembalian = uang - diskon2
#Output
print B1, HargaB1
print B2, HargaB2
print B3, HargaB3
print 'total:',total
print ("selamat kamu ditembak crush dan kamu mendapat diskon 20%")
print diskon2
print 'uang pelanggan :',uang
print 'kembalianmu :', kembalian
print ("TERIMAKASI LOVE YOU FULL")

