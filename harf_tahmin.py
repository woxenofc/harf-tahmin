import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                             QLineEdit, QPushButton, QLabel, QFrame, QStackedWidget, 
                             QCheckBox, QDialog)
from PyQt5.QtCore import Qt

class KuralEkrani(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Oyun Kuralları")
        self.setFixedSize(400, 320)
        self.setStyleSheet("background-color: #1a1d24; color: white; font-family: 'Segoe UI'; border: 1px solid #3498db;")
        layout = QVBoxLayout()
        baslik = QLabel("📜 OYUN KURALLARI")
        baslik.setStyleSheet("font-size: 18px; font-weight: bold; color: #3498db; border: none;")
        baslik.setAlignment(Qt.AlignCenter)
        layout.addWidget(baslik)
        
        kurallar = QLabel(
            "<b>Şart 1:</b> En az 3 karakter olmalıdır.<br><br>"
            "<b>Şart 2:</b> Peşpeşe iki sesli veya iki sessiz harf olmamalıdır.<br><br>"
            "<b>Şart 3:</b> Sadece harf içermelidir (Büyük-Küçük harf duyarsız).<br><br>"
            "<b>Şart 4:</b> Önceki kelimenin SON harfiyle başlamalıdır.<br><br>"
            "<b>Şart 5:</b> Önceki uzunluk ÇİFT ise yeni kelime TEK, TEK ise ÇİFT olmalıdır."
        )
        kurallar.setStyleSheet("font-size: 13px; border: none;")
        kurallar.setWordWrap(True)
        layout.addWidget(kurallar)
        
        btn = QPushButton("ANLADIM")
        btn.setStyleSheet("background-color: #3498db; color: white; font-weight: bold; padding: 10px; border-radius: 5px;")
        btn.clicked.connect(self.accept)
        layout.addWidget(btn)
        self.setLayout(layout)

class KazananEkrani(QDialog):
    def __init__(self, kazanan_adi, parent=None):
        super().__init__(parent)
        self.setWindowTitle("ŞAMPİYON!")
        self.setFixedSize(300, 220)
        self.setWindowFlags(Qt.Window | Qt.WindowTitleHint | Qt.CustomizeWindowHint)
        self.setStyleSheet("background-color: #1a1d24; color: white; font-family: 'Segoe UI';")
        
        layout = QVBoxLayout()
        lbl = QLabel(f"OYUN BİTTİ!\n\n🏆{kazanan_adi} KAZANDI!")
        lbl.setAlignment(Qt.AlignCenter)
        lbl.setStyleSheet("font-size: 18px; font-weight: bold; color: #f1c40f;")
        layout.addWidget(lbl)
        
        self.btn_tekrar = QPushButton("YENİDEN BAŞLA")
        self.btn_tekrar.setStyleSheet("background-color: #2ecc71; color: white; font-weight: bold; padding: 10px; border-radius: 5px; font-size: 11px;")
        self.btn_tekrar.clicked.connect(self.accept)
        layout.addWidget(self.btn_tekrar)
        
        self.btn_kapat = QPushButton("PROGRAMI KAPAT")
        self.btn_kapat.setStyleSheet("background-color: #e74c3c; color: white; font-weight: bold; padding: 10px; border-radius: 5px;")
        self.btn_kapat.clicked.connect(self.reject)
        layout.addWidget(self.btn_kapat)
        self.setLayout(layout)

class HarfTahmin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Harf Tahmin (beta)")
        self.setFixedSize(500, 800) 
        self.reset_game_data()
        
        self.setStyleSheet("""
            QWidget { background-color: #0c0e12; color: #e0e0e0; font-family: 'Segoe UI'; }
            QFrame#MainContainer { background-color: #1a1d24; border: 2px solid #3498db; border-radius: 20px; }
            QFrame#WordBadge { background-color: #2c3e50; border-radius: 15px; border: 1px dashed #3498db; margin: 10px; }
            QFrame#StatusPanel { background-color: #11141a; border-radius: 10px; border: 1px solid #2c3e50; }
            QLineEdit { 
                background-color: #0c0e12; border: 1px solid #3d4450; border-radius: 8px; 
                padding: 12px; color: #3498db; font-size: 16px; font-weight: bold;
            }
            QPushButton { background-color: #3498db; color: white; border-radius: 10px; padding: 14px; font-weight: bold; }
            QPushButton:hover { background-color: #2980b9; }
            QPushButton#RuleBtn { background-color: #f39c12; }
            QPushButton#GameRuleBtn { background-color: #5d6d7e; font-size: 11px; padding: 8px; }
            QLabel#Title { font-size: 40px; font-weight: bold; color: #3498db; }
            QLabel#CurrentWordLabel { color: #f1c40f; font-size: 26px; font-weight: bold; }
        """)
        self.init_ui()

    def reset_game_data(self):
        self.p1_puan = 0
        self.p2_puan = 0
        self.aktif_oyuncu = 1
        self.onceki_kelime = ""

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.stack = QStackedWidget()

        self.giris_widget = QWidget()
        g_layout = QVBoxLayout(self.giris_widget)
        g_layout.setAlignment(Qt.AlignCenter)
        g_layout.setSpacing(15)

        title = QLabel("KELİME OYUNU"); title.setObjectName("Title")
        g_layout.addWidget(title, alignment=Qt.AlignCenter)

        self.p1_isim = QLineEdit(); self.p1_isim.setPlaceholderText("1. Oyuncu Adı")
        self.p2_isim = QLineEdit(); self.p2_isim.setPlaceholderText("2. Oyuncu Adı")
        g_layout.addWidget(self.p1_isim); g_layout.addWidget(self.p2_isim)

        btn_init_rules = QPushButton("📖 OYUN KURALLARINI GÖR"); btn_init_rules.setObjectName("RuleBtn")
        btn_init_rules.clicked.connect(self.kurallari_goster)
        g_layout.addWidget(btn_init_rules)

        self.check_onay = QCheckBox("Kuralları okudum ve anladım.")
        self.check_onay.setEnabled(False)
        self.check_onay.stateChanged.connect(lambda: self.btn_basla.setEnabled(self.check_onay.isChecked()))
        g_layout.addWidget(self.check_onay, alignment=Qt.AlignCenter)

        self.btn_basla = QPushButton("MAÇI BAŞLAT"); self.btn_basla.setEnabled(False)
        self.btn_basla.clicked.connect(self.oyunu_baslat)
        g_layout.addWidget(self.btn_basla)

        self.oyun_widget = QFrame(); self.oyun_widget.setObjectName("MainContainer")
        o_layout = QVBoxLayout(self.oyun_widget)
        o_layout.setContentsMargins(30, 20, 30, 20)

        self.lbl_skor = QLabel(); self.lbl_skor.setAlignment(Qt.AlignCenter)
        self.lbl_skor.setStyleSheet("font-size: 18px; color: #f1c40f; font-weight: bold; padding: 5px;")
        o_layout.addWidget(self.lbl_skor)

        self.lbl_sira = QLabel(); self.lbl_sira.setStyleSheet("font-size: 22px; color: #3498db; font-weight: bold;")
        o_layout.addWidget(self.lbl_sira, alignment=Qt.AlignCenter)

        word_frame = QFrame(); word_frame.setObjectName("WordBadge")
        wf_layout = QVBoxLayout(word_frame)
        wf_layout.addWidget(QLabel("SON GEÇERLİ KELİME:"), alignment=Qt.AlignCenter)
        self.lbl_son_kelime = QLabel("---"); self.lbl_son_kelime.setObjectName("CurrentWordLabel")
        wf_layout.addWidget(self.lbl_son_kelime, alignment=Qt.AlignCenter)
        o_layout.addWidget(word_frame)

        self.txt_kelime = QLineEdit(); self.txt_kelime.setPlaceholderText("Kelimenizi yazın...")
        self.txt_kelime.returnPressed.connect(self.hamle_yap)
        o_layout.addWidget(self.txt_kelime)

        status_panel = QFrame(); status_panel.setObjectName("StatusPanel"); status_panel.setFixedHeight(110)
        sp_layout = QVBoxLayout(status_panel)
        self.lbl_log = QLabel("Oyun başladı, ilk kelimeyi girin."); self.lbl_log.setWordWrap(True)
        self.lbl_log.setAlignment(Qt.AlignCenter)
        self.lbl_log.setStyleSheet("font-size: 14px; color: #bdc3c7; border: none;")
        sp_layout.addWidget(self.lbl_log)
        o_layout.addWidget(status_panel)
        
        o_layout.addStretch()

        btn_remember = QPushButton("❔ KURALLAR"); btn_remember.setObjectName("GameRuleBtn")
        btn_remember.clicked.connect(self.kurallari_goster)
        o_layout.addWidget(btn_remember, alignment=Qt.AlignCenter)

        self.stack.addWidget(self.giris_widget)
        self.stack.addWidget(self.oyun_widget)
        self.layout.addWidget(self.stack)
        self.setLayout(self.layout)

    def kurallari_goster(self):
        dlg = KuralEkrani(self)
        dlg.exec_()
        self.check_onay.setEnabled(True)

    def oyunu_baslat(self):
        self.p1_ad = self.p1_isim.text().upper() or "OYUNCU 1"
        self.p2_ad = self.p2_isim.text().upper() or "OYUNCU 2"
        self.guncelle_arayuz()
        self.stack.setCurrentIndex(1)

    def kelime_kontrol(self, kelime):
        hatalar = []
        sesli = "aeıioöuüAEIİOÖUÜ"
        sessiz = "bcçdfgğhjklmnprsştvyzBCÇDFGĞHJKLMNPRSŞTVYZ"
        alfabe = sesli + sessiz

        if len(kelime) < 3: hatalar.append("- Şart 1: En az 3 karakter olmalı.")
        for harf in kelime:
            if harf not in alfabe:
                hatalar.append("- Şart 3: Sadece harflerden oluşmalıdır.")
                break
        for i in range(1, len(kelime)):
            h1, h2 = kelime[i-1], kelime[i]
            if (h1 in sesli and h2 in sesli) or (h1 in sessiz and h2 in sessiz):
                hatalar.append("- Şart 2: Peşpeşe iki aynı tür harf.")
                break
        
        if self.onceki_kelime:
            o_k = self.onceki_kelime.lower()
            k = kelime.lower()
            if k[0] != o_k[-1] and not (k[0] == 'i' and o_k[-1] == 'i'):
                hatalar.append(f"- Şart 4: '{o_k[-1].upper()}' harfiyle başlamalıydı.")
            
            o_cift = len(o_k) % 2 == 0
            k_cift = len(k) % 2 == 0
            if o_cift == k_cift: 
                durum = "TEK" if o_cift else "ÇİFT"
                hatalar.append(f"- Şart 5: Uzunluk {durum} olmalıydı.")
        return hatalar

    def hamle_yap(self):
        kelime = self.txt_kelime.text().strip()
        if not kelime: return

        hatalar = self.kelime_kontrol(kelime)
        if hatalar:
            ceza = len(hatalar)
            if self.aktif_oyuncu == 1: self.p2_puan += ceza
            else: self.p1_puan += ceza
            self.lbl_log.setText(f"<font color='#e74c3c'><b>DİKKAT!</b><br>{'<br>'.join(hatalar)}</font>")
        else:
            self.onceki_kelime = kelime
            self.lbl_log.setText(f"<font color='#2ecc71'><b>HARİKA!</b><br>'{kelime.upper()}' kelimesi geçerli kabul edildi.</font>")

        self.txt_kelime.clear()
        self.aktif_oyuncu = 2 if self.aktif_oyuncu == 1 else 1
        self.guncelle_arayuz()
        self.kontrol_oyun_bitti()

    def guncelle_arayuz(self):
        self.lbl_skor.setText(f"🏆 {self.p1_ad}: {self.p1_puan}  |  {self.p2_ad}: {self.p2_puan}")
        sira = self.p1_ad if self.aktif_oyuncu == 1 else self.p2_ad
        self.lbl_sira.setText(f"SIRA: {sira}")
        self.lbl_son_kelime.setText(self.onceki_kelime.upper() if self.onceki_kelime else "---")

    def kontrol_oyun_bitti(self):
        winner = ""
        if self.p1_puan >= 10: winner = self.p1_ad
        elif self.p2_puan >= 10: winner = self.p2_ad

        if winner:
            dlg = KazananEkrani(winner, self)
            if dlg.exec_():
                self.reset_game_data()
                self.lbl_log.setText("Yeni maç başladı. Başarılar!")
                self.guncelle_arayuz()
            else:
                self.close()

app = QApplication(sys.argv)
ex = HarfTahmin()
ex.show()
sys.exit(app.exec_())
