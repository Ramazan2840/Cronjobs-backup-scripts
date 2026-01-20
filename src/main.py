import shutil
import datetime
import os
import time
import logging

# --- RAMAZAN BACKUP LOGLARI ---
# Log dosyasi adi farkli: 'islem_gecmisi.txt'
logging.basicConfig(filename='islem_gecmisi.txt', level=logging.INFO,
                    format='%(asctime)s - ISLEM: %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

def yedeklemeyi_gerceklestir(kaynak_dizin, hedef_dizin):
    # Zaman damgasi formatini degistirdik
    zaman_etiketi = datetime.datetime.now().strftime("%Y-%m-%d__%H-%M-%S")
    dosya_ismi = f"Yedek_{zaman_etiketi}"
    tam_hedef = os.path.join(hedef_dizin, dosya_ismi)

    try:
        # Arsivleme islemi (zip)
        shutil.make_archive(tam_hedef, 'zip', kaynak_dizin)
        
        bilgi_mesaji = f"BASARILI: '{kaynak_dizin}' klasoru -> {dosya_ismi}.zip oldu."
        print(f"✅ {bilgi_mesaji}")
        logging.info(bilgi_mesaji)
        
    except Exception as hata:
        hata_mesaji = f"Yedekleme hatasi: {str(hata)}"
        print(f"❌ {hata_mesaji}")
        logging.error(hata_mesaji)

def kullanici_girisi():
    print("\n==========================================")
    print("===   OTOMATIK YEDEKLEME SISTEMI v2    ===")
    print("==========================================\n")
    
    # Sorular biraz farkli
    print("1. Hangi klasor yedeklenecek? (Bos birakirsan: ./belgelerim)")
    src = input("   Dizin: ").strip()
    if not src: src = "./belgelerim"

    print("\n2. Zip dosyalari nereye gitsin? (Bos birakirsan: ./yedekler)")
    dst = input("   Hedef: ").strip()
    if not dst: dst = "./yedekler"

    print("\n3. Kac saniyede bir tekrar etsin? (Varsayilan: 30)")
    try:
        inp = input("   Sure: ").strip()
        if not inp:
            sure = 30
        else:
            sure = int(inp)
    except:
        print("   ! Sayi girmediniz, 30 saniye ayarlandi.")
        sure = 30
        
    return src, dst, sure

if __name__ == "__main__":
    k_yol, h_yol, saniye = kullanici_girisi()

    # Klasor yoksa otomatik olustur
    if not os.path.exists(k_yol):
        os.makedirs(k_yol)
        # Test icin icine bir dosya atalim
        with open(os.path.join(k_yol, "test_dosyasi.txt"), "w") as f:
            f.write("Bu dosya yedekleme testi icin otomatik olusturuldu.")
            
    if not os.path.exists(h_yol):
        os.makedirs(h_yol)

    print(f"\nSistem Baslatildi! Periyot: {saniye} saniye.")
    print("Durdurmak icin: CTRL + C\n")
    
    logging.info(f"Program baslatildi. Kaynak: {k_yol} -> Hedef: {h_yol}")

    while True:
        yedeklemeyi_gerceklestir(k_yol, h_yol)
        time.sleep(saniye)