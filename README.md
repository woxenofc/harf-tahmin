# 🔠 Harf-Tahmin Oyunu(beta)

Oyun, iki oyuncu arasında geçen, belirli dilbilgisi ve mantık kurallarına dayalı, rekabetçi bir kelime düellosu oyunudur.

## 🎮 Oyunun Mantığı ve Kuralları

Oyuncular sırayla kelime girerek rakiplerine puan kazandırmamaya çalışır. Girilen her hatalı kelime, içerdiği kural ihlali sayısı kadar rakip oyuncuya puan yazdırır. **10 puana** ilk ulaşan oyuncu maçı kazanır. 

### 📋 Uygun Kelime Şartları
Bir kelimenin geçerli sayılması için şu 5 şartı sağlaması gerekir:

1.  **Uzunluk:** Kelime en az 3 karakterden oluşmalıdır.
2.  **Harf Dizilimi:** Kelime içinde peşpeşe iki sesli harf veya peşpeşe iki sessiz harf bulunamaz.
3.  **Karakter Kontrolü:** Kelime sadece harflerden oluşmalıdır (Rakam veya sembol içeremez).
4.  **Son Harf Kuralı:** Yeni girilen kelime, bir önceki geçerli kelimenin **son harfi** ile başlamalıdır.
5.  **Tek/Çift Kuralı:** Önceki kelimenin uzunluğu **çift** ise, yeni kelime **tek** uzunlukta olmalıdır, aynı şekilde tek ise yeni kelime çift olmalıdır.

## 🚀 Kurulum ve Çalıştırma

### Gereksinimler
Sisteminizde **Python +3.x** bulunması ve **PyQt5** kütüphanesinin yüklü olması gerekir.


2.  **Kütüphaneyi yükleme:**
    ```bash
    pip install PyQt5
    ```

3.  **Oyunu Başlatın:**
    ```bash
    python harf_tahmin.py
    ```

## 🛠 Kullanılan Teknolojiler
* **Python:**
* **PyQt5:**
* **QSS (Qt Style Sheets):**

<h3 align="center">📸 Oyun Ekran Görüntüleri</h3>

<p align="center">
  <b>Giriş Ekranı</b><br>
  <img src="https://github.com/user-attachments/assets/3a2638df-64a1-415b-add9-7a965fbeb8ff" width="320" title="Kelime Ligi Başlangıç">
</p>

<p align="center">
  <b>Başlangıç Ekranı</b><br>
  <img src="https://github.com/user-attachments/assets/be2cff41-5a22-4831-a0b6-6fffc087bd1a" width="320" title="Kelime Ligi Oyun Anı">
</p>

---
Geliştiren: Batın Emirhan Taş
