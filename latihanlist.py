list=["a", "b", "c", "d", "e"]


print("Tampilkan Element ke 3:", list[2])
print("ambil Element ke 2 sampai 4:", list[1:4])
print("ambil elemen terakhir:", list[5-1])


# merubah elemen ke 4 dengan nilai lain
list[3] = "f"

print("merubah elemen ke 4 dengan nilai lain:", list)

# merubah elemen ke 4 sampai terakhir
list[3:] = "f", "g"
print("merubah elemen ke sampai elemen terakhir:", list)
