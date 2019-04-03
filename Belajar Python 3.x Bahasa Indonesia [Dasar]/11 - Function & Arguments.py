#fungsi dengan menggunakan argument sederhana
def siswa(nama):
    print('siswa ini:',nama)

siswa('anjas')

print(40*'=')

#fungsi dengan menggunakan keywords arguments
def guru(nama,pelajaran):
    print('guru ini bernama',nama)
    print('mengajar',pelajaran)

guru(nama='anjas',pelajaran='seni rupa')


print(40*'=')

#fungsi dengan menggunakan default arguments
def penjagaSekolah(nama,shift='siang',galak='tidak'):
    print('penjaga sekolah ini bernama:',nama)
    print('shiftnya:',shift)
    print('galak?',galak)

penjagaSekolah('Entis')
penjagaSekolah('Maman',shift='malam')