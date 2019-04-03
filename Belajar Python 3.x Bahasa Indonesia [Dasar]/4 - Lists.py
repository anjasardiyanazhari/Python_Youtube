Data = [1,4,9,16,25,36,49,64]

#Menampilkan
subdata = Data[4]


#Memotong
subdata1 = Data[2:4]
subdata2 = Data[:4]



print(subdata1)

Data2 = [100,200,300,400,500]

#Menambah
Data3 = Data + Data2
print(Data3)

#Merubah content dari list
print(Data)
Data[4] = 1000
print(Data)

#Mengcopy list ke variabel baru
a = Data[:]
a[7] = 900

print(Data)

#merubah contet list dengan menggunakan metode slicing
Data[3:4] = [11,12]

#list dalam list
x = [Data,Data2]

# mengakses list dalam multidimensional list
y = x[1][4]

print(x)
print(y)

#method untuk list
Data.append(30)
print(Data)

#Fungction yang bisa kita gunakan kepada list
panjang_list = len(Data)

print(Data)
print(panjang_list)
