#Codificador y decodificador cesar
#Practica04
#Delgadillo Villegas Edgar Antonio
abc = "abcdefghijklmnopqrstuvwxyz"
codificado = ""
print("--------------------------------")
print("Codificador y Decodificador cesar")
print("--------------------------------\n")

t = input("Ingresar texto a modificar: ")
arch = open("Archivo.txt","w")
arch.write(t)
arch.close()
print("texto: ")
arch = open("Archivo.txt", "r")
print(arch.read())
arch.close()
print("\ntexto codificado: ")
arch = open("Archivo.txt","r")
archmod = open("archivoCod.txt", "w")

for l in arch:
    for letra in l:
        if letra in abc:
            ind = abc.find(letra)
            ind += 1
            if ind > 26:
                ind - 26
            codificado += abc[ind]
        else:
           codificado += letra
archmod.write(codificado)
arch.close()
archmod.close()
archmod = open("archivoCod.txt","r")
print(archmod.read())
archmod.close()

print("\ntexto decodificado: ")
archdes = open("archivoDec.txt","w")
archmod = open("archivoCod.txt","r")

deco = ""
for l in archmod:
    for letra in l:
        if letra in abc:
            ind = abc.find(letra)
            ind -= 1
            if ind == 1:
                ind + 25
            deco += abc[ind]
        else:
           deco += letra
archdes.write(deco)
archdes.close()
archmod.close()
archdes = open("archivoDec.txt","r")
print(archdes.read())
archdes.close()