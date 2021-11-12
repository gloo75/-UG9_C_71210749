#SOAL N0 2 a

string = input("Masukan kalimat : ")

substring = input("Masukan kata untuk dihitung : ")

count = string.count(substring)

print('ada', count, 'buah kata', substring)


#SOAL NO 2 b

string = input("Masukan kalimat : ")

substring = input("Masukan kata untuk dihitung : ")

count = string.casefold().count(substring)

print('ada', count, 'buah kata', substring)
