ogrenciler = []
#1
ogrenciIsmi = input("Öğrenci İsmi: ")
ogrenciSoyadi = input("Öğrenci Soyadı: ")
ogrenciler.append(ogrenciIsmi+" "+ogrenciSoyadi)
print(ogrenciler)

print("************")

#2
ogrenciAdiSoyadi = input("Silmek istediğiniz öğrencinin adı ve soyadı: ")

for ogrenci in ogrenciler:
    if ogrenci == ogrenciAdiSoyadi:
        ogrenciler.remove(ogrenci)
        print(f"{ogrenciAdiSoyadi} listeden silinmiştir.")
    else:
        print(f"{ogrenciAdiSoyadi} listede bulunmamıştır.")

print("************")

# 3
sayi = int(input("Öğrenci sayısı: "))
i = 0
while(i < sayi):
    yeniOgrenci = input("Adı-Soyadı: ")
    i += 1
    ogrenciler.extend([yeniOgrenci])
print(ogrenciler)

print("************")

#4
for ogr in ogrenciler:
    print(ogr)

print("************")

#5
ogrenciNumarasi = input("Numarasını öğrenmek istediğiniz öğrencinin adı-soyadı: ")

for ogrenciNo in ogrenciler:
    if ogrenciNumarasi == ogrenciNo:
        ogrenciNo = ogrenciler.index(ogrenciNumarasi) + 1
        print("Öğrenci Numarası: ", ogrenciNo)
    else:
        print(f"{ogrenciNumarasi} listede bulunamamıştır.")

print("************")

#6
sayi2 = int(input("Silmek istediğiniz öğrenci sayısı: "))
i = 0
while(i < sayi2):
    silinenOgrenci = input("Adı-Soyadı: ")
    ogrenciler.remove(silinenOgrenci)
    i += 1
print(f"Güncel liste: {ogrenciler}")


