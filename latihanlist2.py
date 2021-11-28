# tambah elemen list
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

# Ambil 2 bagian list A dijadikan list B
b.append(a[1:3])
print("2 bagian list A dijadikan list B:", b)

# tambah list b dengan string
b.append("saya")
print("Tambah B dengan Sring:", b)

# tambah list b dengan 3 nilai
print("Tambah list b dengan 3 nilai:", b+[11, 12, 13])

# Gabungan list B dan A
c = b+a
print("Gabungan list B dan A:", c)
