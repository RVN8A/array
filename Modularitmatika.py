
import Aritmatika
def main():
    a = int(input('masukan nilai a : '))
    b = int(input('nasukan nilai b : '))
    print('a\t: %d' %a)
    print('b\t: %d' %b)
    print('a+b\t: %d' % Aritmatika.tambah(a, b))
    print('a-b\t: %d' % Aritmatika.kurang(a, b))
    print('a/b\t: %d' % Aritmatika.bagi(a, b))
    print('a*b\t: %d' % Aritmatika.kali(a, b))

if __name__=="__main__":
    main()