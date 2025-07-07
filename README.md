# 🎮 Pac-Man AI - Seviye Sistemli Yapay Zekâlı Pac-Man Oyunu

Bu proje, klasik Pac-Man oyununa modern bir bakış kazandırarak Python ve Pygame ile geliştirilen yapay zekâ destekli bir **oyun algoritması** sunar. A* (A-Star) algoritması kullanan akıllı hayaletler, Pac-Man’in hareketlerine göre yolunu hesaplayarak oyuncuya meydan okur. Her seviyede zorluk dinamik olarak artar: harita büyür, hayalet sayısı artar ve oyun temposu hızlanır.

---

## 🆚 Klasik Pac-Man'den Farkları

| Özellik                        | Klasik Pac-Man         | Pac-Man AI Projemiz                                  |
|-------------------------------|-------------------------|------------------------------------------------------|
| 👻 Hayalet Hareketi           | Önceden tanımlı yol     | A* algoritması ile gerçek zamanlı hedef takibi       |
| 🗺️ Harita Sistemi             | Sabit tek harita        | Seviye geçildikçe genişleyen dinamik harita          |
| 📈 Seviye Sistemi             | Belirli düşman paterni  | Her seviyede +1 hayalet ve daha büyük labirent       |
| 🧠 Yapay Zekâ                 | Yok                     | A* Pathfinding algoritmasıyla AI destekli hayalet    |
| 🧩 Modülerlik & Genişletilebilirlik | Kısıtlı          | Kolayca yeni ödüller, görevler, karakterler eklenebilir |

---

## 🔧 Özellikler

- ✅ **Dinamik Seviye Sistemi**  
  Her tüm noktalar toplandığında bir sonraki seviyeye geçilir. Harita büyür ve hayalet sayısı artar.

- 🤖 **Yapay Zekâ Kontrollü Düşmanlar (A*)**  
  Her hayalet, Pac-Man’in anlık pozisyonuna göre A* algoritmasıyla en kısa yolu bulur.

- 🧱 **Gelişen Harita Tasarımı**  
  Kodla üretilebilecek şekilde ölçeklenebilir labirent yapısı.

- 🔄 **Oyun Bitti Ekranı & Yeniden Başlatma Seçeneği**

- 📊 **Skor ve Seviye Takibi**

---
## 📸 Görseller

> ![Ekran görüntüsü 2025-07-07 155246](https://github.com/user-attachments/assets/2f4a97e5-774c-4381-989a-b910eba89d2b)
> ![Ekran görüntüsü 2025-07-07 155332](https://github.com/user-attachments/assets/b18c3ff5-8a4b-4bf7-b3e9-6e2970817bfa)
> ![Ekran görüntüsü 2025-07-07 155416](https://github.com/user-attachments/assets/635b0440-b393-4453-82a1-20a66afb03f8)
> ![Ekran görüntüsü 2025-07-07 155613](https://github.com/user-attachments/assets/7c034aa6-a76b-4fdf-b046-8f0a53a1ef62)


## 🛠️ Kullanılan Teknolojiler

- Python 3.x
- Pygame
- A* (A-Star) Pathfinding Algoritması

---

## 📦 Kurulum

```bash
git clone https://github.com/kullanici-adi/pacman-ai.git
cd pacman-ai
pip install -r requirements.txt
python main.py
```

---

## 🔮 Geliştirme Planları (Yakında)

🎁 Haritaya puan getirisi olan bonus ödüller

🎨 Skor ile açılan karakter özelleştirmeleri

🧠 Pac-Man için AI kontrolü (gözlemsel öğrenme)

🌐 Web sürümü (Pygbag ile tarayıcıda oynanabilir versiyon)

---

## 👨‍💻 Geliştirici

Emir Aksu

Yapay Zekâ Operatörlüğü Öğrencisi

📍 Karabük Üniversitesi

💡 AI, oyun geliştirme ve görsel destek teknolojileri ile ilgileniyor.
