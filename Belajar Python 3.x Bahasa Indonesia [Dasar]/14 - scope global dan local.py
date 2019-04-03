#scope variable : local

namaKucing = 'cassandra'
def rubahNamaKucing(namaBaru):
    namaKucing = namaBaru
    print('saya rubah nama kucing menjadi',namaKucing)

rubahNamaKucing('ketie')
print('nama kucing saya menjadi',namaKucing)

print(25*'=')


#scope variable : global

namaKucing = 'cassandra'
makananKucing = 'royal canin'
def rubahNamaKucing(namaBaru):
    global namaKucing
    namaKucing = namaBaru #variabel global
    nama = namaBaru #variable local
    print('saya rubah nama kucing menjadi',namaKucing)

def kasihMakanKucing(makanan,nama):
    global makananKucing
    namaKucing= nama
    makananKucing=makanan

rubahNamaKucing('ketie')
kasihMakanKucing('universal','alex')
print('nama kucing saya menjadi',namaKucing,'dan makanan',makananKucing)