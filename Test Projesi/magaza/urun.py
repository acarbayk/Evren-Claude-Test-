KDV_ORANI = 0.20


class Urun:
    def __init__(self, ad, fyt, stok=0):
        self.ad = ad
        self.fyt = fyt
        self.stok = stok

    def kdvli_fiyat(self):
        """Ürünün KDV dahil fiyatını döndürür."""
        return round(self.fyt * KDV_ORANI, 2)

    def stok_dus(self, adet):
        if adet > self.stok:
            raise ValueError(f"{self.ad} için yeterli stok yok")
        self.stok -= adet
