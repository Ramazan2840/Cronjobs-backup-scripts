# Otomatik Yedekleme Scripti (Cronjob-Backup)

Açık Kaynak İşletim Sistemi dersi final projesi.

### 👤 Öğrenci Bilgileri
* **Adı Soyadı:** Ramazan ÇİÇEK
* **Öğrenci No:** 2420161064

## 📝 Proje Ne Yapar?
Bu Python aracı, sistem yöneticilerinin işini kolaylaştırmak için tasarlanmıştır. Seçtiğiniz bir klasörü belirlediğiniz saniye aralıklarıyla otomatik olarak `.zip` haline getirir ve yedekler klasörüne taşır.

## 🚀 Özellikler
* **Kullanıcı Dostu:** Başlangıçta size kaynak ve hedef klasörü sorar.
* **Loglama:** Yapılan her işlem `islem_gecmisi.txt` dosyasına kaydedilir.
* **Hata Yönetimi:** Klasör yoksa oluşturur, program çökmez.

## 💻 Çalıştırma Komutu
```bash
python src/main.py