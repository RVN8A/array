print ("====LOGIN USER====")

us = raw_input("Masukan Username: ")
pw = raw_input("Masukan password: ")
us2 =("revingawi123")
pw2 =("akmalngawi123")

if us == us2 and pw == pw2 :
    print("selamat datang di revingawi123")

elif us != us2 and pw == pw2 :
    print("username salah")

elif us == us2 and pw != pw2 :
    print("password salah")


elif us != us2 and pw != pw2 :
    print("penyusup!!!!")
