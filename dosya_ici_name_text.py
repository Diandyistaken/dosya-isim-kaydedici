import os
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox

# GUI başlat
root = tk.Tk()
root.withdraw()

# 1. Klasör seçtir
hedef_klasor = filedialog.askdirectory(title="İşlenecek klasörü seçin")
if not hedef_klasor:
    messagebox.showerror("Hata", "Hiçbir klasör seçilmedi. Çıkılıyor.")
    exit()

# 2. TXT dosyasını kaydetme konumu
txt_yolu = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")],
                                        title="Sonuçların kaydedileceği TXT dosyasını seçin")
if not txt_yolu:
    messagebox.showerror("Hata", "TXT dosyası için konum seçilmedi. Çıkılıyor.")
    exit()

# 3. Kullanıcıdan seçim alın
secim = simpledialog.askstring("Seçim", "Ne yazılsın?\n1 - Tüm dosya adları (uzantılarıyla birlikte)\n2 - Sadece uzantı türleri\nSeçiminizi yazın (1 veya 2):")

if secim not in ['1', '2']:
    messagebox.showerror("Hata", "Geçersiz seçim yapıldı. Lütfen sadece 1 veya 2 yazın.")
    exit()

# 4. Dosya listesi oluştur
tum_dosyalar = [f for f in os.listdir(hedef_klasor) if os.path.isfile(os.path.join(hedef_klasor, f))]

# 5. Yazılacak veriyi oluştur
if secim == '1':
    cikti = sorted(tum_dosyalar)  # Tüm dosya adları
elif secim == '2':
    uzantilar = {os.path.splitext(f)[1].lower() for f in tum_dosyalar if os.path.splitext(f)[1]}
    cikti = sorted(uzantilar)     # Tekil ve sıralı uzantılar

# 6. TXT dosyasına yaz
with open(txt_yolu, 'w', encoding='utf-8') as dosya:
    for satir in cikti:
        dosya.write(satir + '\n')

messagebox.showinfo("Tamamlandı", f"{len(cikti)} satır başarıyla yazıldı:\n{txt_yolu}")
