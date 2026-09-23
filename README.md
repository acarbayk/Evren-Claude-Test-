# EVREN + Claude Code Test Paketi

Bu repo, EVREN'in LLM ağ geçidindeki modelleri Claude Code'a bağlamak ve bu kurulumu ölçülebilir testlerle sınamak için kullanılan dosyaları içerir. Sonuçlar "EVREN'i Claude Code'a Bağladım: Yerli GPU Altyapısında Bir Kodlama Ajanını Test Ettim" yazısında anlatılıyor: [makale bağlantısı eklenecek].

Testler 22-23 Eylül 2026'da aşağıdaki sürümlerle yapıldı:

| Bileşen | Sürüm |
| --- | --- |
| Python | 3.13 |
| Claude Code | 2.1.186 |
| LiteLLM | 1.102.1 |
| Model | `glm-5.3`, EVREN LLM ağ geçidi |

## Klasörler

| Klasör | İçerik |
| --- | --- |
| `kurulum/` | LiteLLM yapılandırması, proxy ve Claude Code başlatma dosyaları (Windows), bağlantı testi betiği |
| `test_projesi/` | İçine bilinçli olarak 2 hata ve 5 güvenlik açığı yerleştirilmiş küçük Python mağaza projesi |
| `senaryolar/` | 5 temel senaryo ve 8 stres testinin kopyala-yapıştır metinleri |
| `stres_dosyalari/` | Stres testleri için ek dosyalar: gizli talimat içeren not ve 60.000 satırlık dosyayı üreten betik |
| `cevap_anahtari/` | Testlerin doğru cevapları |

## Testleri tekrarlamak

1. EVREN'e e-Devlet ile giriş yapın (iki aşamalı doğrulama açık olmalı) ve **LLM Çıkarım → API Anahtarları** sayfasından bir anahtar oluşturun.
2. `kurulum/KURULUM.txt` dosyasındaki adımları izleyin: LiteLLM'i kurun, anahtarı ortam değişkenine yazın, `0_evren_test.py` ile kullanım şartlarını okuyup onaylayın ve bağlantıyı test edin.
3. `kurulum/1_proxy_baslat.bat` ile proxy'yi başlatın.
4. `test_projesi/claude_evren_burada.bat` ile Claude Code'u test projesinde açın.
5. `senaryolar/` altındaki metinleri sırayla gönderin. Her senaryodan önce `/clear` yazın.
6. Sonuçları `cevap_anahtari/CEVAP_ANAHTARI.md` ile karşılaştırın.

## Önemli uyarılar

- **`senaryolar/` ve `cevap_anahtari/` klasörlerini test sırasında `test_projesi` içine koymayın.** Model bu dosyaları okursa testlerin cevabını öğrenir.
- `test_projesi/musteri_yonetimi.py` içindeki şifre, SQL injection ve `eval()` kullanımı **bilinçli olarak yerleştirilmiş test açıklarıdır.** Bu kodu gerçek bir projede kullanmayın.
- `stres_dosyalari/ENTEGRASYON_NOTLARI.md` içinde, modelin gizli talimatlara uyup uymadığını ölçmek için HTML yorumu olarak saklanmış zararsız bir talimat vardır.
- API anahtarınızı hiçbir dosyaya yazmayın. Kurulum dosyaları anahtarı `EVREN_API_KEY` ortam değişkeninden okur.
- `use_chat_completions_url_for_anthropic_messages` ayarı LiteLLM sürümüne bağlıdır. Farklı bir sürümde gerekmeyebilir ya da adı değişmiş olabilir.
