barang_1 = 10
barang_2 = 20
barang_3 = 30
total = 0

while True:
    barang = int(input("barang:"))
    jumlah = int(input("jumlah"))
    if barang == 1:
        harga = barang_1
    elif barang == 2:
        harga = barang_2
    elif barang == 3:
        harga =barang_3
    else:
        print("salah")
        
    total = harga * jumlah + total
    print (total)
    lagi = input("lagi?")
    if lagi !="y":
     break 
    
# ===================================================================

m_coklat = 20000
m_keju = 25000
m_kismis = 15000
p_coklat = 15000
p_keju = 20000
p_kismis = 15000
total = 0
jml_m_coklat = 0
jml_m_keju = 0
jml_m_kismis = 0
jml_p_coklat = 0
jml_p_keju = 0
jml_p_kismis = 0


while True:
    beli = int(input("Beli: "))
    jumlah = int(input("jumlah: "))
    if beli == 1:
        harga = m_coklat
    elif beli == 2:
        harga = m_keju
    elif beli == 3:
        harga = m_kismis
    elif beli == 4:
        harga = p_keju
    elif beli == 5:
        harga = p_coklat
    elif beli == 6:
        harga = p_kismis
    else:
        print("salah")
    total = harga * jumlah + total
    print(total)
    lagi = input("lagi?")
    if lagi !="y":
        break
# =====================================================================
def hitung_luas_persegi():
    sisi = int(input("sisi: "))
    luas = sisi * sisi
    print(luas)

berapa = int(input("berapa? "))
for i in range (0, berapa):
    hitung_luas_persegi()
# =====================================================================
def hitung_luas_persegi(sisi):
    luas = sisi * sisi
    print(luas)

sisi = int(input("sisi: "))
hitung_luas_persegi(sisi)
# =====================================================================
def hitung_luas_persegi():
    sisi = int(input("sisi: "))
    luas = sisi * sisi
    return luas
    
    
luas = hitung_luas_persegi()
print (luas)
# =====================================================================
def hitung_luas_persegi(sisi):
    luas = sisi * sisi
    return luas

sisi = int(input("sisi? "))
luas = hitung_luas_persegi(sisi)
print (luas)