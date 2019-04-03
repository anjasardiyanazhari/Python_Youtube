#list sebagai itereble
gorengan = ['tahu isi', 'tempe goreng', 'bakwan', 'pisang goreng', 'ubi goreng ']

for g in gorengan:
    print(g)
    print(len(g))

#string sebagai iterable
bakwan = 'bakwan'

for i in bakwan:
    print(i)

#for di dalam for
buah = ['semangka', 'jeruk', 'aple', 'anggur']
sayur = ['kangkung', 'wortel', 'tomat', 'kentang']

daftar_belanja = [gorengan, buah, sayur]

print(daftar_belanja)

print(70 *'=')

for subDaftarBelanja in daftar_belanja:
    print(subDaftarBelanja)
    for komponen in subDaftarBelanja:
        print(komponen)

