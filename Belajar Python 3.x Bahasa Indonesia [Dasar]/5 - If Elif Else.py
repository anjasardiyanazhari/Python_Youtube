nilai = 49

if nilai == 75: #equal eksplisit
    print("nilai anda:", nilai)

if nilai is not 60: #equal
    print("nilai anda:", nilai)

if nilai is not 60: #not equal
    print("nilai anda bukan: 60")

print(20 *"=")

if 80 <= nilai <= 100:
    print("nilai anda adalah A")
elif 70 <= nilai < 80:
    print("nilai anda adalah B")
elif 60 <= nilai < 70:
    print("nilai anda adalah C")
elif 50 <= nilai < 60:
    print("nilai anda adalah D, anda harus lakukan perbaikan")
else:
    print("maaf anda harus ngulang tahun depan")

print(21*"+")

sate={"ayam", "kambing", "kerbau", "kuda", "jerapah"}
beli = "ayam"

if beli in sate:
    print('Bibik bilang,"ya, saya jual sate',beli,'"')

if not beli in sate:
    print('Bibik bilang,"saya ndk jual sate',beli,'"')

print(21*"-")

karakter = "a"
if karakter in beli:
    print("ada", karakter,"di", beli)

else:
    print("tidak ada",karakter,"di", beli)
