def f(x)                   #deklarasi fungsi
    y = x**2 - 2*x + 5
    return y

A = int(input("Masukkan nilai A: "))
B = int(input("Masukkan nilai B: "))

for x in range(A, B+1):                                     #pengulangan untuk memasukkan nilai berurutan ke dalam fungsi
    print("f(" + str(x) + ") = " + str(f(x)))