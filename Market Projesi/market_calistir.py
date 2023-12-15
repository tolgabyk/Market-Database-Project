import time

from market import *


print("""""
-------------------------------------

**** Marketimize Hoş Geldiniz ****

1- Marketi Göster

2- Ürünleri Sorgula

3- Ürün Ekle

4- Ürün Sil

5- Ürün Sayısı Ayarla

Çıkış için 'q' basınız ...

-------------------------------------

""")

marketler = supermarket()

while True:
    secim = input("Yapacağınız işlemi seçin: ")

    if secim=='q':
        print("Programdan çıkılıyor...")
        break
    elif secim =="1":
        marketler.marketi_goster()
    elif secim=="2":
        isim = input("Ürün ismini girin: ")
        print("ürün sorgulanıyor....")
        time.sleep(2)
        marketler.urun_sorgula(isim)
    elif secim=="3":
        isim = input("Ürün adı: ")
        kategori = input("Kategorisi: ")
        sayisi = int(input("Mevcut ürün Sayısı: "))
        firma = input("Firma adı: ")
        yeni_urun = market(isim,kategori,sayisi,firma)
        print("Ürün ekleniyor...")
        time.sleep(2)
        marketler.urun_ekle(yeni_urun)
        print("Ürün eklendi...")

    elif secim =="4":
        isim = input("Silinecek ürün: ")
        cevap = input("Emin misiniz (E\H):  ")

        if cevap == "E":
            print("Ürün siliniyor...")
            time.sleep(1)
            marketler.urun_sil(isim)
            print("Ürün silindi...")

    elif secim == "5":
        isim = input("Sayısı Ayarlanacak Ürün: ")
        marketler.urun_sayisi_ayarla(isim)
    else:
        print("Geçersiz İşlem...")






