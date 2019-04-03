Barang = ['kunci','ember','jaket','ban','mobil']
print(Barang)

# Beberapa method yang bisa digunakan untuk memanipulasi list
# untuk menambah data ke dalam list
Barang.append('sepeda')
print(Barang)

Barang.extend('dompet')
print(Barang)

Barang.insert(3,'sepeda')
print(Barang)

# untuk menghitung anggota
jumlahSepeda = Barang.count('sepeda')
print("jumlah sepeda adalah:",jumlahSepeda)

# meremove data
Barang.remove('sepeda')
print(Barang)

Barang.reverse()
print(Barang)

#contoh
stuff = Barang.copy()
stuff.append('gelas')
print(stuff)
print(Barang)

