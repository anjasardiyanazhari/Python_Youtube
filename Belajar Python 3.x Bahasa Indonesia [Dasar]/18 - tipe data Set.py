# Set, himpunan:

superhero = {"wiro sableng",
             "si buta dari goa hantu",
             "saras",
             "gundala",
             "gatot kaca"}

superhero.add("mak lampir")
superhero.add("gundala")

print(sorted(superhero))

print(25*'=')

ganjil = {1,3,5,7,9}
genap = {2,4,6,8,10}
prima = {2,3,5,7}

print(ganjil.union(genap))
print(ganjil.intersection(prima))