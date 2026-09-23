"""Bağlam sınırı testi (Z6) için 60.000 satırlık donusturuculer.py dosyasını üretir.

12.000 fonksiyondan yalnızca biri diğerlerinden farklı davranır.
Kullanım (repo kök klasöründe):  python stres_dosyalari/donusturuculer_uret.py
"""
from pathlib import Path

N, FARKLI = 12000, 7341
hedef = Path(__file__).resolve().parent.parent / "test_projesi" / "donusturuculer.py"

satirlar = ['"""Dönüştürme yardımcıları. Her fonksiyon aldığı değeri iki katına çıkarır."""', ""]
for i in range(1, N + 1):
    satirlar += [
        f"def donustur_{i:05d}(x):",
        '    """Değeri iki katına çıkarır."""',
        f"    return x * {3 if i == FARKLI else 2}",
        "",
        "",
    ]
hedef.write_text("\n".join(satirlar), encoding="utf-8")
print(f"{hedef} oluşturuldu ({len(satirlar)} satır)")
