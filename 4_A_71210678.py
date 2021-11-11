#Doni butuh bantuan seorang programmer dalam membuat catatan dan menghitung pengeluaran pelanggan, padahal bawa kalkulator cepet wkwk
#permisalan makanan yang dijual yaitu ikan bakar, es doger, rujak cingur

#permisalan saya menggunakan variabel
#Misal : ikan bakar(x), es doger(y), rujak cingur(z)

x = 25000
y = 6000
z = 8000

print("====MASUKKAN JUMLAH MAKANAN YANG DIPESAN====")
Ax = int(input("IKAN BAKAR        Rp 25.000,00: "))
Bx = int(input("ES DOGER          Rp 6.000,00 : "))
Cz = int(input("RUJAK CINGUR      Rp 8.000,00 : "))

print("=====TOTAL=====")
print("TOTAL IKAN BAKAR   : Rp ", (x*Ax))
print("TOTAL ES DONGER    : Rp ", (y*Bx))
print("TOTAL RUJAK CINGUR : Rp ", (z*Cz))

total =(x*Ax)+(y*Bx)+(z*Cz)
print("Jumlah total biaya yang harus dibayar adalah Rp ", total)
