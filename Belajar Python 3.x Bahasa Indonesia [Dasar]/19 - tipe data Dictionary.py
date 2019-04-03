# dictionary
#         Key,Values

member1 = {"ID":1710,
           "Nama":"Anjas ardiyan A",
           "Pekerjaan":"Mahasiswa",
           "Status":"Gold"
           }

member2 = {"ID":1720,
           "Nama":"Ayam panggang",
           "Pekerjaan":"Potong ayam",
           "Status":"Sekarat"
           }


# print(member1["Pekerjaan"])
# print(member1.keys())
# print(member1.values())
# print(member1.items())

memberlist = {1710:member1,1720:member2}

print(memberlist[1710])
