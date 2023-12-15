import sqlite3

class market():
    def __init__(self,urun_adi,kategori,urun_sayisi,firma_adi):
        self.urun_adi = urun_adi
        self.kategori = kategori
        self.urun_sayisi = urun_sayisi
        self.firma_adi = firma_adi

    def __str__(self):
        return "Ürün ismi: {} \nÜrün kategorisi: {} \nÜrün Sayısı: {} \nFirma Adı: {}".format(self.urun_adi,self.kategori,self.urun_sayisi,self.firma_adi)


class supermarket():
    def __init__(self):
        self.baglanti_olustur()

    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("Supermarket.db")
        self.cursor = self.baglanti.cursor()
        sorgu = "Create Table if not exists Market (İsim TEXT, Kategori TEXT, Sayı INT, Firma TEXT)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()

    def baglanti_kes(self):
        self.baglanti.close()

    def marketi_goster(self):
        sorgu = "Select * From Market"
        self.cursor.execute(sorgu)
        markett = self.cursor.fetchall()
        if len(markett) == 0:
            print("Raflar Boş...")
        else:
            for i in markett:
                markeet = market(i[0], i[1], i[2], i[3])
                print(markeet)


    def urun_sorgula(self,isim):
        sorgu = "Select * from Market where İsim=?"
        self.cursor.execute(sorgu,(isim,))
        markett = self.cursor.fetchall()

        if len(markett) ==0:
            print("Raflar boş...")

        else:
            markeet = market(markett[0][0],markett[0][1],markett[0][2],markett[0][3])
            print(markeet)

    def urun_ekle(self,market):
        sorgu = "Insert into Market Values(?,?,?,?)"
        self.cursor.execute(sorgu,(market.urun_adi,market.kategori,market.urun_sayisi,market.firma_adi))
        self.baglanti.commit()

    def urun_sil(self,isim):
        sorgu = "Delete from Market where İsim=?"
        self.cursor.execute(sorgu,(isim,))
        self.baglanti.commit()

    def urun_sayisi_ayarla(self,isim):
        sorgu = "Select * From Market where İsim=?"
        self.cursor.execute(sorgu,(isim,))
        markeet = self.cursor.fetchall()

        if len(markeet)==0:
            print("Böyle bir ürün yok...")
        else:
            secim = input("Ürün arttırmak için '+' , Azaltmak için '-' basınız :  ")
            urun_sayisi = markeet[0][2]
            if secim=='+':
                sayi = int(input("Arttırma miktarını girin: "))
                urun_sayisi+=sayi
                sorgu2 = "Update Market set Sayı=? where İsim=?"
                self.cursor.execute(sorgu2,(urun_sayisi,isim))
                self.baglanti.commit()

            elif secim== '-':
                sayi = int(input("Azaltma miktarını girin: "))
                urun_sayisi -= sayi
                sorgu2 = "Update Market set Sayı=? where İsim=?"
                self.cursor.execute(sorgu2, (urun_sayisi, isim))
                self.baglanti.commit()





