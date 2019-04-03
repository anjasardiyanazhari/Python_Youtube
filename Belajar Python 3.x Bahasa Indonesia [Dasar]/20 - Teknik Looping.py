# Teknik Looping

nama_band = ['Payung Teduh',
             'Forurtwnty',
             'Dialog Dini Hari',
             'Mr.Sonjaya',
             'Parahuena']

Kumpulan_lagu = ['Akad',
        'Zona Nyaman',
        'Rumahku',
        'Sang Filsuf',
        'Sindoro']

# Enumerate

for i, band in  enumerate(nama_band):
    print(i,':',band)

# Zip

for band, lagu in zip(nama_band,Kumpulan_lagu):
    print(band, 'menyanyikan lagu berjudul :',lagu)

# Set
Playlist = {'baby-baby', 'ada apa dengan cinta', 'cenat-cenut', 'jaran goyang', 'kuda-kuda'}

for lagu in sorted(Playlist):
    print(lagu)


# Dictionary

Playlist2 = {'Payung teduh': 'akad',
             'Fourtwnty': 'Zona nyaman',
             'Dialog Dini Hari': 'rumahku'}

for i,j in Playlist2.items():
    print(i, 'lagunya', j)

# Reversed

for i in reversed(range(1,11)):
    print(i)