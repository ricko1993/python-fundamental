"""
semua sintaksis dasar bahasa pemrograman terdiri dari:
1. Sekuensial : langkah berurutan
2. percabangan : langkah melompat jika kondisi terpenuhi
3. perulangan : mengulang langkah yang sama berkali-kali selama/sampai kondisi terpenuhi
"""

# Sekuensial
print('Ibu berkata "pergi ketoko"')
print('Budi menjawab"baik apa yang harus saya lakukan"')
print('Ibu menjawab "belikan 1 botol susu, dan jika ada telur beli 6"')
print('maka budi berangkat ketoko')
print('dan mulai belanja')

# Percabangan
jumlah_botol_susu = 173
jumlah_telur = 873
print(f"jumlah botol susu {jumlah_botol_susu} botol")
print(f"jumlah telur {jumlah_telur} butir")

if jumlah_botol_susu > 0 :
    print("budi mengecek harga dan uang cukup")
    if jumlah_telur == 0 :
        print("Budi membeli 1 botol susu")
    else:
        print("budi membeli 6 botol telur")

else:
    print("budi tidak jadi membeli 1 botol susu")

print("budi pulang kerumah")
print("menyampaikan hasilnya kepada ibu")