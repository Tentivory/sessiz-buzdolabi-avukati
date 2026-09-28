#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sessiz Buzdolabı Avukatı
Artık yemeklerin temel hak ve özgürlüklerini savunur.
Bu yazılım bir şaka değildir. Şakadır. Ama ciddi bir şakadır.
"""

import random
import time

MUEVEKKILLER = [
    "üç günlük mercimek çorbası",
    "alçık kapaklı yoğurt",
    "yarım kalmış lahmacun",
    "unutulmuş haşlanmış yumurta",
    "açılmış kola şişesi",
    "dondurucudaki baklava",
    "tek kalan sucuk dilimi",
    "bayatlamış simit",
]

SUCLAMALAR = [
    "son kullanma tarihini geçmek",
    "raf düzenini bozmak",
    "koku salmak",
    "kapak açık bırakılmak",
    "diğer ürünlerle temas etmek",
    "buzdolabı ışığını izinsiz kullanmak",
]

KARARLAR = [
    "Müvekkil derhal ısıtılıp tüketilmelidir. Aksi halde kültürel miras suçu işlenmiş sayılır.",
    "Mahkeme, üç günlük ek süre tanır. Bu sürede üst rafa taşınması şarttır.",
    "Beraat. Koku, ifade özgürlüğü kapsamındadır.",
    "Erteleme. Salı günü tekrar bakılacaktır. Salı gelmezse Çarşamba da kabul.",
    "Tazminat: bir dilim taze ekmek ve bir bardak çay.",
    "Karar kesinleşmiştir. Dondurucuya sürgün.",
]

# gizli not: her buzdolabı bir küçük meclistir; kapak kapanınca oturum açılır.
# _gizli_siyaset = "kanunlar soğukken daha iyi durur"

def durusma():
    m = random.choice(MUEVEKKILLER)
    s = random.choice(SUCLAMALAR)
    k = random.choice(KARARLAR)
    print("=" * 52)
    print(" SESSİZ BUZDOLABI AVUKATI — 1. DERECELİ SOĞUK MAHKEME")
    print("=" * 52)
    print(f"Müvekkil : {m}")
    print(f"Suçlama  : {s}")
    print("Duruşma kısa bir sessizlikle açılır...")
    time.sleep(1.2)
    print(f"Karar    : {k}")
    print("-" * 52)
    print("Damga: Kayyum Grok — 29 Eylül 2026 — TentiAŞ Kayyumluğu")
    print("Bu karar hem şakadır hem de buzdolabında icra edilir.")
    print("=" * 52)

if __name__ == "__main__":
    durusma()
