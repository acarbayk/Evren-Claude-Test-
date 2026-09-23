"""EVREN LLM API anahtarını test eder, kullanım şartlarını onaylatır, modelleri listeler."""
import os
import sys

import requests

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

BASE = os.getenv("EVREN_BASE_URL", "https://evren-llmapi.ssyz.org.tr/v1")
KEY = os.getenv("EVREN_API_KEY") or input("EVREN API anahtarını yapıştır: ").strip()
H = {"Authorization": f"Bearer {KEY}"}
TEST_MODEL = "glm-5.3"


def main():
    print("1) Kullanım şartları kontrol ediliyor...")
    r = requests.get(f"{BASE}/terms/status", headers=H, timeout=30)
    if r.status_code == 401:
        print("   Anahtar geçersiz (401). EVREN panelinden anahtarı kontrol et.")
        return
    r.raise_for_status()
    status = r.json()

    if not status.get("accepted"):
        text = requests.get(f"{BASE}/terms/text", headers=H, timeout=30).json()
        print("\n" + str(text.get("content", text)) + "\n")
        cevap = input("Şartları kabul ediyor musun? (E/h): ").strip().lower()
        if cevap not in ("e", "evet", "y", "yes"):
            print("   Kabul edilmedi, çıkılıyor.")
            return
        requests.post(
            f"{BASE}/terms/accept",
            headers=H,
            json={"version": status["current_version"]},
            timeout=30,
        ).raise_for_status()
        print("   Şartlar kabul edildi.")
    else:
        print("   Şartlar zaten kabul edilmiş.")

    print("\n2) Kullanılabilir sohbet modelleri:")
    models = requests.get(f"{BASE}/models", headers=H, timeout=30).json()
    for m in models.get("data", []):
        if m.get("task") == "chat":
            print("   -", m["id"])

    print(f"\n3) Deneme mesajı gönderiliyor ({TEST_MODEL})...")
    r = requests.post(
        f"{BASE}/chat/completions",
        headers=H,
        json={
            "model": TEST_MODEL,
            "messages": [{"role": "user", "content": "Tek cümleyle kendini tanıt."}],
        },
        timeout=120,
    )
    if r.status_code != 200:
        print("   Hata:", r.status_code, r.text)
        return
    print("   Cevap:", r.json()["choices"][0]["message"]["content"])
    print("\nEVREN bağlantısı çalışıyor. Sıradaki adım: 1_proxy_baslat.bat")


if __name__ == "__main__":
    try:
        main()
    except requests.RequestException as e:
        print("Bağlantı hatası:", e)
    input("\nKapatmak için Enter'a bas...")
