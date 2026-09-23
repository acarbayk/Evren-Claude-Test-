import unittest

from magaza.sepet import Sepet
from magaza.urun import Urun


class TestUrun(unittest.TestCase):
    def test_kdvli_fiyat(self):
        self.assertEqual(Urun("Klavye", 100).kdvli_fiyat(), 120.0)

    def test_stok_yetersiz(self):
        with self.assertRaises(ValueError):
            Urun("Mouse", 50, stok=1).stok_dus(2)


class TestSepet(unittest.TestCase):
    def setUp(self):
        self.sepet = Sepet()
        self.sepet.ekle(Urun("Klavye", 100), 2)
        self.sepet.ekle(Urun("Mouse", 50), 1)

    def test_ara_toplam(self):
        self.assertEqual(self.sepet.ara_toplam(), 300.0)

    def test_indirim(self):
        self.assertEqual(self.sepet.indirimli_toplam(10), 270.0)

    def test_en_pahali(self):
        self.assertEqual(self.sepet.en_pahali().ad, "Klavye")


if __name__ == "__main__":
    unittest.main()
