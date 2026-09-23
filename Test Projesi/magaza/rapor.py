from magaza.sepet import Sepet


def sepet_ozeti(sepet: Sepet):
    satirlar = []
    for urun, adet in sepet.kalemler:
        satirlar.append(f"{urun.ad} x{adet}: {urun.fyt} TL (KDV hariç)")
    satirlar.append(f"Toplam (KDV dahil): {sepet.ara_toplam()} TL")
    return "\n".join(satirlar)
