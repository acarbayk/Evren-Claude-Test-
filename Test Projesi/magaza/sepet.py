from magaza.urun import Urun


class Sepet:
    def __init__(self):
        self.kalemler = []  # (Urun, adet)

    def ekle(self, urun: Urun, adet=1):
        self.kalemler.append((urun, adet))

    def ara_toplam(self):
        """KDV dahil sepet toplamı."""
        return round(sum(u.kdvli_fiyat() * adet for u, adet in self.kalemler), 2)

    def indirimli_toplam(self, yuzde):
        """Toplama yüzde indirim uygular. yuzde: 0-100 arası."""
        toplam = self.ara_toplam()
        return round(toplam - toplam * yuzde, 2)

    def en_pahali(self):
        return max(self.kalemler, key=lambda k: k[0].fyt)[0]
